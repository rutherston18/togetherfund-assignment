import requests
import os
import time

def scrape_and_save_jina(url, filepath):
    jina_url = f"https://r.jina.ai/{url}"
    
    try:
        response = requests.get(jina_url, timeout=15)
        
        if response.status_code == 200:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f" [SUCCESS] Saved to {filepath}")
        else:
            print(f" [FAILED] Status {response.status_code} for URL: {url}")
            
    except requests.exceptions.RequestException as e:
        print(f" [ERROR] Connection failed for {url}: {e}")

def batch_process_urls(txt_file_path, save_directory):
    """Reads a text file of URLs and processes them one by one."""
    
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        print(f"Created directory: {save_directory}")

    try:
        with open(txt_file_path, "r", encoding="utf-8") as file:
            # .readlines() grabs every line, .strip() removes the invisible \n characters
            urls = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find the file '{txt_file_path}'")
        return

    print(f"Found {len(urls)} URLs to process.\n" + "-"*30)

    for index, url in enumerate(urls):

        filename = f"article_{index + 1}.md"
        

        filepath = os.path.join(save_directory, filename)
        
        print(f"Processing ({index + 1}/{len(urls)}): {url}")
        scrape_and_save_jina(url, filepath)
        
        time.sleep(1) 

    print("-" * 30 + "\nAll done!")


TXT_FILE = "./data/corpuslinks.txt"          
SAVE_FOLDER = "./data/markdown_articles"  

batch_process_urls(TXT_FILE, SAVE_FOLDER)
# scrape_and_save_jina("https://www.npr.org/2026/04/07/nx-s1-5771707/mental-health-care-workforce-artificial-intelligence-ai", "./data/markdown_articles/article_21.md")