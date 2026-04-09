import json
import os
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI # Replaced Groq with Google
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

# Set your Google AI Studio API Key here
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

CHROMA_PATH = "./chroma_db"
METADATA_PATH = "data/metadata.json"

# Build a lookup from filename → article metadata, loaded once at startup
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

# Initialize the Google Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-pro", # You can also use "gemini-1.5-flash" for a faster, lighter option
    temperature=0.2,      # Low for RAG tasks
    max_output_tokens=4096 # Note: Langchain Google GenAI uses 'max_output_tokens' instead of 'max_tokens'
)

class AgentState(TypedDict):
    question: str
    context: str
    answer: str

def retrieve_node(state: AgentState):
    """Agent 1: The Researcher. Finds context from the Vector DB."""
    print("-> [Agent] Retrieving context...")
    question = state["question"]

    docs = db.similarity_search(question, k=3)

    context_blocks = []
    for doc in docs:
        source_file = doc.metadata.get("source", "")
        meta = ARTICLE_METADATA.get(source_file, {})

        # Build a rich source header so the LLM always knows where each chunk came from
        article_num  = meta.get("article_number", "?")
        title        = meta.get("title", "Unknown title")
        publication  = meta.get("publication", "Unknown publication")
        date         = meta.get("date", "Unknown date")
        cluster      = meta.get("cluster", "")
        url          = meta.get("url", "")

        header = (
            f"[Article {article_num} | {title} | {publication} | {date}"
            + (f" | Cluster: {cluster}" if cluster else "")
            + (f" | URL: {url}" if url else "")
            + "]"
        )
        context_blocks.append(f"{header}\n{doc.page_content}")

    context = "\n\n---\n\n".join(context_blocks)
    return {"context": context}

def generate_node(state: AgentState):
    """Agent 2: The Writer. Drafts the answer based ONLY on the context."""
    print("-> [Agent] Generating answer...")
    question = state["question"]
    context = state["context"]
    
    template = """You are a helpful assistant specializing in healthcare AI. \
Use ONLY the retrieved context below to answer the question.
If the answer is not in the context, say you don't know.

Each context block starts with a header like:
[Article N | Title | Publication | Date | Cluster: ... | URL: ...]

Context:
{context}

Question: {question}

In your answer:
- Cite the article number(s) you draw from (e.g. "According to Article 3...").
- Quote directly from the context where relevant.
- If multiple articles contribute, note what each one adds.
"""
    prompt = ChatPromptTemplate.from_template(template)
    
    # chaining prompt and llm together
    chain = prompt | llm
    
    # Generate the response
    response = chain.invoke({"context": context, "question": question})
    
    return {"answer": response.content}

# building the workflow graph
print("Building Agent Graph...")
workflow = StateGraph(AgentState)

# Add our nodes
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)

# Define the flow: START -> Retrieve -> Generate -> END
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()

# testing the agent with a sample question
if __name__ == "__main__":
    test_question = "Two frameworks for governing post-deployment AI in healthcare propose different monitoring mechanisms. One focuses on operationalised clinic-level audit steps; the other calls for adaptive regulatory oversight replacing static approval. What does the EU AI Act add that neither framework alone provides?"
    print(f"\nUser: {test_question}\n")
    
    # Run the graph
    initial_state = {"question": test_question}
    result = app.invoke(initial_state)
    
    print("\n==================================")
    print("Final Answer:")
    print("==================================")
    print(result["answer"])