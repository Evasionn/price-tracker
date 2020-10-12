import json
import time

from scraper import Scraper

with open('config.json') as json_file:
    config = json.load(json_file)
with open('products.json') as json_file:
    products = json.load(json_file)

scraper = Scraper(config["SENDER_GMAIL"], config["GMAIL_PASSWORD"], config["RECEIVER_EMAIL"])

while True:
    products = scraper.run(products)
    if not products:
        break

    time.sleep(60 * 60)
