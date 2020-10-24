# PRICE TRACKER
It's a simple python3 application that tracks prices and warn the user by email.

## Dependencies
- This application uses gmail smtp server, so firstly you should have a gmail account.
I suggest you to use two-step verification for the application. For additional information check the links bellow.

    - [Google Two-Step Verification](https://www.google.com/landing/2step/)
    - [Google App Passwords](https://myaccount.google.com/apppasswords)
- python3 and pip `sudo apt install python3 python3-pip`

- run `pip3 install -r requirements.txt` to install dependencies

- You can test application with using temp mail as receiver. I use [temp-mail.io](https://temp-mail.io/) while development.
## Usage
- input and config files must be json. 
- prepare products.json. Example products.json is must be in format bellow!

```
[
  {
    "url": "https://www.hepsiburada.com/iphone-se-64-gb-p-HBV00000SXR45",
    "warn_price": 5000
  },
  {
    "url": "https://www.amazon.com.tr/Philips-Hd7461-20-Kahve-Makinesi/dp/B00R04CAH0/ref=zg_bs_kitchen_home_1?_encoding=UTF8&psc=1&refRID=Q90ZVE1A20WY367CAJPQ",
    "warn_price": 550
  },
  {
    "url": "https://www.vatanbilgisayar.com/arnica-ih33151-demli-rose-cay-makinesi.html",
    "warn_price": 340
  }
]
```
- run `python3 price_tracker.py` or with defining input file path `python3 price_tracker -i products.json`

- optionally you can define a config.json. It should be in format bellow:
```
{
    "sender_gmail": "gmail@gmail.com"
    "gmail_password": "mygmailpassword!"
    "receiver_mail": "receiver@gmail.com" 
}
```
To run with config file `python3 price_tracker.py -i products.json -c config.json`

### Supported Web Sites
- [hepsiburada.com](https://www.hepsiburada.com/)
- [gittigidiyor.com](https://www.gittigidiyor.com/)
- [trendyol.com](https://www.trendyol.com/)
- [amazon.com](https://www.amazon.com/) for each country
- [vatanbilgisayar.com](https://www.vatanbilgisayar.com/)
