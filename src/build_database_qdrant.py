import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Swap Chroma for LangChain's Qdrant vector store
from langchain_qdrant import QdrantVectorStore

MARKDOWN_FOLDER = "data/cleaned_articles"
# 2. Define a local folder for Qdrant storage
QDRANT_PATH = "./qdrant_db"

def load_documents_from_folder(folder_path):
    """Reads all markdown files from the folder and converts them to LangChain Documents."""
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                text = file.read()
                # store the article number so we can map it to metadata.json
                doc = Document(page_content=text, metadata={"source": filename})
                documents.append(doc)
    
    print(f"Loaded {len(documents)} articles.")
    return documents

def build_vector_database():
    docs = load_documents_from_folder(MARKDOWN_FOLDER)
    if not docs:
        print("No markdown files found. Check your folder path!")
        return
    
    # RecursiveCharacterTextSplitter tries to split by paragraphs first, then sentences, then words.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,       
        chunk_overlap=200,    
        length_function=len,
        separators=["\n\n", "\n", " ", ""] # Prioritize splitting at paragraphs
    )
    
    print("Chunking documents...")
    chunks = text_splitter.split_documents(docs)
    print(f"Split articles into {len(chunks)} total chunks.")

    print("Loading embedding model...")
    embedding_model = HuggingFaceEmbeddings(
        model_name="abhinand/MedEmbed-large-v0.1",
        encode_kwargs={"normalize_embeddings": True},
        # Adding device="cuda" ensures it leverages your RTX 4050
        model_kwargs={"device": "cuda"} 
    )

    # 3. Save to Qdrant Vector Database
    print("Generating embeddings and saving to Qdrant...")
    
    # Qdrant requires a collection name. It creates the folder and DB automatically.
    db = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embedding_model,
        path=QDRANT_PATH, 
        collection_name="healthcare_docs" 
    )
    
    print(f"Database successfully built and saved to {QDRANT_PATH}!")

build_vector_database()