import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {
    "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

SENDER_GMAIL = 'SENDER_GMAIL'
GMAIL_PASSWORD = 'SENDER_PASSWORD'
RECEIVER_EMAIL = 'RECEIVER_EMAIL'
PRODUCT_URL = 'https://www.hepsiburada.com/iphone-se-64-gb-p-HBV00000SXR45'


def check_hepsiburada_link(url, warn_price):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='product-name').get_text()
    price = float(
        soup.find(id='offering-price').get_text().replace(
            '\n', '').split(',')[0].replace('.', ''))

    if price < warn_price:
        send_mail(url)


def send_mail(url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(SENDER_GMAIL, GMAIL_PASSWORD)
    subject = 'Price Fell Down!'
    body = 'Check the link ' + url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(SENDER_GMAIL, RECEIVER_EMAIL, msg)
    print('HEY! EMAIL HAS BEEN SENT')

    server.quit()


while True:
    check_hepsiburada_link(PRODUCT_URL, 4500)
    time.sleep(60 * 60)
