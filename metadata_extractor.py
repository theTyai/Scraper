# scraper/metadata_extractor.py
from bs4 import BeautifulSoup

class MetadataExtractor:
    def extract(self, soup, url):
        data = {}

        # Safe extraction helper
        def get_text(elem):
            return elem.get_text(strip=True) if elem else None

        def get_attr(elem, attr):
            return elem[attr] if elem and elem.has_attr(attr) else None

        data["source_url"] = url
        data["title"] = get_text(soup.title)
        
        meta_desc = soup.find("meta", attrs={"name": "description"})
        data["description"] = get_attr(meta_desc, "content")

        canonical = soup.find("link", rel="canonical")
        data["canonical"] = get_attr(canonical, "href")

        # OG Tags
        og = {}
        for tag in soup.find_all("meta"):
            if tag.get("property", "").startswith("og:"):
                og[tag["property"]] = tag.get("content")
        data["og_tags"] = og

        # Images (First 5 to save space)
        images = [img["src"] for img in soup.find_all("img", src=True)]
        data["images"] = images[:5] 

        # Headings
        data["headings"] = {
            "h1": [h.get_text(strip=True) for h in soup.find_all("h1")],
            "h2": [h.get_text(strip=True) for h in soup.find_all("h2")]
        }

        return data