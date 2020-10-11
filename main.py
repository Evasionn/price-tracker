from scraper import Scraper
import time

SENDER_GMAIL = 'SENDER_GMAIL'
GMAIL_PASSWORD = 'GMAIL_PASSWORD'
RECEIVER_EMAIL = 'RECEIVER_EMAIL'
PRODUCT_URL = 'https://www.hepsiburada.com/iphone-se-64-gb-p-HBV00000SXR45'

scraper = Scraper(SENDER_GMAIL, GMAIL_PASSWORD, RECEIVER_EMAIL)

while True:
    # you can add more link here
    scraper.check_hepsiburada_product(PRODUCT_URL, 4500)
    time.sleep(60 * 60)
