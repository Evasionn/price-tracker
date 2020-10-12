import json
import time

from scraper import Scraper

PRODUCT_URL = 'https://www.hepsiburada.com/iphone-se-64-gb-p-HBV00000SXR45'

with open('config.json') as json_file:
    data = json.load(json_file)

scraper = Scraper(data["SENDER_GMAIL"], data["GMAIL_PASSWORD"], data["RECEIVER_EMAIL"])

while True:
    # you can add more link here
    scraper.check_hepsiburada_product(PRODUCT_URL, 5000)
    time.sleep(60 * 60)
