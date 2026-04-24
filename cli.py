import click
from fetcher import fetch_news
from scraper import scrape_rss
from storage import save_articles
from exporter import export_data

@click.group()
def cli():
    """News Aggregator CLI - Fetch, store and export news."""
    pass

@cli.command()
@click.option("--keyword", "-k", default=None, help="Search keyword")
@click.option("--source",  "-s", default=None, help="News source")
@click.option("--date",    "-d", default=None, help="From date YYYY-MM-DD")
@click.option("--limit",   "-l", default=10,   help="Number of articles")
@click.option("--rss",     is_flag=True,        help="Use RSS scraping instead")
def fetch(keyword, source, date, limit, rss):
    """Fetch news and save to database."""
    if rss:
        articles = scrape_rss(source=source or "bbc", limit=limit)
    else:
        articles = fetch_news(keyword=keyword, source=source,
                              date=date, limit=limit)
    if articles:
        save_articles(articles)
    else:
        click.echo("No articles fetched.")

@cli.command()
@click.option("--format",  "-f", "fmt", default="csv",
              type=click.Choice(["csv", "excel"]), help="Export format")
@click.option("--output",  "-o", default="news_export", help="Output filename")
@click.option("--keyword", "-k", default=None, help="Filter by keyword")
@click.option("--source",  "-s", default=None, help="Filter by source")
def export(fmt, output, keyword, source):
    """Export saved articles to CSV or Excel."""
    export_data(fmt=fmt, output=output, keyword=keyword, source=source)

if __name__ == "__main__":
    cli()