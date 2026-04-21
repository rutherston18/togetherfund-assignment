import sqlite3
import ollama
import os
import json
import re
from config import MODEL_EXTRACT, INBOX_DIR, DB_PATH

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolio_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            startup_name TEXT,
            mrr TEXT,
            runway_months TEXT,
            key_challenge TEXT,
            raw_text TEXT
        )
    ''')
    conn.commit()
    return conn

def extract_json_from_text(text):
    """Utility to clean up LLM output if it wraps JSON in markdown blocks."""
    match = re.search(r'```json\n(.*?)\n```', text, re.DOTALL)
    if match:
        return match.group(1)
    return text

def process_inbox():
    conn = setup_database()
    cursor = conn.cursor()
    
    files = [f for f in os.listdir(INBOX_DIR) if f.endswith('.txt')]
    print(f"Found {len(files)} emails to process using {MODEL_EXTRACT}...")
    
    schema_instructions = """
    Extract the following information from the provided email text and output strictly valid JSON.
    If a metric is not mentioned, use "Unknown".
    {
        "startup_name": "Name of the startup",
        "mrr": "Monthly Recurring Revenue mentioned (e.g. $10k)",
        "runway_months": "Runway left in months (e.g. 6)",
        "key_challenge": "A brief 5-word summary of their main problem"
    }
    """

    for filename in files:
        # Check if already processed
        cursor.execute("SELECT 1 FROM portfolio_metrics WHERE filename=?", (filename,))
        if cursor.fetchone():
            continue

        filepath = os.path.join(INBOX_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_text = f.read()

        try:
            response = ollama.chat(
                model=MODEL_EXTRACT,
                messages=[
                    {'role': 'system', 'content': schema_instructions},
                    {'role': 'user', 'content': f"Email text:\n{raw_text}"}
                ],
                format='json'
            )
            
            raw_json_str = extract_json_from_text(response['message']['content'])
            data = json.loads(raw_json_str)
            
            cursor.execute('''
                INSERT INTO portfolio_metrics (filename, startup_name, mrr, runway_months, key_challenge, raw_text)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (filename, data.get('startup_name', 'Unknown'), str(data.get('mrr', 'Unknown')), 
                  str(data.get('runway_months', 'Unknown')), data.get('key_challenge', 'Unknown'), raw_text))
            conn.commit()
            print(f"Extracted: {filename} -> {data.get('startup_name')}")
            
        except json.JSONDecodeError:
            print(f"Failed to parse JSON for {filename}. Skipping.")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    conn.close()

if __name__ == "__main__":
    process_inbox()

    