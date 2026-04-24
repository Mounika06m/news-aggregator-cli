import feedparser

RSS_FEEDS = {
    "bbc":     "http://feeds.bbci.co.uk/news/rss.xml",
    "reuters": "https://feeds.reuters.com/reuters/topNews",
    "hindu":   "https://www.thehindu.com/news/feeder/default.rss",
}

def scrape_rss(source="bbc", limit=10):
    url = RSS_FEEDS.get(source)
    if not url:
        print(f"No RSS feed found for: {source}")
        return []

    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries[:limit]:
        articles.append({
            "title":       entry.get("title"),
            "url":         entry.get("link"),
            "publishedAt": entry.get("published"),
            "source":      {"name": source},
            "content":     entry.get("summary"),
        })

    return articles