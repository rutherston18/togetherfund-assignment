# use for locally downloaded webpages that we not loading correctly with trafilatura in scrapev2.py

import trafilatura

def extract_from_local_html(html_filepath, save_filepath):
    # Read the raw HTML you saved manually
    with open(html_filepath, 'r', encoding='utf-8') as f:
        raw_html = f.read()

    clean_text = trafilatura.extract(raw_html, include_links=False, include_images=False, include_formatting=True)

    if clean_text:
        with open(save_filepath, "w", encoding="utf-8") as file:
            file.write(clean_text)
        print(f"Success! Saved clean text to {save_filepath}")
    else:
        print("Failed to extract text from the HTML file.")

extract_from_local_html("/home/ruther/Downloads/Leading artificial intelligence–driven drug discovery platforms_ 2025 landscape and global outlook - ScienceDirect.html", "article_missing.md")