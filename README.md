# news-aggregator-cli# News Aggregator CLI

Fetch, store, filter and export news headlines from the command line.

## Setup
pip install -r requirements.txt

## Usage
python cli.py fetch --keyword "AI" --limit 5
python cli.py export --format excel --output news

## Features
- NewsAPI integration
- SQLite storage with deduplication
- CSV / Excel export
- CLI filters: keyword, source, date