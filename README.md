# 🚀 Growth Swift - Micro Tools Scraper

**Growth Swift** is a comprehensive web intelligence dashboard built with Python and Flask. It provides a suite of automated tools to scrape metadata, extract contact details, and analyze social media conversations using **Playwright** and **BeautifulSoup**.

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

### 1. 📊 Metadata Scraper
* Extracts **SEO tags** (Title, Description, Canonical).
* Retrieves **OG (Open Graph)** social tags.
* Analyzes **Keyword Density** and fetches headings (H1-H3).
* Performs **WHOIS lookups** for domain age and ownership.

### 2. 📧 Email & Contact Scraper
* Crawls websites to find **Email Addresses** and **Phone Numbers**.
* Uses **recursive crawling** (up to 5 pages deep) to find team/contact pages.
* Exports leads directly to CSV.

### 3. 💬 Conversation Scraper
* Designed for Reddit threads and forum discussions.
* Extracts user comments, authors, timestamps, and upvotes.
* Includes **"Sort By"** and **"Limit"** filters.
* Powered by **Playwright** to handle dynamic JavaScript loading.

---

## 📂 Project Structure

Ensure your folder looks exactly like this for the tool to work:

```text
GrowthSwiftScraper/
│
├── app.py                      # Main Flask Server (Entry Point)
├── requirements.txt            # Python Dependencies
├── README.md                   # Documentation
│
├── static/
│   └── logo.png                # Your branding logo
│
├── templates/                  # Frontend UI
│   ├── UI.html                 # Main Dashboard
│   ├── metadata.html           # Metadata Tool Interface
│   ├── pagecontent.html        # Email/Contact Tool Interface
│   └── conversation.html       # Conversation Tool Interface
│
└── scraper/                    # Logic Engine
    ├── __init__.py             # (Empty file to make this a package)
    ├── fetcher.py              # Hybrid Request/Playwright fetcher
    ├── parser.py               # BeautifulSoup parser
    ├── proxymanager.py         # Proxy rotation logic
    ├── metadata_extractor.py   # SEO data extraction
    ├── whois_lookup.py         # Domain lookup logic
    ├── email_crawler.py        # Lead generation logic
    └── conversation_logic.py   # Social media scraping logic

🛠️ Installation & Setup
Follow these steps to set up the project locally.

1. Clone the Repository
Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

Bash

git clone [https://github.com/your-username/Growth-Swift-Scraper.git](https://github.com/your-username/Growth-Swift-Scraper.git)
cd Growth-Swift-Scraper
2. Create a Virtual Environment
It is highly recommended to use a virtual environment to avoid conflicts.

For Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
For Mac / Linux:

Bash

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install all the required Python libraries listed in requirements.txt:

Bash

pip install -r requirements.txt
4. Install Browser Engines
This project uses Playwright to scrape dynamic websites (like Reddit or Single Page Apps). You must install the necessary browser binaries:

Bash

playwright install
🚀 How to Run
Start the Server: Ensure your virtual environment is active (you should see (venv) in your terminal), then run:

Bash

python app.py
You should see output similar to:

Plaintext

* Running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (Press CTRL+C to quit)
Open the Dashboard: Open your web browser and navigate to: 👉 http://127.0.0.1:5000

Stop the Server: To stop the application, go back to your terminal and press CTRL + C.

📝 Usage Guide
Metadata Tool
Enter a URL (e.g., https://example.com).

(Optional) Enter a keyword to check how often it appears on the page.

Click Analyze.

Download the report as CSV.

Email Scraper
Enter a target URL (e.g., https://example.com/contact).

Set Max Pages (keep it low, e.g., 2-3, for faster results).

The tool will crawl the links and extract any emails found.

Conversation Scraper
Paste a Reddit thread URL (e.g., https://www.reddit.com/r/technology/comments/...).

Select Sort By (New/Top) and Comment Limit.

Click Extract. The browser will open invisibly (headless mode) to fetch data.

❓ Troubleshooting
Q: ModuleNotFoundError: No module named 'scraper'

Fix: Ensure you are running python app.py from the root folder (GrowthSwiftScraper/), not inside the scraper/ folder. Also, check if scraper/__init__.py exists (it can be empty).

Q: Playwright Error: "Executable doesn't exist"

Fix: You forgot to run playwright install. Run that command in your terminal.

Q: The scraper returns "Connection Error"

Fix: The website might be blocking bots.

Try a different URL.

Open scraper/fetcher.py and ensure headless=True is set (or set to False to see what's happening).

Check your internet connection.

⚠️ Disclaimer
This tool is for educational and research purposes only.

Respect robots.txt files.

Do not use this tool to spam or violate the Terms of Service of any website.

The developers are not responsible for misuse of this software.

Built with ❤️ by Growth Swift