import json
import time

from scraper import Scraper

with open('config.json') as json_file:
    config = json.load(json_file)
with open('products.json') as json_file:
    products = json.load(json_file)

scraper = Scraper(config["SENDER_GMAIL"], config["GMAIL_PASSWORD"], config["RECEIVER_EMAIL"])

while True:
    # you can add more link here
    for product in products:
        scraper.check_hepsiburada_product(product['url'], product['warn_price'])
    time.sleep(60 * 60)
