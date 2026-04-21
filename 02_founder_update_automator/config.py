import os

# --- MODEL CONFIGURATION ---
# You can change these strings to any model you have pulled via 'ollama pull <model>'
MODEL_GENERATE = "llama3"       # Good for creative, messy text generation
MODEL_EXTRACT = "phi3"          # Fast and strict for JSON extraction
MODEL_EMBED = "nomic-embed-text" # Standard for local RAG embeddings

# --- DIRECTORIES ---
INBOX_DIR = "./data/inbox"
CHROMA_DIR = "./chroma_db"
DB_PATH = "portfolio.db"

# Ensure directories exist
os.makedirs(INBOX_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)