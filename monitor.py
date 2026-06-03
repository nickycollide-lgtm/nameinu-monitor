import requests
from bs4 import BeautifulSoup

URL = "https://nameinu.info/list?sex=woman&age=all&region=kanto"

print("開始")

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

print("HTML取得成功")
print("文字数:", len(html))

soup = BeautifulSoup(html, "html.parser")

cards = soup.select(".card.white")

print("カード数:", len(cards))

for card in cards[:5]:
    title = card.select_one(".card-title")
    if title:
        print(title.get_text(strip=True))

print("終了")
