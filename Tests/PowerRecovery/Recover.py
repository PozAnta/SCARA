
from Provider import RecoveryPowerCycleProvide
from colorama import Fore, Style


class Main:

    def __init__(self, name_test="NA"):
        self.test = RecoveryPowerCycleProvide.RecoveryPowerCycle("COM4")
        self.name_test = name_test
        self.status = True


class Support(Main):

    def check_all_device_communications(self):
        self.__check_ec_communication()
        self.__check_feedback_communication()
        self.__check_mcu_communication()

    def power_cycle(self):
        pass

    def record(self):
        pass

    def check_enable_status(self):
        pass

    def check_disable_status(self):
        pass

    def check_command_order_enable(self):
        pass

    def check_command_order_disable(self):
        pass

    def enable_setup(self):
        pass

    def disable_setup(self):
        pass

    def movement_test(self):
        pass

    def __check_mcu_communication(self):
        pass

    def __check_ec_communication(self):
        result = self.test.read_ec_communication_status()

    def __check_feedback_communication(self):
        pass


class Test(Support):
    def test(self):
        self.check_all_device_communications()
        self.enable_setup()
        self.check_enable_status()
        self.disable_setup()
        self.check_disable_status()

        self.power_cycle()
        self.check_all_device_communications()
        self.enable_setup()
        self.check_enable_status()
        self.disable_setup()
        self.check_disable_status()
