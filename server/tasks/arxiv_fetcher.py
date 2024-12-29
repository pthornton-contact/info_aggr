import feedparser
from urllib.parse import quote
from datetime import datetime

def fetch_arxiv_data(target_author):
    base_url = "https://export.arxiv.org/api/query?"
    query = f"search_query=au:{quote(target_author)}&start=0&max_results=5"
    url = base_url + query

    response = feedparser.parse(url)
    if response.bozo:
        raise Exception(f"Error fetching arXiv data: {response.bozo_exception}")

    papers = []
    for entry in response.entries:
        all_authors = [author.name for author in entry.get("authors", [])]  # Get all authors
        if target_author in all_authors:  # Check if target author is among the contributors
            papers.append({
                "title": entry.get("title", "No Title"),
                "authors": ", ".join(all_authors),  # Store all authors as a comma-separated string
                "published_date": datetime.strptime(entry.get("published", "1970-01-01T00:00:00Z"), "%Y-%m-%dT%H:%M:%SZ"),
                "abstract": entry.get("summary", "No Abstract"),
            })

    return papers