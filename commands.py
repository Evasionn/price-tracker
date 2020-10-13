import abc


class ICommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass


class HepsiburadaCommand(ICommand):
    def __init__(self, scraper, url, warn_price):
        self.scrapper = scraper
        self.url = url
        self.warn_price = warn_price

    def execute(self):
        return self.scrapper.check_hepsiburada_product(self.url, self.warn_price)


class GittigidiyorCommand(ICommand):
    def __init__(self, scraper, url, warn_price):
        self.scrapper = scraper
        self.url = url
        self.warn_price = warn_price

    def execute(self):
        return self.scrapper.check_gittigidiyor_product(self.url, self.warn_price)
