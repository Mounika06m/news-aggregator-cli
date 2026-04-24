import pandas as pd
from storage import query_articles

COLUMNS = ["id", "title", "source", "url", "published_at", "content"]

def export_data(fmt="csv", output="news_export", keyword=None, source=None):
    rows = query_articles(keyword=keyword, source=source)

    if not rows:
        print("No articles found to export.")
        return

    df = pd.DataFrame(rows, columns=COLUMNS)

    if fmt == "excel":
        filename = f"{output}.xlsx"
        df.to_excel(filename, index=False)
    else:
        filename = f"{output}.csv"
        df.to_csv(filename, index=False)

    print(f"Exported {len(df)} articles to {filename}")