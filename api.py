from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

@app.route('/announcements', methods=['GET'])
def getAnnouncements():
    announcements = "http://makautexam.net/announcement.html"

    html = requests.get(announcements).content
    soup = BeautifulSoup(html, 'html.parser')

    pdf_links = []
    latAnnounces = soup.find('ul', class_="download")

    for item in latAnnounces.contents[:22]:
        if item.name == 'li':
            link = item.find('a')
            if link:
                title = link.text.strip()
                href = link.get('href')
                href.replace(" ", "%20")

                if not href.startswith("http://makautexam.net/"):
                    href="http://makautexam.net/"+href
                    
                if href.endswith(".pdf"):
                    pdf_links.append((title, href))

    # Return the first 10 PDF links with titles as JSON
    response = [{'title': title, 'link': link} for title, link in pdf_links[:11]]
    return jsonify(response)

@app.route('/mainPage', methods=['GET'])
def getMainPage():
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
                    pdf_links.append({
                        "title": title,
                        "link": href
                    })

    return jsonify(pdf_links)

if __name__ == '__main__':
    app.run()
