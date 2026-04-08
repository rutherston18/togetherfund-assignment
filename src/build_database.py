import os
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
MARKDOWN_FOLDER = "data/markdown_articles"
CHROMA_PATH = "./chroma_db"

def load_documents_from_folder(folder_path):
    """Reads all markdown files from the folder and converts them to LangChain Documents."""
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                text = file.read()
                # Store the filename in metadata so we know where the info came from
                doc = Document(page_content=text, metadata={"source": filename})
                documents.append(doc)
    
    print(f"Loaded {len(documents)} articles.")
    return documents

def build_vector_database():
    # 1. Load the raw markdown text
    docs = load_documents_from_folder(MARKDOWN_FOLDER)
    if not docs:
        print("No markdown files found. Check your folder path!")
        return

    # 2. Chunk the text
    # RecursiveCharacterTextSplitter tries to split by paragraphs first, then sentences, then words.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,       # Number of characters per chunk
        chunk_overlap=100,    # Overlap to prevent cutting a thought in half
        length_function=len,
        separators=["\n\n", "\n", " ", ""] # Prioritize splitting at paragraphs
    )
    
    print("Chunking documents...")
    chunks = text_splitter.split_documents(docs)
    print(f"Split articles into {len(chunks)} total chunks.")

    # 3. Initialize the Embedding Model
    # This downloads a small, fast, free model from HuggingFace
    print("Loading embedding model...")
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Create and save the Chroma Vector Database
    print("Generating embeddings and saving to ChromaDB...")
    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embedding_model, 
        persist_directory=CHROMA_PATH
    )
    
    print(f"Database successfully built and saved to {CHROMA_PATH}!")

# Run the process
build_vector_database()