# PRICE TRACKER
It's a simple python3 application that tracks prices and warn the user by email.

## Dependencies
- This application uses gmail smtp server, so firstly you should have a gmail account.
I suggest you to use two-step verification for the application. For additional information check the links bellow.

    - [Google Two-Step Verification](https://www.google.com/landing/2step/)
    - [Google App Passwords](https://myaccount.google.com/apppasswords)
- python3 `sudo apt-get install python3`
- pip  `sudo apt-get install python3-pip`
- run `pip3 install -r requirements.txt` to install dependencies
## Usage
- Set properties in `config.json`
    - SENDER_GMAIL: Your gmail account will be used for sending email
    - GMAIL_PASSWORD: Your gmail account password.
    - RECEIVER_EMAIL: The email address that the application will inform when the price fell down.
- Edit product list in `products.json`
- run **main.py** `python3 main.py`

### Supported Web Sites
- [hepsiburada.com](https://www.hepsiburada.com/)
- [gittigidiyor.com](https://www.gittigidiyor.com/)
- [trendyol.com](https://www.trendyol.com/)
- [amazon.com](https://www.amazon.com/) for each country
