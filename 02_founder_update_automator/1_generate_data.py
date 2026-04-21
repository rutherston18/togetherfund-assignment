import ollama
import random
import os
from config import MODEL_GENERATE, INBOX_DIR

STARTUPS = [
    ("NeuralCast", "AI/ML"), ("EcoFlow", "ClimateTech"), ("Vaulted", "FinTech"), 
    ("HealthSync", "HealthTech"), ("OrbitLogistics", "Supply Chain"), 
    ("ByteForge", "DevTools"), ("AgriSense", "AgriTech"), ("BlockTrust", "Web3")
]

MOODS = ["optimistic but stressed", "panicking about runway", "neutral and highly quantitative", "celebratory but facing technical debt"]

def generate_emails(num_emails=100):
    print(f"Generating {num_emails} simulated emails using {MODEL_GENERATE}...")
    
    for i in range(1, num_emails + 1):
        startup, sector = random.choice(STARTUPS)
        mood = random.choice(MOODS)
        
        prompt = f"""
        Write a messy, realistic email update from the founder of '{startup}' (a {sector} startup) to their investor. 
        The founder's mood is: {mood}. 
        Include some quantitative data (like MRR, runway, or user count) hidden in the text. 
        Mention at least one current blocker or challenge. 
        Do not use formal formatting, make it look like a hastily written email. Max 150 words.
        """
        
        try:
            response = ollama.chat(model=MODEL_GENERATE, messages=[{'role': 'user', 'content': prompt}])
            email_content = response['message']['content']
            
            # Save to file
            filename = f"email_{i:03d}_{startup.lower()}.txt"
            filepath = os.path.join(INBOX_DIR, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"From: founder@{startup.lower()}.com\n")
                f.write(f"Startup: {startup}\n")
                f.write(f"Sector: {sector}\n")
                f.write("-" * 40 + "\n")
                f.write(email_content)
                
            print(f"[{i}/{num_emails}] Generated {filename}")
            
        except Exception as e:
            print(f"Error generating email {i}: {e}")

if __name__ == "__main__":
    generate_emails(100)