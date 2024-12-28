# server/tasks/arxiv_fetcher.py

def fetch_arxiv_data(author):
    """
    Simulate fetching research papers for a given author from Arxiv.
    """
    from datetime import datetime
    return [
        {
            "title": f"Research Paper by {author}",
            "authors": author,
            "published_date": datetime.utcnow(),
            "abstract": "This is a mock abstract for demonstration purposes."
        }
    ]