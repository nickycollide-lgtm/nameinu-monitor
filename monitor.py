import requests
from bs4 import BeautifulSoup

URL = "https://nameinu.info/list?sex=woman&age=all&region=kanto"

html = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

soup = BeautifulSoup(html, "html.parser")

cards = soup.select(".card.white")

for card in cards[:10]:
    title = card.select_one(".card-title")

    if title:
        print(title.get_text(strip=True))
