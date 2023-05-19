import requests
from bs4 import BeautifulSoup

url = "http://makautexam.net"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")   

pdf_links = []

latest_announcement = soup.find("h3", text="Latest Announcement")
if latest_announcement:
    ul = latest_announcement.find_next_sibling("ul")
    if ul:
        links = ul.find_all("a")
        for link in links[:10]:
            title = link.text.strip()
            href = link.get("href")
            if href.endswith(".pdf"):
                pdf_links.append(href)

# Display the first 10 PDF links under the Latest Announcement
for link in pdf_links:
    print("Title: ",title)
    print("Link: ",link)