# scraper/whois_lookup.py
import whois
from urllib.parse import urlparse

class WhoisLookup:
    def lookup(self, url):
        try:
            domain = urlparse(url).netloc
            # Strip www.
            if domain.startswith("www."):
                domain = domain[4:]
            
            w = whois.whois(domain)
            return {
                "registrar": w.registrar,
                "creation_date": str(w.creation_date),
                "expiration_date": str(w.expiration_date),
                "country": w.country
            }
        except Exception as e:
            return {"error": "Whois lookup failed"}