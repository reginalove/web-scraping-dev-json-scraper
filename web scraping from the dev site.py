import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import json

url = "https://web-scraping.dev/"

headers = {
        "user-agent": "mozilla/5.0"
           }

list_web = []

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

everything = soup.select("div.col")

for each in everything:

    time.sleep(2)

    title = each.select_one("h3.card-title").text.strip()
    link = each.select_one("a.card.h-100")
    description = each.select_one("p.card-text").text.strip()
    difficulty = each.select_one("span.difficulty-badge").text.strip()

    link_title = urljoin(url, link["href"])

    follow_up = {"title" : title,
                 "link" : link_title,
                 "description" : description,
                 "difficulty" : difficulty}


    list_web.append(follow_up)

    print(title)
    print(link_title)

with open("web-scraping.json", "w", encoding="utf-8") as file:
    json.dump(list_web, file, ensure_ascii=False, indent=4)

