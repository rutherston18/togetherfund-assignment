import sqlite3
import ollama
import chromadb
from config import MODEL_GENERATE, CHROMA_DIR, DB_PATH
import subprocess

def run_script(script_name):
    print(f"\n--- Running {script_name} ---")
    subprocess.run(["python", script_name])
    print(f"--- Finished {script_name} ---\n")

def chat_interface():
    print("\n--- Portfolio RAG Chat (Type 'exit' to quit) ---")
    
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_or_create_collection(name="founder_updates")
    
    while True:
        query = input("\nInvestor Query: ")
        if query.lower() in ['exit', 'quit']:
            break
            
        print("Searching database...")
        # 1. Embed the query
        query_embed = ollama.embeddings(model="nomic-embed-text", prompt=query)["embedding"]
        
        # 2. Retrieve top 3 documents
        results = collection.query(query_embeddings=[query_embed], n_results=3)
        
        if not results['documents'][0]:
            print("No relevant documents found.")
            continue
            
        context_chunks = "\n\n---\n\n".join(results['documents'][0])
        
        # 3. Generate answer using RAG
        prompt = f"""
        You are an AI assistant for a Venture Capital firm.
        Use ONLY the following context from founder update emails to answer the user's question.
        If the answer is not in the context, say "I cannot find this in the recent updates."
        
        Context:
        {context_chunks}
        
        Question: {query}
        """
        
        print(f"Generating answer using {MODEL_GENERATE}...")
        response = ollama.chat(model=MODEL_GENERATE, messages=[{'role': 'user', 'content': prompt}])
        
        print("\n🤖 AI Response:")
        print(response['message']['content'])
        
        # Print sources
        print("\nSources retrieved:", results['ids'][0])

def view_sql_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT startup_name, mrr, runway_months, key_challenge FROM portfolio_metrics LIMIT 5")
        rows = cursor.fetchall()
        print("\n--- Sample Structured Data (SQLite) ---")
        print(f"{'Startup':<15} | {'MRR':<10} | {'Runway':<8} | {'Challenge'}")
        print("-" * 60)
        for row in rows:
            print(f"{str(row[0])[:14]:<15} | {str(row[1])[:10]:<10} | {str(row[2])[:8]:<8} | {str(row[3])[:20]}")
    except sqlite3.OperationalError:
        print("Database not found or empty. Run the extraction pipeline first.")
    finally:
        conn.close()

if __name__ == "__main__":
    while True:
        print("\n=== VC Portfolio OS Backend ===")
        print("1. Generate Synthetic Emails (1_generate_data.py)")
        print("2. Run Extraction Pipeline (2_ingest_extract.py)")
        print("3. Run Vector Embedding (3_rag_setup.py)")
        print("4. View Structured SQL Data")
        print("5. Start RAG Chat Interface")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1': run_script("1_generate_data.py")
        elif choice == '2': run_script("2_ingest_extract.py")
        elif choice == '3': run_script("3_rag_setup.py")
        elif choice == '4': view_sql_data()
        elif choice == '5': chat_interface()
        elif choice == '6': break
        else: print("Invalid choice.")