# PRICE TRACKER
It's a simple python3 application that tracks prices and warn the user by email.

## Dependencies
- This application uses gmail smtp server, so firstly you should have a gmail account.
I suggest you to use two-step verification for the application. For additional information check the links bellow.

    - [Google Two-Step Verification](https://www.google.com/landing/2step/)
    - [Google App Passwords](https://myaccount.google.com/apppasswords)
- pip  `sudo apt-get install python3-pip`
- BeautifulSoup4 library `python3 -m pip install BeautifulSoup4`

## Usage
- Set variables properly
    - SENDER_GMAIL: Your gmail account will be used for sending email
    - PASSWORD: Your gmail account password.
    - RECEIVER_EMAIL: The email address that the application will inform when the price fell down.
    - PRODUCT_URL:  The product url that the application will track
- Edit or add some urls by using 
`check_hepsiburada_link(URL, PRICE)` function. First argument must be an url for the product, and the second parameter is price when the user will inform.
