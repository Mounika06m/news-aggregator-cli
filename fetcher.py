import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(keyword=None, source=None, date=None, limit=10):
    params = {
        "apiKey": API_KEY,
        "pageSize": limit,
    }
    if keyword:
        params["q"] = keyword
    if source:
        params["sources"] = source
    if date:
        params["from"] = date

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print(f"Error: {data.get('message')}")
        return []

    return data.get("articles", [])