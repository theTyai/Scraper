# scraper/email_crawler.py
import re
from playwright.sync_api import sync_playwright

def crawl_site(start_url, max_pages=1):
    results = []
    visited = set()
    queue = [start_url]
    
    # Regex patterns
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d[\d -]{8,12}\d'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        count = 0
        while queue and count < max_pages:
            url = queue.pop(0)
            if url in visited:
                continue

            try:
                print(f"🕷️ Crawling: {url}")
                page.goto(url, timeout=30000, wait_until="domcontentloaded")
                content = page.content()
                text = page.inner_text("body")
                
                # Extract Data
                emails = set(re.findall(email_pattern, text))
                phones = set(re.findall(phone_pattern, text))
                title = page.title()

                # Basic Name Extraction (Heuristic: looks for "Name: X" patterns or title)
                # In a real tool, you'd use NLP here.
                names = "N/A" 
                
                # Store Result
                for email in emails:
                    results.append({
                        "source_page": url,
                        "email": email,
                        "first_name": title.split(" ")[0] if title else "Unknown", # Placeholder logic
                        "last_name": "",
                        "designations": "Found on Page",
                        "phone": ", ".join(phones)
                    })

                visited.add(url)
                count += 1

            except Exception as e:
                print(f"❌ Error scraping {url}: {e}")

        browser.close()

    if not results:
        # Return a dummy result if nothing found so the UI shows something
        return [{
            "source_page": start_url, 
            "email": "no_emails_found@example.com", 
            "first_name": "No Data", 
            "last_name": "", 
            "designations": "System"
        }]

    return results