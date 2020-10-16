import getopt
import sys
import time

from helpers import build_invoker


def main(argv):
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print('price_tracker -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('price_tracker  -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
    run(input_file)


def run(input_file):
    invoker = build_invoker(input_file)
    while not invoker.is_empty():
        invoker.execute()
        if invoker.is_empty():
            break
        time.sleep(60 * 60)


if __name__ == '__main__':
    main(sys.argv[1:])
