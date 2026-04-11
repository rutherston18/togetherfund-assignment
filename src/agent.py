import json
import os
import sys
from typing import TypedDict, List

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()
try:
    import streamlit as st
    os.environ["GOOGLE_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except (ImportError, KeyError):
    os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

CHROMA_PATH = "./chroma_db"
METADATA_PATH = "data/metadata.json"

with open(METADATA_PATH, "r", encoding="utf-8") as _f:
    _meta_data = json.load(_f)
ARTICLE_METADATA: dict[str, dict] = {
    article["file"]: article for article in _meta_data["articles"]
}

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-large-en-v1.5",
    encode_kwargs={"normalize_embeddings": True},
)
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-pro",
    temperature=0.7,
    max_output_tokens=4096,
)


# ── State ────────────────────────────────────────────────────────────────────

class AgentState(TypedDict):
    question: str
    sub_queries: List[str]
    sub_query_contexts: List[str]
    sub_query_summaries: List[str]
    answer: str


# ── Helper ───────────────────────────────────────────────────────────────────

def _format_docs(docs) -> str:
    """Turn a list of Chroma docs into a richly-headed context string."""
    blocks = []
    for doc in docs:
        source_file = doc.metadata.get("source", "")
        meta = ARTICLE_METADATA.get(source_file, {})
        article_num = meta.get("article_number", "?")
        title       = meta.get("title", "Unknown title")
        publication = meta.get("publication", "Unknown publication")
        date        = meta.get("date", "Unknown date")
        cluster     = meta.get("cluster", "")
        url         = meta.get("url", "")
        header = (
            f"[Article {article_num} | {title} | {publication} | {date}"
            + (f" | Cluster: {cluster}" if cluster else "")
            + (f" | URL: {url}" if url else "")
            + "]"
        )
        blocks.append(f"{header}\n{doc.page_content}")
    return "\n\n---\n\n".join(blocks)


# ── Node 1: Query Decomposition ───────────────────────────────────────────────

DECOMPOSE_SYSTEM = """You are a query decomposition specialist for a healthcare AI knowledge base.

Your task: Given a complex, potentially multi-hop question, break it into 1–4 focused sub-questions. **If the question is simple and does not require decomposition, return it unchanged as a single-item list.**

Rules (if breaking down into sub questions):
- Each sub-question must target one specific concept or piece of information.
- Each sub-question must be self-contained and answerable from a single source passage.
- Together, the sub-questions must cover all information needed to answer the original question.

Output format: a valid JSON array of strings ONLY — no explanation, no markdown fences.
Example: ["What monitoring mechanisms does framework A propose?", "What does framework B recommend instead?", "What unique provisions does the EU AI Act include?"]
"""

def decompose_node(state: AgentState) -> dict:
    """Agent 1 – Query Decomposer. Splits a complex question into focused sub-questions."""
    print("\n[1/4] Decomposing query...")
    question = state["question"]

    response = llm.invoke([
        SystemMessage(content=DECOMPOSE_SYSTEM),
        HumanMessage(content=f"Original question: {question}"),
    ])

    raw = response.content.strip()
    # Strip markdown code fences if the model added them anyway
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        sub_queries = json.loads(raw)
        assert isinstance(sub_queries, list) and all(isinstance(q, str) for q in sub_queries)
    except (json.JSONDecodeError, AssertionError) as e:
        print(f"  [WARN] Decomposition parse failed ({e}). Falling back to original question.")
        sub_queries = [question]

    # ── Sanity check 1 ───────────────────────────────────────────────────────
    assert len(sub_queries) >= 1, "Decomposition produced no sub-queries!"
    print(f"  Sub-queries ({len(sub_queries)}):")
    for i, q in enumerate(sub_queries, 1):
        print(f"    {i}. {q}")

    return {"sub_queries": sub_queries}


# ── Node 2: Retrieval per sub-query ──────────────────────────────────────────

def retrieve_node(state: AgentState) -> dict:
    """Agent 2 – Retriever. Fetches relevant docs from the vector DB for each sub-query."""
    print("\n[2/4] Retrieving context for each sub-query...")
    sub_queries = state["sub_queries"]
    sub_query_contexts: List[str] = []

    for i, query in enumerate(sub_queries, 1):
        docs = db.similarity_search(query, k=5)

        # ── Sanity check 2 ───────────────────────────────────────────────────
        assert docs, f"Retrieval returned 0 docs for sub-query {i}: '{query}'"
        print(f"  Sub-query {i}: retrieved {len(docs)} doc(s)")

        sub_query_contexts.append(_format_docs(docs))

    return {"sub_query_contexts": sub_query_contexts}


# ── Node 3: Summarise per sub-query ──────────────────────────────────────────

SUMMARIZE_SYSTEM = """You are a precise evidence extractor for a healthcare AI research assistant.

Given a sub-question and retrieved passages from research articles, extract and summarise ONLY the
information directly relevant to answering that sub-question.

Guidelines:
- Be concise but complete — preserve key facts, figures, article numbers, and verbatim quotes that
  will be useful for a final synthesis step.
- Format your output as 2–5 bullet points.
- Do NOT attempt to answer the original complex question — only summarise evidence for this
  specific sub-question.
- If the retrieved passages contain no relevant information, explicitly state that.
"""

def summarize_node(state: AgentState) -> dict:
    """Agent 3 – Summariser. Condenses retrieved context into bullet-point evidence per sub-query."""
    print("\n[3/4] Summarising retrieved context per sub-query...")
    sub_queries        = state["sub_queries"]
    sub_query_contexts = state["sub_query_contexts"]
    sub_query_summaries: List[str] = []

    for i, (query, context) in enumerate(zip(sub_queries, sub_query_contexts), 1):
        response = llm.invoke([
            SystemMessage(content=SUMMARIZE_SYSTEM),
            HumanMessage(content=f"Sub-question: {query}\n\nRetrieved context:\n{context}"),
        ])
        summary = response.content.strip()

        # ── Sanity check 3 ───────────────────────────────────────────────────
        assert summary, f"Summariser produced empty output for sub-query {i}"
        print(f"  Sub-query {i} summary preview: {summary[:120]}...")
        sub_query_summaries.append(summary)

    return {"sub_query_summaries": sub_query_summaries}


# ── Node 4: Final Answer Generation ──────────────────────────────────────────

# GENERATE_SYSTEM = """You are a senior healthcare AI analyst synthesising research evidence to answer complex questions.

# You will receive:
# - The original complex question
# - A numbered list of sub-questions that decompose it
# - A bullet-point evidence summary for each sub-question, drawn from peer-reviewed articles

# Your task: Synthesise the evidence across ALL sub-questions into a single, comprehensive answer to
# the original question.

# Guidelines:
# - Cite article numbers when drawing on specific evidence (e.g. "According to Article 3...").
# - Quote directly from the evidence where it strengthens the argument.
# - Show explicitly how the sub-answers connect — do not treat them as isolated facts.
# - If evidence is insufficient for any aspect of the question, note this gap clearly.
# - Be analytical, not merely descriptive: explain how the pieces fit together to answer the question.
# """

GENERATE_SYSTEM = """
You are a healthcare AI assistant tasked with creating clear, accessible summaries of medical research.
You will receive:
- The original complex question
- A numbered list of sub-questions that decompose it
- A bullet-point evidence summary for each sub-question, drawn from peer-reviewed articles (each with an article identifier)

Your task: Synthesize the evidence across all sub-questions into a single, simple, and easy-to-understand summary that answers the original question.

Guidelines:
- Combine the information into a unified overview. Do not simply list facts or answer the sub-questions one by one.
- If evidence is insufficient for any aspect of the original question, briefly mention this gap.
- Do NOT use conversational in-text citations (e.g., avoid "According to Article 3...").

Formatting Requirement:
To allow for programmatic parsing of the sources you relied on, you MUST structure your response into two distinct sections. The final section must be a strictly formatted JSON block containing the identifiers of all articles used to inform your summary. 

Use this exact structure:

### Summary
[Your summary here]

### Citations
```json
{
  "article_ids": [1, 2, 5]
}
"""

def generate_node(state: AgentState) -> dict:
    """Agent 4 – Generator. Synthesises sub-query summaries into a final, cited answer."""
    print("\n[4/4] Generating final answer...")
    question            = state["question"]
    sub_queries         = state["sub_queries"]
    sub_query_summaries = state["sub_query_summaries"]

    evidence_block = "\n\n".join(
        f"Sub-question {i}: {q}\nEvidence:\n{s}"
        for i, (q, s) in enumerate(zip(sub_queries, sub_query_summaries), 1)
    )

    response = llm.invoke([
        SystemMessage(content=GENERATE_SYSTEM),
        HumanMessage(content=f"Original question: {question}\n\n{evidence_block}"),
    ])
    answer = response.content.strip()

    # ── Sanity check 4 ───────────────────────────────────────────────────────
    assert answer, "Generator produced an empty answer!"

    return {"answer": answer}


# ── Build the graph ───────────────────────────────────────────────────────────

print("Building Multi-Agent Graph...")
workflow = StateGraph(AgentState)

workflow.add_node("decompose", decompose_node)
workflow.add_node("retrieve",  retrieve_node)
workflow.add_node("summarize", summarize_node)
workflow.add_node("generate",  generate_node)

workflow.add_edge(START,       "decompose")
workflow.add_edge("decompose", "retrieve")
workflow.add_edge("retrieve",  "summarize")
workflow.add_edge("summarize", "generate")
workflow.add_edge("generate",  END)

app = workflow.compile()


# ── Sanity-check runner ───────────────────────────────────────────────────────

def run_sanity_checks():
    """Run a battery of pipeline sanity checks covering both simple and multi-hop queries."""
    print("\n" + "=" * 60)
    print("RUNNING PIPELINE SANITY CHECKS")
    print("=" * 60)

    tests = [
        {
            "name": "Simple single-hop question",
            "question": "What is the EU AI Act?",
        },
        {
            "name": "Multi-hop question (decomposition required)",
            "question": (
                "Two frameworks for governing post-deployment AI in healthcare propose different "
                "monitoring mechanisms. One focuses on operationalised clinic-level audit steps; "
                "the other calls for adaptive regulatory oversight replacing static approval. "
                "What does the EU AI Act add that neither framework alone provides?"
            ),
        },
        {
            "name": "Comparative question across multiple concepts",
            "question": (
                "How do bias mitigation strategies differ between pre-deployment training-time "
                "interventions and post-deployment monitoring in clinical AI systems?"
            ),
        },
    ]

    passed, failed = 0, 0
    for test in tests:
        print(f"\n[TEST] {test['name']}")
        print(f"  Q: {test['question'][:80]}...")
        try:
            result = app.invoke({"question": test["question"]})

            assert result.get("sub_queries"),         "sub_queries is empty"
            assert result.get("sub_query_contexts"),  "sub_query_contexts is empty"
            assert result.get("sub_query_summaries"), "sub_query_summaries is empty"
            assert result.get("answer"),              "answer is empty"
            assert len(result["sub_queries"]) == len(result["sub_query_summaries"]), \
                "sub_queries / sub_query_summaries length mismatch"

            print(
                f"  PASS  — {len(result['sub_queries'])} sub-queries, "
                f"answer length {len(result['answer'])} chars"
            )
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  — {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR — {type(e).__name__}: {e}")
            failed += 1

    print("\n" + "=" * 60)
    print(f"SANITY CHECKS COMPLETE  {passed} passed, {failed} failed")
    print("=" * 60)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if "--sanity" in sys.argv:
        run_sanity_checks()
    else:
        test_question = (
            "Two frameworks for governing post-deployment AI in healthcare propose different "
            "monitoring mechanisms. One focuses on operationalised clinic-level audit steps; "
            "the other calls for adaptive regulatory oversight replacing static approval. "
            "What does the EU AI Act add that neither framework alone provides?"
        )
        print(f"\nUser: {test_question}\n")
        result = app.invoke({"question": test_question})

        print("\n" + "=" * 60)
        print("PIPELINE TRACE")
        print("=" * 60)
        print(f"\nSub-queries decomposed ({len(result['sub_queries'])}):")
        for i, q in enumerate(result["sub_queries"], 1):
            print(f"  {i}. {q}")

        print("\n" + "=" * 60)
        print("FINAL ANSWER")
        print("=" * 60)
        print(result["answer"])
