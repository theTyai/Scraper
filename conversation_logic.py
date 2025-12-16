from playwright.sync_api import sync_playwright
import time

def scrape_conversation(url, limit=50, sort="new"):
    """
    Scrapes comments from a discussion thread (e.g., Reddit).
    """
    results = []
    
    with sync_playwright() as p:
        # Launch browser (headless=True is invisible and faster)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        page = context.new_page()

        print(f"🕵️ Connecting to {url}...")
        page.goto(url, timeout=60000)
        
        # Basic logic to handle simple scraping (e.g., Reddit, HackerNews)
        # This selector logic is generic; for production, you need site-specific selectors
        try:
            page.wait_for_selector('body', timeout=10000)
            
            # Scroll down to load comments
            for _ in range(3):
                page.mouse.wheel(0, 3000)
                time.sleep(1)

            # Generic attempt to find comments (looks for paragraph tags inside list items or divs)
            # For Reddit specifically, we target 'shreddit-comment' or standard elements
            comments = page.locator('p').all_inner_texts()
            
            # Filtering out noise (very short texts usually aren't comments)
            clean_comments = [c for c in comments if len(c) > 20]

            for i, text in enumerate(clean_comments[:limit]):
                results.append({
                    "author": "Unknown (Protected)", # extracting author is harder generically
                    "text": text,
                    "date": "Today",
                    "likes": 0,
                    "replies": 0
                })

        except Exception as e:
            print(f"Error scraping page: {e}")
        finally:
            browser.close()

    if not results:
        # Fallback mock data if scraping fails (so you can test UI)
        return [
            {"author": "System", "text": "Could not extract comments. The site might be blocking bots or the structure is unique.", "likes": 0, "date": "Now"}
        ]

    return results