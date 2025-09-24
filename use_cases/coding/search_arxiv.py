# filename: search_arxiv.py
from arxiv import query

query_results = query(query="machine learning healthcare", max_results=5)

for result in query_results:
    print("Title:", result['title'])
    print("Authors:", result['authors'])
    print("Abstract:", result['summary'])
    print("PDF link:", result['pdf_url'])
    print("------------------------------------------------------")