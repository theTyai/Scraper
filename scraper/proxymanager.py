# scraper/proxymanager.py
import random

class ProxyManager:
    def __init__(self):
        # Add your proxies here: "http://user:pass@ip:port"
        self.proxies = []

    def get_proxy(self):
        if not self.proxies:
            return None
        proxy = random.choice(self.proxies)
        return {"http": proxy, "https": proxy}