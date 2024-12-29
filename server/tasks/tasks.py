from server.celery_app import celery, app
from server.models import db, ResearchPaper, StockData
from server.tasks.arxiv_fetcher import fetch_arxiv_data
from server.tasks.stock_fetcher import fetch_stock_data

@celery.task
def fetch_stock_data_task(ticker):
    """Task to fetch and save stock data."""
    with app.app_context():
        # Fetch data from the stock API
        data = fetch_stock_data(ticker)

        # Check for existing entry in the database
        existing_entry = StockData.query.filter_by(ticker=data["ticker"], timestamp=data["timestamp"]).first()
        if not existing_entry:
            # Save new entry if it doesn't already exist
            stock_entry = StockData(**data)
            db.session.add(stock_entry)
            db.session.commit()
            return f"Fetched and saved data for {ticker}"
        else:
            return f"Duplicate data for {ticker} at {data['timestamp']} skipped."

@celery.task
def fetch_arxiv_data_task(author):
    """Task to fetch and save research papers from arXiv."""
    with app.app_context():
        # Fetch papers from arXiv
        papers = fetch_arxiv_data(author)

        for paper in papers:
            # Check for existing entry in the database
            existing_entry = ResearchPaper.query.filter_by(
                title=paper["title"],
                authors=paper["authors"],
                published_date=paper["published_date"]
            ).first()
            if not existing_entry:
                # Save new entry if it doesn't already exist
                paper_entry = ResearchPaper(
                    title=paper["title"],
                    authors=paper["authors"],
                    published_date=paper["published_date"],
                    abstract=paper["abstract"],
                )
                db.session.add(paper_entry)

        # Commit all new entries at once
        db.session.commit()

        return f"Fetched and saved {len(papers)} papers for {author}."