import json
import time

from commands import HepsiburadaCommand, GittigidiyorCommand, Invoker, TrendyolCommand
from scraper import Scraper

# Reading config file and product list
with open('config.json') as json_file:
    config = json.load(json_file)
with open('products.json') as json_file:
    products = json.load(json_file)

# Scraper instance that is receiver of commands
scraper = Scraper(config["SENDER_GMAIL"], config["GMAIL_PASSWORD"], config["RECEIVER_EMAIL"])


# Function for generating commands from domain address
def build_command(receiver, item):
    if 'hepsiburada' in item['url']:
        return HepsiburadaCommand(receiver, item)
    elif 'gittigidiyor' in item['url']:
        return GittigidiyorCommand(receiver, item)
    elif 'trendyol' in item['url']:
        return TrendyolCommand(receiver, item)


# Creating an invoker for the execute remaining commands
invoker = Invoker()
for product in products:
    invoker.register(build_command(scraper, product))

while not invoker.is_empty():
    invoker.execute()
    if invoker.is_empty():
        break
    time.sleep(60 * 60)
