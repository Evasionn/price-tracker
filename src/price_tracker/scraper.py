import re
import smtplib

import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, sender_gmail, gmail_password, receiver_email):
        self.sender_gmail = sender_gmail
        self.gmail_password = gmail_password
        self.receiver_email = receiver_email
        self.headers = {
            "User-Agent":
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 "
                "Safari/537.36 "
        }

    def check_hepsiburada_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(id='product-name').get_text().strip()
        price = float(
            re.sub(r'\D', '', soup.find(id='offering-price').get_text().split(',')[0])
        )

        if price < warn_price:
            self.send_mail(url, product_name)
            return True
        return False

    def check_gittigidiyor_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(id='sp-title').get_text().strip()
        price = float(
            re.sub(r'\D', '', soup.find(class_='lastPrice').get_text().replace('\n', '').split(',')[0])
        )

        if price < warn_price:
            self.send_mail(url, product_name)
            return True
        return False

    def check_trendyol_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(class_='pr-nm').get_text().strip()
        price = soup.find(class_='prc-dsc')
        if not price:
            price = soup.find(class_='prc-slg')

        price = float(
            re.sub(r'\D', '', price.get_text().split(',')[0])
        )
        if price < warn_price:
            self.send_mail(url, product_name)
            return True
        return False

    def check_amazon_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(id='productTitle').get_text().strip()

        price = soup.find(id='priceblock_dealprice')
        if not price:
            price = soup.find(id='priceblock_ourprice')

        price = float(
            re.sub(r'\D', '', price.get_text().split(',')[0])
        )

        if price < warn_price:
            self.send_mail(url, product_name)
            return True
        return False

    def check_vatan_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(class_='product-list__product-name').get_text().strip()

        price = float(
            re.sub(r'\D', '', soup.find(class_='product-list__price').get_text().strip())
        )

        if price < warn_price:
            self.send_mail(url, product_name)
            return True
        return False

    def send_mail(self, url, product_name):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(self.sender_gmail, self.gmail_password)
        subject = 'Price Fell Down!'
        Tr2Eng = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCĞIOSU")
        body = f"{product_name} is cheaper now. Check the link below: \n{url}".translate(Tr2Eng)

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(self.sender_gmail, self.receiver_email, msg)
        print('An email has been sent!')

        server.quit()
