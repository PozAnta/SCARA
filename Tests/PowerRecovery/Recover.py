
from Provider import InputOutputProvide
from colorama import Fore, Style


class Main:

    def __init__(self, name_test="NA"):
        self.test = InputOutputProvide.IOProvide()
        self.name_test = name_test
        self.status = True


class Support(Main):
    def support_func(self):
        pass


class Test(Support):
    def test(self):
        pass