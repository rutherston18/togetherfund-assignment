# Healthcare AI Research Assistant

A **multi-agent RAG** (retrieval-augmented generation) app that answers questions over a curated corpus of healthcare AI articles. The backend is a [LangGraph](https://github.com/langchain-ai/langgraph) pipeline (query decomposition → retrieval → per-query summarisation → final synthesis); the UI is [Streamlit](https://streamlit.io/) with chain-of-thought visibility and source citations.

## Features

- **Four-stage pipeline**: decompose the user question, retrieve chunks from a vector store, summarise evidence per sub-query, then synthesise an answer with structured citations.
- **21 articles** with metadata (title, URL, publication, date, thematic cluster) in `data/metadata.json`; cleaned markdown bodies live under `data/cleaned_articles/`.
- **Follow-up context**: recent Q&A turns are injected so questions like “tell me more about that” still make sense.
- **Vector backends**: [Qdrant](https://qdrant.tech/) (default, local `qdrant_db/`) or [Chroma](https://www.trychroma.com/) (`chroma_db/`), selected via `VECTOR_DB_TYPE`.

## Requirements

- **Python 3.11+** (matches the devcontainer image).
- **Google Gemini API key** for `ChatGoogleGenerativeAI` (`gemini-2.5-pro` in code).
- **Disk / RAM**: the embedding model `abhinand/MedEmbed-large-v0.1` is downloaded on first use via Hugging Face; allow several GB for model weights and the vector index.

Optional: **NVIDIA GPU** — `src/build_database_qdrant.py` sets `device="cuda"` for embedding; CPU works but is slower.

## Setup

1. **Clone and enter the project root** (the directory that contains `app.py`).

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   pip install langchain-qdrant
   ```

   `langchain-qdrant` is required because `src/agent.py` imports it for the default Qdrant store; it is not yet pinned in `requirements.txt`.

4. **Configure the Gemini API key** using either:

   - **`.env`** in the project root (loaded by `python-dotenv`):

     ```env
     GEMINI_API_KEY=your_key_here
     ```

   - **Streamlit secrets** when deploying or running in an environment that provides them: create `.streamlit/secrets.toml` with `GEMINI_API_KEY = "your_key_here"`. The agent prefers `st.secrets` when Streamlit is available and falls back to the environment variable.

5. **Vector database**: The repository may already include a populated `qdrant_db/`. If you need to rebuild the index from `data/cleaned_articles/`:

   ```bash
   # Qdrant (default; uses GPU in the script if CUDA is available)
   python src/build_database_qdrant.py

   # Chroma
   python src/build_database.py
   ```

   Then set `VECTOR_DB_TYPE` to `qdrant` or `chroma` to match what you built.

## Run the app

From the **project root**:

```bash
streamlit run app.py
```

Open the URL Streamlit prints (by default `http://localhost:8501`).

### Dev container

A [Dev Container](https://containers.dev/) configuration is under `.devcontainer/`. It installs dependencies, forwards port **8501**, and can run Streamlit on attach. For cloud or strict proxies you may need flags such as `--server.enableCORS false` (as in `devcontainer.json`).

## Project layout

| Path | Role |
|------|------|
| `app.py` | Streamlit chat UI, citation parsing, session state |
| `src/agent.py` | LangGraph graph, embeddings, vector store, LLM |
| `src/build_database.py` / `src/build_database_qdrant.py` | Chunk articles and build Chroma / Qdrant indexes |
| `src/scrape*.py`, `src/clean_articles.py` | Earlier pipeline for fetching and normalising articles |
| `data/cleaned_articles/` | Markdown source for indexing |
| `data/metadata.json` | Per-article metadata and cluster labels |
| `qdrant_db/`, `chroma_db/` | Persistent vector stores (when built or committed) |

## Environment variables

| Variable | Purpose |
|----------|---------|
| `GEMINI_API_KEY` | Google Gemini API key (or use Streamlit secrets) |
| `VECTOR_DB_TYPE` | `qdrant` (default) or `chroma` |
| `GOOGLE_API_KEY` | Set automatically from the above in normal use |
