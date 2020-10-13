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
            soup.find(id='offering-price').get_text().replace(
                '\n', '').split(',')[0].replace('.', ''))

        if price < warn_price:
            self.send_mail(url, product_name)
            return True
        return False

    def check_gittigidiyor_product(self, url: str, warn_price: float) -> bool:
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        product_name = soup.find(id='sp-title').get_text().strip()
        price = float(soup.find(class_='lastPrice').get_text().replace('\n', '').split(',')[0].replace('.', ''))

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
        body = f"{product_name} is cheaper now. Check the link below: \n{url}"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(self.sender_gmail, self.receiver_email, msg)
        print('An email has been sent!')

        server.quit()
