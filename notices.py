import requests
from bs4 import BeautifulSoup

notices = "http://makautexam.net/application-notice.html"

html = requests.get(notices).content
soup = BeautifulSoup(html, "html.parser")

pdf_links = {}


application_forms_notices = soup.find("div", class_="boxWhtHead", text="Application Forms & Notices ").parent
pdf_links["Application Forms & Notices"] = [a["href"] for a in application_forms_notices.find_all("a")]

notices = soup.find("div", class_="boxWhtHead", text="Notices ").parent
pdf_links["Notices"] = [a["href"] for a in notices.find_all("a")]

for title, links in pdf_links.items():
    print(f"{title}:")
    for link in links:
        print(link)
    print()