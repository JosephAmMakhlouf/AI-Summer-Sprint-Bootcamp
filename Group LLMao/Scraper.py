
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

def scrape_aljazeera_article(topic):
    print(f"Scraping Al Jazeera for topic: {topic}")
    base_url = "https://www.aljazeera.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Step 1: Load Al Jazeera's news homepage
        res = requests.get(f"{base_url}/news", headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # Step 2: Search for links containing the topic (with multiple selectors)
        article_selectors = [
            "a.u-clickable-card__link",
            "a[href*='/news/']",
            "article a",
            ".post-card a",
            "h3 a",
            "h2 a"
        ]
        
        full_url = None
        for selector in article_selectors:
            articles = soup.select(selector)
            for a in articles:
                href = a.get("href", "")
                title = a.get_text(strip=True)
                
                # Check both URL and title for topic match
                if (topic.lower() in href.lower()) or (topic.lower() in title.lower()):
                    if href.startswith("/"):
                        full_url = base_url + href
                    elif href.startswith("http"):
                        full_url = href
                    else:
                        continue
                    print(f"Found article: {full_url}")
                    break
            if full_url:
                break

        if not full_url:
            return "❌ No article found matching the topic"

        # Step 3: Add delay to be respectful
        time.sleep(1)

        # Step 4: Scrape the article content with multiple fallback selectors
        article_res = requests.get(full_url, headers=headers, timeout=10)
        article_res.raise_for_status()
        article_soup = BeautifulSoup(article_res.text, "html.parser")
        
        # Multiple paragraph selectors to try
        paragraph_selectors = [
            "div.article-p-wrapper > p",
            "div.wysiwyg p",
            "div.content p",
            "article p",
            ".article-body p",
            ".post-content p",
            "div[data-module='ArticleBody'] p",
            "main p"
        ]
        
        text = ""
        for selector in paragraph_selectors:
            paragraphs = article_soup.select(selector)
            if paragraphs:
                text = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
                if text:
                    print(f"✅ Successfully extracted text using selector: {selector}")
                    break
        
        # If no paragraphs found, try to get any text content from the main article area
        if not text:
            main_content = article_soup.find("main") or article_soup.find("article")
            if main_content:
                text = main_content.get_text(strip=True)
                text = " ".join(text.split())  # Clean up whitespace
        
        if not text:
            # Last resort: get all text and filter
            all_text = article_soup.get_text()
            # Try to find content between common markers
            lines = [line.strip() for line in all_text.split('\n') if line.strip()]
            # Filter out very short lines and common navigation text
            content_lines = [line for line in lines if len(line) > 20 and 
                           not any(skip in line.lower() for skip in ['menu', 'search', 'subscribe', 'follow', 'share'])]
            text = "\n".join(content_lines[:50])  # Take first 50 substantial lines
        
        return text[:3000] if text else "❌ Article found but no text extracted"
        
    except requests.RequestException as e:
        return f"❌ Network error: {str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

@app.route("/scrape")
def scrape():
    topic = request.args.get("topic", "")
    if not topic:
        return jsonify({"error": "Missing topic parameter"})
    
    article = scrape_aljazeera_article(topic)
    return jsonify({
        "topic": topic,
        "article": article,
        "status": "success" if not article.startswith("❌") else "error"
    })

@app.route("/")
def home():
    return jsonify({
        "message": "Al Jazeera Scraper API",
        "usage": "GET /scrape?topic=your_topic_here"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
