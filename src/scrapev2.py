from seleniumbase import Driver
import trafilatura
import time
import os

def scrape_and_save_trafilatura(url, filepath):
    """Fetches a URL using a stealth browser and extracts clean text via Trafilatura."""
    print(f" -> Spinning up stealth browser for: {url}")
    
    # uc=True for bypassing CAPTCHAs, headless=True to run invisibly in background
    # could use headless = False for articles that were not loading correctly with trafilatura before
    driver = Driver(uc=True, headless=True) 
    
    try:
        driver.get(url)
        
        #can increase time here
        time.sleep(10) 
        
        # Grab the raw HTML from the fully loaded page
        raw_html = driver.page_source
        
        # Use Trafilatura to extract the main article and ignore boilerplate
        clean_text = trafilatura.extract(
            raw_html, 
            include_links=False, 
            include_images=False, 
            include_formatting=True 
        )
        
        if clean_text:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(clean_text)
            print(f"   [SUCCESS] Saved clean article to {filepath}")
        else:
            print(f"   [FAILED] Trafilatura could not find main article content for URL: {url}")
            
    except Exception as e:
        print(f"   [ERROR] Failed to scrape {url}: {e}")
        
    finally:
        # ALWAYS quit the driver to free up your computer's memory
        driver.quit() 

def batch_process_urls(txt_file_path, save_directory):
    """Reads a text file of URLs and processes them one by one."""
    
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        print(f"Created directory: {save_directory}")


    try:
        with open(txt_file_path, "r", encoding="utf-8") as file:
            urls = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find the file '{txt_file_path}'")
        return

    print(f"Found {len(urls)} URLs to process.\n" + "-"*30)

    for index, url in enumerate(urls):
        filename = f"article_{index + 1}.md"
        filepath = os.path.join(save_directory, filename)
        
        print(f"\nProcessing ({index + 1}/{len(urls)}): {url}")
        scrape_and_save_trafilatura(url, filepath)
        
        # Optional: A short pause between spinning up new browsers
        time.sleep(2) 

    print("\n" + "-" * 30 + "\nAll done! Your dataset is ready for chunking.")


TXT_FILE = "./data/corpuslinks.txt"          
SAVE_FOLDER = "./data/markdown_articles"  

batch_process_urls(TXT_FILE, SAVE_FOLDER)