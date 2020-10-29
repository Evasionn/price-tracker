import json

from price_tracker.commands import Invoker, HepsiburadaCommand, GittigidiyorCommand, TrendyolCommand, AmazonCommand, \
    VatanCommand, TeknosaCommand, N11Command, CiceksepetiNetCommand
from price_tracker.scraper import Scraper


def build_invoker(input_file, mailer):
    # Reading product list
    try:
        with open(input_file) as json_file:
            products = json.load(json_file)
    except ValueError:
        print('Json file that stores products is broken')
        exit(3)

    # Scraper instance that is receiver of commands
    scraper = Scraper(mailer)

    # Creating an invoker for the execute remaining commands
    invoker = Invoker()
    for product in products:
        invoker.register(build_command(scraper, product))

    return invoker


# Function for generating commands from domain address
def build_command(receiver, item):
    if 'hepsiburada' in item['url']:
        return HepsiburadaCommand(receiver, item)
    elif 'gittigidiyor' in item['url']:
        return GittigidiyorCommand(receiver, item)
    elif 'trendyol' in item['url']:
        return TrendyolCommand(receiver, item)
    elif 'amazon' in item['url']:
        return AmazonCommand(receiver, item)
    elif 'vatanbilgisayar' in item['url']:
        return VatanCommand(receiver, item)
    elif 'teknosa' in item['url']:
        return TeknosaCommand(receiver, item)
    elif 'n11' in item['url']:
        return N11Command(receiver, item)
    elif 'ciceksepeti' in item['url']:
        return CiceksepetiNetCommand(receiver, item)
    else:
        print(f'{item["url"]} is a non-supported web site')
