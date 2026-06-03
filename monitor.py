import requests

URL = "https://nameinu.info/list?sex=woman&age=all&region=kanto"

html = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

print(html[:3000])
