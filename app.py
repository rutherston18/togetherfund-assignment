"""
app.py — Streamlit chat interface for the Healthcare AI Research Assistant.

Run from the project root:
    streamlit run app.py
"""

import re
import sys
import json
from pathlib import Path

import streamlit as st

# ── Path setup ─────────────────────────────────────────────────────────────────
# Ensure `from src.agent import ...` resolves when running from the project root.
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# ── Page config (must come before any other Streamlit calls) ───────────────────
st.set_page_config(
    page_title="Healthcare AI Research Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ── Lazy-load the agent (cached so the heavy init only runs once per session) ──
@st.cache_resource(show_spinner="Initialising pipeline (loading embedding model and vector DB)…")
def load_agent():
    from src.agent import app as agent_graph, ARTICLE_METADATA  # noqa: PLC0415
    return agent_graph, ARTICLE_METADATA


agent_graph, ARTICLE_METADATA = load_agent()


# ── Helpers ────────────────────────────────────────────────────────────────────

def parse_answer(raw: str) -> tuple[str, list[int]]:
    """Split the LLM output into (summary_text, article_ids).

    The agent is instructed to produce:
        ### Summary
        …text…
        ### Citations
        ```json
        {"article_ids": [1, 2, 5]}
        ```
    """
    summary_match = re.search(
        r"###\s*Summary\s*(.*?)(?=###\s*Citations|$)", raw, re.DOTALL | re.IGNORECASE
    )
    citations_match = re.search(
        r"###\s*Citations\s*```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL | re.IGNORECASE
    )

    summary = summary_match.group(1).strip() if summary_match else raw.strip()

    article_ids: list[int] = []
    if citations_match:
        try:
            data = json.loads(citations_match.group(1))
            article_ids = [int(i) for i in data.get("article_ids", [])]
        except (json.JSONDecodeError, ValueError):
            pass

    return summary, article_ids


def extract_ids_from_contexts(contexts: list[str]) -> list[int]:
    """Return all unique article numbers that appear in the retrieved context blocks.

    Every chunk the retriever pulled has a header like:
        [Article 3 | Title | Publication | ...]
    These are the articles that actually informed the evidence summaries, so they
    all deserve a citation regardless of what the LLM remembered to list.
    """
    ids: list[int] = []
    for ctx in contexts:
        for num in re.findall(r"\[Article (\d+) \|", ctx):
            n = int(num)
            if n not in ids:
                ids.append(n)
    return ids


def get_article_meta(article_id: int) -> dict:
    """Return metadata dict for the given article_number integer."""
    for meta in ARTICLE_METADATA.values():
        if meta.get("article_number") == article_id:
            return meta
    return {}


def build_contextualized_question(question: str, history: list[dict]) -> str:
    """Inject the last few Q&A turns into the question so the agent can
    resolve follow-up references such as 'tell me more about that'.
    """
    if not history:
        return question

    tail = history[-3:]  # Cap at 3 exchanges to keep tokens manageable
    lines = ["[Prior conversation — use only to resolve follow-up references]"]
    for idx, turn in enumerate(tail, 1):
        lines.append(f"Q{idx}: {turn['question']}")
        preview = turn["answer"][:400] + ("…" if len(turn["answer"]) > 400 else "")
        lines.append(f"A{idx}: {preview}")
    lines.append("")
    lines.append(f"[New question]: {question}")
    return "\n".join(lines)


def render_cot(cot: dict) -> None:
    """Render the full chain-of-thought breakdown (called inside an expander)."""
    sub_queries: list[str] = cot.get("sub_queries", [])
    sub_query_contexts: list[str] = cot.get("sub_query_contexts", [])
    sub_query_summaries: list[str] = cot.get("sub_query_summaries", [])

    # ── Step 1 ────────────────────────────────────────────────────────────────
    st.markdown("#### Step 1 — Query Decomposition")
    if sub_queries:
        for i, q in enumerate(sub_queries, 1):
            st.markdown(f"**{i}.** {q}")
    else:
        st.caption("No sub-queries recorded.")

    st.divider()

    # ── Step 2 ────────────────────────────────────────────────────────────────
    st.markdown("#### Step 2 — Document Retrieval")
    if sub_query_contexts:
        for i, ctx in enumerate(sub_query_contexts, 1):
            nums = list(dict.fromkeys(re.findall(r"\[Article (\d+) \|", ctx)))
            if nums:
                badges = " ".join(f"`#{n}`" for n in nums)
                st.markdown(f"**Sub-query {i}** — retrieved articles: {badges}")
            else:
                st.markdown(f"**Sub-query {i}** — documents retrieved")
    else:
        st.caption("No retrieval data recorded.")

    st.divider()

    # ── Step 3 ────────────────────────────────────────────────────────────────
    st.markdown("#### Step 3 — Evidence Summaries")
    if sub_queries and sub_query_summaries:
        for i, (sq, sm) in enumerate(zip(sub_queries, sub_query_summaries), 1):
            st.markdown(f"**Sub-query {i}:** {sq}")
            st.markdown(sm)
            if i < len(sub_queries):
                st.markdown("---")
    else:
        st.caption("No evidence summaries recorded.")


def render_citations(article_ids: list[int]) -> None:
    """Render a formatted sources section below the answer."""
    if not article_ids:
        return

    st.divider()
    st.markdown("**Sources**")
    for aid in sorted(set(article_ids)):
        meta = get_article_meta(aid)
        if meta:
            title = meta.get("title", f"Article {aid}")
            pub = meta.get("publication", "")
            date = meta.get("date", "")
            url = meta.get("url", "")
            cluster = meta.get("cluster", "")
            cluster_badge = f" `{cluster}`" if cluster else ""
            pub_info = f" — {pub}, {date}" if pub else ""
            title_link = f"[{title}]({url})" if url else title
            st.markdown(f"**[{aid}]** {title_link}{pub_info}{cluster_badge}")
        else:
            st.markdown(f"**[{aid}]** Article {aid}")


# ── Sidebar ────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("About")
    st.markdown(
        "A **multi-agent RAG pipeline** over 21 curated healthcare AI articles.\n\n"
        "**Pipeline stages:**\n"
        "1. Query decomposition\n"
        "2. Vector similarity retrieval\n"
        "3. Evidence summarisation\n"
        "4. Answer synthesis with citations\n"
    )

    st.divider()
    st.markdown("**Article clusters:**")
    clusters = sorted(
        {m.get("cluster", "") for m in ARTICLE_METADATA.values() if m.get("cluster")}
    )
    for cluster in clusters:
        count = sum(1 for m in ARTICLE_METADATA.values() if m.get("cluster") == cluster)
        st.markdown(f"- {cluster} ({count} articles)")

    st.divider()
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()


# ── Session state ──────────────────────────────────────────────────────────────

if "messages" not in st.session_state:
    # Each entry: {role, content, summary?, article_ids?, cot_data?}
    st.session_state.messages = []

if "history" not in st.session_state:
    # Compact Q&A pairs used to inject follow-up context into the agent
    st.session_state.history = []


# ── Main layout ────────────────────────────────────────────────────────────────

st.title("Healthcare AI Research Assistant")
st.caption(
    "Ask complex questions about healthcare AI. "
    "Every response shows chain-of-thought reasoning and cites its sources."
)

# Re-render all prior messages on page reload / rerun
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.write(msg["content"])
        else:
            st.markdown(msg.get("summary", msg["content"]))
            cot = msg.get("cot_data")
            if cot:
                with st.expander("Chain of Thought", expanded=False):
                    render_cot(cot)
            render_citations(msg.get("article_ids", []))


# ── Chat input ─────────────────────────────────────────────────────────────────

if prompt := st.chat_input("Ask a question about healthcare AI…"):

    # Show the user's message immediately
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Embed conversation history so the agent can resolve follow-up references
    agent_question = build_contextualized_question(prompt, st.session_state.history)

    with st.chat_message("assistant"):

        sub_queries: list[str] = []
        sub_query_contexts: list[str] = []
        sub_query_summaries: list[str] = []
        raw_answer = ""

        try:
            # ── Live chain-of-thought via st.status ───────────────────────────
            with st.status("Running multi-agent pipeline…", expanded=True) as status:

                st.write("**[1/4]** Decomposing query into focused sub-questions…")

                for update in agent_graph.stream({"question": agent_question}):
                    for node_name, node_output in update.items():

                        if node_name == "decompose":
                            sub_queries = node_output.get("sub_queries", [])
                            sq_text = "\n".join(
                                f"  {i}. {q}" for i, q in enumerate(sub_queries, 1)
                            )
                            st.write(
                                f"**[1/4]** Decomposed into **{len(sub_queries)}** "
                                f"sub-question(s):\n{sq_text}"
                            )
                            st.write("**[2/4]** Retrieving documents from the vector store…")

                        elif node_name == "retrieve":
                            sub_query_contexts = node_output.get("sub_query_contexts", [])
                            retrieval_lines = []
                            for i, ctx in enumerate(sub_query_contexts, 1):
                                nums = list(dict.fromkeys(re.findall(r"\[Article (\d+) \|", ctx)))
                                badges = ", ".join(f"#{n}" for n in nums) if nums else "docs"
                                retrieval_lines.append(f"  Sub-query {i}: articles {badges}")
                            st.write(
                                "**[2/4]** Documents retrieved:\n" + "\n".join(retrieval_lines)
                            )
                            st.write("**[3/4]** Summarising evidence per sub-question…")

                        elif node_name == "summarize":
                            sub_query_summaries = node_output.get("sub_query_summaries", [])
                            st.write(
                                f"**[3/4]** Evidence summarised for "
                                f"**{len(sub_query_summaries)}** sub-question(s)."
                            )
                            st.write("**[4/4]** Synthesising final answer…")

                        elif node_name == "generate":
                            raw_answer = node_output.get("answer", "")
                            st.write("**[4/4]** Answer generated.")

                status.update(label="Pipeline complete", state="complete", expanded=False)

            # ── Final answer ──────────────────────────────────────────────────
            summary, llm_ids = parse_answer(raw_answer)

            # Merge LLM-reported IDs with every article that was actually retrieved.
            # The LLM sometimes omits articles it used, so the retrieval contexts
            # are the authoritative source of what informed the answer.
            retrieved_ids = extract_ids_from_contexts(sub_query_contexts)
            article_ids = sorted(set(llm_ids) | set(retrieved_ids))

            st.markdown(summary)

            # ── Persistent chain-of-thought expander ──────────────────────────
            cot_data = {
                "sub_queries": sub_queries,
                "sub_query_contexts": sub_query_contexts,
                "sub_query_summaries": sub_query_summaries,
            }
            with st.expander("Chain of Thought", expanded=False):
                render_cot(cot_data)

            render_citations(article_ids)

            # ── Persist to session state ───────────────────────────────────────
            st.session_state.messages.append({
                "role": "assistant",
                "content": raw_answer,
                "summary": summary,
                "article_ids": article_ids,
                "cot_data": cot_data,
            })
            st.session_state.history.append({
                "question": prompt,
                "answer": summary,
            })

        except Exception as exc:
            st.error(f"Pipeline error — {type(exc).__name__}: {exc}")
