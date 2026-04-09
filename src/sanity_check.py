from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


CHROMA_PATH = "./chroma_db"

def test_database():
    # use same embedding model here
    print("Loading embedding model...")
    # embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-large-en-v1.5",
    encode_kwargs={"normalize_embeddings": True},
    )

    print("Connecting to ChromaDB...\n")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)

    query = "Imaging AI has high deployment rates across US health systems but only 19% of deployers report high success. Using what you know about FDA validation gaps and algorithmic bias literature, construct the most likely causal mechanism for this divergence" 

    # k --> number of chunks to return
    results = db.similarity_search_with_score(query, k=3)

    if not results:
        print("No results found. The database might be empty.")
        return

    print(f"==================================================")
    print(f" QUERY: '{query}'")
    print(f"==================================================\n")

    for i, (doc, score) in enumerate(results):
        # chroma uses L2 distance
        print(f"--- MATCH {i+1} (Score: {score:.4f}) ---")
        print(f"Source: {doc.metadata.get('source', 'Unknown File')}")
        print(f"Text: {doc.page_content[:500]}...\n")


test_database()