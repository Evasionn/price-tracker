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
- You can test application with using temp mail as receiver. I use [temp-mail.io](https://temp-mail.io/) while masterment.
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

- Run bellow command to set configurations. It will be automatically opened http://localhost:5051 and after saving 
config and product list you can click Shutdown Server button or "ctrl + c" in terminal.
```bash
price_tracker init
``` 

![web-server](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/web-server.png)


- After setting configuration and product list, it is enough to run bellow command.
```bash
price_tracker
```

- To run in background
```bash
nohup python3 -u -m price_tracker
```
## What is New
### Version 0.5
- Some bugs are fixed and includes code refactor works
- Random user agent for get requests
- ebay.com, morhipo.com, teknostore.com, letgo.com, kitapyurdu.com, tozlu.com, dr.com.tr, toyzzshop.com, 
decathlon.com.tr, nike.com scrapers are added
- issue templates are published

Check [change log](https://github.com/Evasionn/price-tracker/blob/master/CHANGE_LOG.md)

## Supported Web Sites
[![amazon.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/amazon.png)](https://www.amazon.com/)
[![ciceksepeti.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/ciceksepeticom.png)](https://www.ciceksepeti.com/)
[![ciceksepeti.net](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/ciceksepetinet.png)](https://www.ciceksepeti.net/)
[![decathlon.com.tr](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/decathlon.png)](https://www.decathlon.com.tr/)
[![dr.com.tr](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/dr.png)](https://www.dr.com.tr/)
[![ebay.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/ebay.png)](https://www.ebay.com/)
[![gittigidiyor.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/gittigidiyor.png)](https://www.gittigidiyor.com/)
[![hepsiburada.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/hepsiburada.png)](https://www.hepsiburada.com/)
[![kitapyurdu.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/kitapyurdu.png)](https://www.kitapyurdu.com/)
[![letgo.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/letgo.png)](https://www.letgo.com/)
[![mediamarkt.com.tr](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/mediamarkt.png)](https://www.mediamarkt.com.tr/)
[![morhipo.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/morhipo.png)](https://www.morhipo.com/)
[![n11.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/n11.png)](https://urun.n11.com/)
[![nike.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/nike.png)](https://www.nike.com/)
[![teknosa.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/teknosa.png)](https://www.teknosa.com/)
[![teknostore.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/teknostore.png)](https://www.teknostore.com/)
[![toyzzshop.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/toyzzshop.png)](https://www.toyzzshop.com/)
[![tozlu.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/tozlu.png)](https://www.tozlu.com/)
[![trendyol.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/trendyol.png)](https://www.trendyol.com/)
[![vatan.com](https://raw.githubusercontent.com/evasionn/price-tracker/develop/docs/vatan.png)](https://www.vatanbilgisayar.com/)


