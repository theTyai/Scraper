# scraper/fetcher.py
import requests
from fake_useragent import UserAgent
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
# Note the dot import below - crucial for package structure
from .proxymanager import ProxyManager 

class HTMLFetcher:
    def __init__(self, use_proxy=False):
        self.proxy_manager = ProxyManager() if use_proxy else None
        try:
            self.ua = UserAgent()
        except:
            self.ua = None

    def fetch(self, url):
        headers = {"User-Agent": self.ua.random if self.ua else "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        proxies = self.proxy_manager.get_proxy() if self.proxy_manager else None

        # 1. Try Requests (Fast)
        try:
            print(f"⚡ Fetching with Requests: {url}")
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"⚠️ Requests failed, switching to Playwright: {e}")

        # 2. Fallback to Playwright (Powerful)
        try:
            with sync_playwright() as p:
                print(f"🎭 Fetching with Playwright: {url}")
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url, timeout=30000)
                html = page.content()
                browser.close()
                return html
        except Exception as e:
            print(f"❌ Playwright failed: {e}")
            return None