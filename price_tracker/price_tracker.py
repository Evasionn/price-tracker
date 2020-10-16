import time

from helpers import build_invoker


def run():
    invoker = build_invoker()
    while not invoker.is_empty():
        invoker.execute()
        if invoker.is_empty():
            break
        time.sleep(60 * 60)


if __name__ == '__main__':
    run()
