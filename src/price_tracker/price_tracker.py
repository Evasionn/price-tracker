import getopt
import json
import os
import sys
import time
from getpass import getpass

from price_tracker.helpers import build_invoker
from price_tracker.mailer import Mailer

help_text = '''usage: price_tracker [-h] [-i <input_json>] [-c <config_json>]

Available Arguments
-h  help
-i setting input file
-c setting config file
'''

# create save directory
save_path = os.path.expanduser("~") + '/price-tracker'
os.makedirs(save_path, exist_ok=True)


def ask_config(config_file):
    if config_file != '':
        try:
            with open(config_file) as json_file:
                return json.load(json_file)
        except ValueError:
            print('Json file that stores mailer configuration is broken')
            exit(3)
        except FileNotFoundError:
            print("Config file couldn't be found")
            exit(3)

    try:
        with open(save_path + '/config.json') as json_file:
            config = json.load(json_file)
            answer = input('There is a config file from previous login. Do you want to use it [y|n]: ')
            if answer == 'y':
                return config
            elif answer == 'n':
                os.remove(save_path + '/config.json')
    except FileNotFoundError:
        pass
    except ValueError:
        os.remove(save_path + '/config.json')

    sender_gmail = input('Sender Gmail Address: ')
    gmail_password = getpass(prompt='Gmail Password: ')
    receiver_email = input('Receiver Email Address: ')

    answer = input('Do you want to save this configuration for next login [y|n]: ')
    config = {'sender_gmail': sender_gmail, 'gmail_password': gmail_password, 'receiver_email': receiver_email}
    if answer == 'y':
        with open(save_path + '/config.json', 'w') as config_file:
            json.dump(config, config_file)

    return config


def ask_input_file():
    input_file = input('Type input json path: ')
    return input_file


def main(argv):
    input_file = ''
    config_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:c:")
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt in '-h':
            print(help_text)
            sys.exit(1)
        elif opt in '-i':
            input_file = arg
        elif opt in '-c':
            config_file = arg

    config = ask_config(config_file)

    if input_file == '':
        input_file = ask_input_file()

    run(input_file, config)


def run(input_file, config):
    mailer = Mailer(config["sender_gmail"], config["gmail_password"], config["receiver_email"])
    mailer.log_in()

    invoker = build_invoker(input_file, mailer)
    try:
        while not invoker.is_empty():
            invoker.execute()
            if invoker.is_empty():
                mailer.log_out()
                break
            time.sleep(60 * 60)
    except KeyboardInterrupt:
        mailer.log_out()
        print('')
        sys.exit(0)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print('')
        sys.exit(0)
