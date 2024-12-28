from server.celery_app import celery, app
# from server.models.stock_data import StockData
# from server.models.research_paper import ResearchPaper
# from server.stock_fetcher import fetch_stock_data
# from server.arxiv_fetcher import fetch_arxiv_data
# from server.models import db


@celery.task
def fetch_stock_data_task(ticker):
    with app.app_context():  # Push Flask app context
        from server.models import db
        from server.models.stock_data import StockData
        from server.stock_fetcher import fetch_stock_data

        data = fetch_stock_data(ticker)
        stock_entry = StockData(**data)
        db.session.add(stock_entry)
        db.session.commit()
        return f"Fetched and saved data for {ticker}"


@celery.task
def fetch_arxiv_data_task(author):
    with app.app_context():  # Push Flask app context
        from server.models import db
        from server.models.research_paper import ResearchPaper
        from server.arxiv_fetcher import fetch_arxiv_data

        papers = fetch_arxiv_data(author)
        for paper in papers:
            paper_entry = ResearchPaper(**paper)
            db.session.add(paper_entry)
        db.session.commit()
        return f"Fetched and saved papers for {author}"