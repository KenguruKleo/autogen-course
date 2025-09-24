# filename: search_arxiv_alternative.py
import requests
import xml.etree.ElementTree as ET

query = "machine learning healthcare"
url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results=5"

response = requests.get(url)
root = ET.fromstring(response.content)

for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
    title = entry.find('{http://www.w3.org/2005/Atom}title').text
    authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
    summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
    pdf_link = entry.find('{http://www.w3.org/2005/Atom}link').attrib['href']
    
    print("Title:", title)
    print("Authors:", ", ".join(authors))
    print("Abstract:", summary)
    print("PDF link:", pdf_link)
    print("------------------------------------------------------")