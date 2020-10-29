import re

import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()


class Scraper:
    def __init__(self, mailer):
        self.mailer = mailer
        self.headers = {
            "User-Agent":
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.74 "
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
            self.mailer.send_mail(url, product_name, price)
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
            self.mailer.send_mail(url, product_name, price)
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
            self.mailer.send_mail(url, product_name, price)
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
            self.mailer.send_mail(url, product_name, price)
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
            self.mailer.send_mail(url, product_name, price)
            return True
        return False

    def check_teknosa_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(class_='product-title').get_text().strip()

        price = float(
            re.findall(r"cd_product_price: '(.*)'", soup.prettify())[0]
        )

        if price < warn_price:
            self.mailer.send_mail(url, product_name, price)
            return True
        return False

    def check_n11_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(class_='proName').get_text().strip()

        price = float(
            re.findall(r'"lowPrice": "(.*)"', soup.prettify())[0]
        )

        if price < warn_price:
            self.mailer.send_mail(url, product_name, price)
            return True
        return False

    def check_ciceksepeti_net_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(class_='o-productDetail__title').get_text().strip()

        price = float(
            re.sub(r'\D', '', soup.find(class_='m-productPrice__value').get_text().strip())
        )

        if price < warn_price:
            self.mailer.send_mail(url, product_name, price)
            return True
        return False

    def check_ciceksepeti_com_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(class_='product__info__title').get_text().strip()

        price = float(
            re.sub(r'\D', '', soup.find(class_='product__info__new-price__integer').get_text().strip())
        )

        if price < warn_price:
            self.mailer.send_mail(url, product_name, price)
            return True
        return False
