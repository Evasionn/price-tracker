# PRICE TRACKER
[![Build Status](https://img.shields.io/pypi/pyversions/price-tracker)](https://pypi.org/project/price-tracker/)
[![License](https://img.shields.io/github/license/Evasionn/price-tracker)](LICENSE)
[![Version](https://img.shields.io/pypi/v/price-tracker)](https://pypi.org/project/price-tracker/)

It's a simple python3 application that tracks prices and warn the user by email.

## Installation
### Requirements
- python3 or later to run price-tracker
- This application uses gmail smtp server, so firstly you should have a gmail account.
I suggest you to use two-step verification for the application. For additional information check the links bellow.

    - [Google Two-Step Verification](https://www.google.com/landing/2step/)
    - [Google App Passwords](https://myaccount.google.com/apppasswords)
- You can test application with using temp mail as receiver. I use [temp-mail.io](https://temp-mail.io/) while development.
### Stable Version
#### Installing via pip
recommended way to install is via pip:
```bash
pip3 install price-tracker
```
### Latest Version
#### Installing from Git
You can install the latest version from Git
```bash
pip3 install git+https://github.com/Evasionn/price-tracker.git
```
## Usage
- input and config files must be json. 
- prepare products.json. Example products.json is must be in format bellow!

```json
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
- To run type in terminal
```bash
price_tracker
``` 
or with defining input file 
```bash
price_tracker -i products.json
```

- optionally you can define a config.json. It should be in format bellow:
```json
{
    "sender_gmail": "gmail@gmail.com",
    "gmail_password": "mygmailpassword!",
    "receiver_mail": "receiver@gmail.com" 
}
```
To run with config file 
```bash
price_tracker -i products.json -c config.json
```

- To run in background products and config file must be given as command line argument
```bash
nohup python3 -u -m price_tracker -i products.json -c config.json &
```
## What is New
### Version 0.4
- Some bugs are fixed and includes code refactor works
- More understandable error messages for the user
- Removing commands that has error
- teknosa.com, n11.com, ciceksepeti.net, ciceksepeti.com, mediamarkt.com.tr scappers are added
- code of conduct is published

## Supported Web Sites
- [hepsiburada.com](https://www.hepsiburada.com/)
- [gittigidiyor.com](https://www.gittigidiyor.com/)
- [trendyol.com](https://www.trendyol.com/)
- [amazon.com](https://www.amazon.com/)
- [vatanbilgisayar.com](https://www.vatanbilgisayar.com/)
- [teknosa.com](https://www.teknosa.com/)
- [n11.com](https://urun.n11.com/)
- [ciceksepeti.net](https://www.ciceksepeti.net/)
- [ciceksepeti.com](https://www.ciceksepeti.com/)
- [mediamarkt.com.tr](https://www.mediamarkt.com.tr/)
- [ebay.com](https://www.ebay.com/)
- [morhipo.com](https://www.morhipo.com/)
- [teknostore.com](https://www.teknostore.com/)
- [letgo.com](https://www.letgo.com/)
- [kitapyurdu.com](https://www.kitapyurdu.com/)
- [tozlu.com](https://www.tozlu.com/)