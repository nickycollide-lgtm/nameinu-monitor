import cloudscraper

scraper = cloudscraper.create_scraper()

html = scraper.get(url).text
