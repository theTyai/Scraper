# scraper/parser.py
from bs4 import BeautifulSoup

class HTMLParser:
    def parse(self, html):
        # Uses lxml for speed, falls back to html.parser if lxml isn't installed
        return BeautifulSoup(html, "html.parser")