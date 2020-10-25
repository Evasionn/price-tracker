import sys


def main():
    from price_tracker.price_tracker import main
    args = sys.argv[1:]
    main(args)


if __name__ == '__main__':
    main()
