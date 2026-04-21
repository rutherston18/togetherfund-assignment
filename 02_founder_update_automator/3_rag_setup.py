import os
import chromadb
import ollama
from config import MODEL_EMBED, INBOX_DIR, CHROMA_DIR

def build_vector_db():
    print(f"Initializing ChromaDB at {CHROMA_DIR}...")
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    
    # Get or create a collection
    collection = client.get_or_create_collection(name="founder_updates")
    
    files = [f for f in os.listdir(INBOX_DIR) if f.endswith('.txt')]
    print(f"Embedding {len(files)} files using {MODEL_EMBED}...")

    # We process in small batches to respect the 6GB VRAM limits
    for i, filename in enumerate(files):
        # Check if document already exists in Chroma
        existing = collection.get(ids=[filename])
        if existing['ids']:
            continue
            
        filepath = os.path.join(INBOX_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        try:
            # Generate embedding
            response = ollama.embeddings(model=MODEL_EMBED, prompt=text)
            embedding = response["embedding"]
            
            # Add to ChromaDB
            collection.add(
                ids=[filename],
                embeddings=[embedding],
                documents=[text],
                metadatas=[{"source": filename}]
            )
            print(f"Embedded [{i+1}/{len(files)}]: {filename}")
        except Exception as e:
            print(f"Error embedding {filename}: {e}")

if __name__ == "__main__":
    build_vector_db()