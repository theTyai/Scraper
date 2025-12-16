# 🚀 Growth Swift – Micro Tools Scraper

**Growth Swift** is a web intelligence dashboard built with **Python** and **Flask**. It provides a suite of automated tools to scrape website metadata, extract contact details, and analyze social media conversations using **Playwright** and **BeautifulSoup**.

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

### 📊 Metadata Scraper

* Extracts **SEO tags** (Title, Meta Description, Canonical).
* Retrieves **Open Graph (OG)** social tags.
* Analyzes **keyword density** and extracts headings (H1–H3).
* Performs **WHOIS lookups** to determine domain age and ownership.

### 📧 Email & Contact Scraper

* Crawls websites to find **email addresses** and **phone numbers**.
* Uses **recursive crawling** (configurable depth) to discover contact/team pages.
* Exports extracted leads to **CSV**.

### 💬 Conversation Scraper

* Designed for **Reddit threads** and forum discussions.
* Extracts comments, authors, timestamps, and upvotes.
* Supports **Sort By** (New / Top) and **Limit** filters.
* Powered by **Playwright** to handle dynamic JavaScript content.

---

## 📂 Project Structure

Ensure your folder structure matches the following:

```text
GrowthSwiftScraper/
│
├── app.py                      # Main Flask server (entry point)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── static/
│   └── logo.png                # Branding assets
│
├── templates/                  # Frontend templates
│   ├── UI.html                 # Main dashboard
│   ├── metadata.html           # Metadata tool UI
│   ├── pagecontent.html        # Email/Contact tool UI
│   └── conversation.html       # Conversation tool UI
│
└── scraper/                    # Core scraping logic
    ├── __init__.py             # Marks this directory as a package
    ├── fetcher.py              # Requests/Playwright fetcher
    ├── parser.py               # BeautifulSoup parsing helpers
    ├── proxymanager.py         # Proxy rotation logic
    ├── metadata_extractor.py   # SEO data extraction
    ├── whois_lookup.py         # Domain WHOIS lookup
    ├── email_crawler.py        # Email & contact crawling
    └── conversation_logic.py   # Social media scraping logic
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Growth-Swift-Scraper.git
cd Growth-Swift-Scraper
```

### 2️⃣ Create a Virtual Environment

Using a virtual environment is **highly recommended**.

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Playwright Browsers

Playwright requires browser binaries for scraping dynamic sites:

```bash
playwright install
```

---

## 🚀 Running the Application

Ensure the virtual environment is active, then start the server:

```bash
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Open your browser and visit:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

To stop the server, press **CTRL + C** in the terminal.

---

## 📝 Usage Guide

### 🔍 Metadata Tool

1. Enter a URL (e.g., `https://example.com`).
2. (Optional) Provide a keyword to analyze its frequency.
3. Click **Analyze**.
4. Download the generated report as **CSV**.

### 📧 Email & Contact Scraper

1. Enter a target URL (e.g., `https://example.com/contact`).
2. Set **Max Pages** (recommended: 2–3 for faster results).
3. Start crawling to extract emails and phone numbers.

### 💬 Conversation Scraper

1. Paste a Reddit thread URL (e.g., `https://www.reddit.com/r/technology/...`).
2. Choose **Sort By** (New / Top) and set a **comment limit**.
3. Click **Extract**. Playwright will fetch the content in headless mode.

---

## ❓ Troubleshooting

**Q: `ModuleNotFoundError: No module named 'scraper'`**
**Fix:** Run `python app.py` from the project root (`GrowthSwiftScraper/`). Ensure `scraper/__init__.py` exists.

**Q: Playwright error – "Executable doesn't exist"**
**Fix:** Run `playwright install` to download browser binaries.

**Q: Connection or blocking errors**

* The site may be blocking bots.
* Try a different URL.
* In `scraper/fetcher.py`, set `headless=False` to debug.
* Check your internet connection or proxy configuration.

---

## ⚠️ Disclaimer

This project is intended for **educational and research purposes only**.

* Respect `robots.txt` and website Terms of Service.
* Do **not** use this tool for spamming or abusive scraping.
* The authors are **not responsible** for any misuse of this software.

---

Built with ❤️ by **Growth Swift**
