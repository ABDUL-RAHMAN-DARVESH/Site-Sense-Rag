# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    print(f"🔍 Scraping URL: {url}")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=15)
        print(f"🔄 Status Code: {response.status_code}")
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        print(f"✅ Scraped text length: {len(text)}")
        return text

    except Exception as e:
        print("❌ Scraper Error:", e)
        return f"Error: {e}"
