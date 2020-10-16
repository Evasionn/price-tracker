import abc


class ICommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass


class HepsiburadaCommand(ICommand):
    def __init__(self, receiver, arg):
        self.receiver = receiver
        self.arg = arg

    def execute(self):
        return self.receiver.check_hepsiburada_product(self.arg['url'], self.arg['warn_price'])


class GittigidiyorCommand(ICommand):
    def __init__(self, receiver, arg):
        self.receiver = receiver
        self.arg = arg

    def execute(self):
        return self.receiver.check_gittigidiyor_product(self.arg['url'], self.arg['warn_price'])


class TrendyolCommand(ICommand):
    def __init__(self, receiver, arg):
        self.receiver = receiver
        self.arg = arg

    def execute(self):
        return self.receiver.check_trendyol_product(self.arg['url'], self.arg['warn_price'])


class AmazonCommand(ICommand):
    def __init__(self, receiver, arg):
        self.receiver = receiver
        self.arg = arg

    def execute(self):
        return self.receiver.check_amazon_product(self.arg['url'], self.arg['warn_price'])


class VatanCommand(ICommand):
    def __init__(self, receiver, arg):
        self.receiver = receiver
        self.arg = arg

    def execute(self):
        return self.receiver.check_vatan_product(self.arg['url'], self.arg['warn_price'])


class Invoker:
    def __init__(self):
        self.commands = []

    def register(self, command):
        self.commands.append(command)

    def clear(self):
        self.commands.clear()

    def is_empty(self):
        if not self.commands:
            return True
        return False

    def execute(self):
        self.commands = [
            command for command in self.commands
            if not command.execute()
        ]
