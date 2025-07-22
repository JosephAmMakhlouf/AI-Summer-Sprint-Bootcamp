import os
from flask import Flask, jsonify
from newspaper import Article
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_latest_article(keyword):
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={keyword}&language=en"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if "results" in data and isinstance(data["results"], list) and data["results"]:
            article = data["results"][0]
            return article.get("link")
        else:
            return None
    except Exception as e:
        return None

def extract_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title + "\n\n" + article.text

def scraper(keyword):
    url = get_latest_article(keyword)
    if url:
        return extract_article_content(url)
    else:
        return "No article found."

app = Flask(__name__)

@app.route("/")
def home():
    return "Scraper is running. Use /scrape/<keyword>"

@app.route("/scrape/<keyword>")
def scrape_route(keyword):
    content = scraper(keyword)
    return jsonify({"content": content})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

