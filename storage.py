import sqlite3
import hashlib

DB_NAME = "news.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id TEXT PRIMARY KEY,
            title TEXT,
            source TEXT,
            url TEXT,
            published_at TEXT,
            content TEXT
        )
    """)
    conn.commit()
    return conn

def save_articles(articles):
    conn = get_db()
    saved = 0
    for a in articles:
        uid = hashlib.md5(
            (str(a.get("title","")) + str(a.get("url",""))).encode()
        ).hexdigest()
        try:
            conn.execute(
                "INSERT INTO articles VALUES (?,?,?,?,?,?)",
                (
                    uid,
                    a.get("title"),
                    a.get("source", {}).get("name"),
                    a.get("url"),
                    a.get("publishedAt"),
                    a.get("content"),
                )
            )
            saved += 1
        except sqlite3.IntegrityError:
            pass  # duplicate, skip
    conn.commit()
    conn.close()
    print(f"Saved {saved} new articles (duplicates skipped).")

def query_articles(keyword=None, source=None):
    conn = get_db()
    query = "SELECT * FROM articles WHERE 1=1"
    params = []
    if keyword:
        query += " AND title LIKE ?"
        params.append(f"%{keyword}%")
    if source:
        query += " AND source LIKE ?"
        params.append(f"%{source}%")
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows