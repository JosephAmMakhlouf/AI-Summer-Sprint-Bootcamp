import requests
import os
from newspaper import Article
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_latest_article(keyword):
    #Constructs a URL to query the NewsData.io API
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={keyword}&language=en"

    try:
        #send a GET request to url and times out after 10 seconds if there's no response
        response = requests.get(url, timeout=10)
        #API response is in json format, so make it a python dictionary
        data = response.json()
        #data is a dictionary, it must have "results" as key which contains the articles
        #data["results"] must be a list
        if "results" in data and isinstance(data["results"], list) and data["results"]:
            #Get the first artigle
            article = data["results"][0]
            return article.get("link")
        else:
            return {"error": "No articles found for this keyword."}

    except Exception as e:
        return {"error": str(e)}
    


def extract_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    # return {
    #     "title": article.title,
    #     "text": article.text
    # }
    return article.title + article.text

def scraper(keyword):
    url = get_latest_article(keyword)
    return extract_article_content(url)
