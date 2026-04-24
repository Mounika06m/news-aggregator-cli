# \# News Aggregator CLI

# 

# A command-line tool to fetch, store, filter and export news headlines.

# 

# \## Author

# Mounika06m

# 

# \## Features

# \- Fetch news using NewsAPI

# \- RSS scraping fallback

# \- SQLite storage with deduplication

# \- CLI filters: keyword, source, date

# \- Export to CSV and Excel

# 

# \## Setup

# pip install -r requirements.txt

# 

# \## Usage

# python cli.py fetch --keyword "AI" --limit 5

# python cli.py fetch --rss --source bbc --limit 5

# python cli.py export --format csv --output mynews

# python cli.py export --format excel --output mynews

