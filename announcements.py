import requests
from bs4 import BeautifulSoup

announcements = "http://makautexam.net/announcement.html"

html = requests.get(announcements).content
soup = BeautifulSoup(html, 'html.parser')

pdf_links = []
latAnnounces = soup.find('ul', class_="download")

for item in latAnnounces.contents[:20]:
    if item.name == 'li':
        link = item.find('a')
        if link:
            title = link.text.strip()
            href = link.get('href')
            if href.endswith(".pdf"):
                pdf_links.append((title, href))

# Print the first 10 PDF links with titles
for title, link in pdf_links:
    print("Title:", title)
    print("Link:", link)
    print()