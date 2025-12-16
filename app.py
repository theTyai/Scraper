import os
import io
import sys
import traceback
import pandas as pd
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS

# Import your scraper modules
# Ensure the 'scraper' folder has an empty __init__.py file
from scraper.fetcher import HTMLFetcher
from scraper.parser import HTMLParser
from scraper.metadata_extractor import MetadataExtractor
from scraper.whois_lookup import WhoisLookup
# You need to ensure email_crawler.py is inside /scraper/ folder or adjust import
from scraper.email_crawler import crawl_site 
from scraper.conversation_logic import scrape_conversation

app = Flask(__name__)
CORS(app)

# Global storage for last scrape (for CSV downloading)
last_scraped_data = []

# --- ROUTING (Frontend) ---
@app.route("/")
def home():
    return render_template("UI.html")

@app.route("/templates/metadata.html")
def metadata_page():
    return render_template("metadata.html")

@app.route("/templates/pagecontent.html")
def pagecontent_page():
    return render_template("pagecontent.html")

@app.route("/templates/conversation.html")
def conversation_page():
    return render_template("conversation.html")


# --- API: METADATA SCRAPER ---
@app.route("/scrape", methods=["POST"])
def scrape_metadata_endpoint():
    global last_scraped_data
    data = request.json
    url = data.get("url")
    keyword = data.get("keyword")

    try:
        # 1. Fetch
        fetcher = HTMLFetcher()
        html = fetcher.fetch(url)
        if not html: return jsonify({"error": "Failed to fetch HTML"}), 400

        # 2. Parse & Extract
        parser = HTMLParser()
        soup = parser.parse(html)
        extractor = MetadataExtractor()
        metadata = extractor.extract(soup, url)

        # 3. Whois
        whois = WhoisLookup()
        metadata["whois"] = whois.lookup(url)

        # 4. Keyword Analysis
        if keyword:
            text = soup.get_text(separator=" ", strip=True)
            snippets = [s.strip() for s in text.split(". ") if keyword.lower() in s.lower()]
            metadata["keyword"] = {"term": keyword, "count": len(snippets), "snippets": snippets}

        last_scraped_data = [metadata] # Store as list for consistency
        return jsonify(metadata)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# --- API: EMAIL SCRAPER ---
@app.route("/api/crawl", methods=["POST"])
def scrape_email_endpoint():
    global last_scraped_data
    data = request.json
    url = data.get("url")
    max_pages = int(data.get("max_pages", 1))

    try:
        results = crawl_site(start_url=url, max_pages=max_pages)
        last_scraped_data = results
        return jsonify({"success": True, "results": results})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# --- API: CONVERSATION SCRAPER (NEW) ---
@app.route("/api/scrape_conversation", methods=["POST"])
def scrape_conversation_endpoint():
    global last_scraped_data
    data = request.json
    url = data.get("url")
    limit = int(data.get("limit", 10))
    sort = data.get("sort", "new")

    try:
        results = scrape_conversation(url, limit, sort)
        last_scraped_data = results
        return jsonify({"success": True, "results": results})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)}), 500


# --- API: DOWNLOAD CSV ---
@app.route("/api/download", methods=["POST"])
def download_csv():
    # Accepts data directly or falls back to server memory
    data = request.json.get("results") or last_scraped_data
    
    if not data:
        return jsonify({"error": "No data to download"}), 400

    try:
        # Normalize data (handle both flat lists and nested metadata dicts)
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame([data])

        buffer = io.BytesIO()
        df.to_csv(buffer, index=False, encoding="utf-8")
        buffer.seek(0)
        
        return send_file(
            buffer,
            mimetype="text/csv",
            as_attachment=True,
            download_name="growth_swift_data.csv"
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)