from API import Selector
from colorama import Fore
from configparser import ConfigParser


class Support:
    def __init__(self, ip="192.168.0.1", path="C:\\WebDriver\\Test\\chromedriver.exe", user="admin", password="ADMIN"):

        self.ip = ip
        self.path = path
        self.user = user
        self.password = password
        self.io = Selector.IO(self.ip, self.path, self.user, self.password)

        self.config = ConfigParser()
        self.config.read('C:\\Python\\Robot\\Scara\\Tests\\DIO\\Scripts\\IOconfig.ini')

        # print(self.config.options('MainDigitalInputs'))
        self.main_inputs_values = {}
        self.temp_inputs_values = {}
        self.safety_inputs_values = {}
        self.safety_outputs_values = {}
        self.sto_values = {}

        self.get_inputs_config()

        config = ConfigParser()
        config.read('C:\\Python\\Robot\\Scara\\Tests\\DIO\\Scripts\\IOconfig.ini')

    def get_inputs_config(self):
        for input_val in self.config.options('MainDigitalInputs'):
            self.main_inputs_values[input_val] = self.config.get('MainDigitalInputs', str(input_val))

        for input_val in self.config.options('TempDigitalInputs'):
            self.temp_inputs_values[input_val] = self.config.get('TempDigitalInputs', str(input_val))

        for input_val in self.config.options('SafetyDigitalInputs'):
            self.safety_inputs_values[input_val] = (self.config.get('SafetyDigitalInputs', str(input_val)))

        for input_val in self.config.options('SafetyDigitalOutputs'):
            self.safety_outputs_values[input_val] = (self.config.get('SafetyDigitalOutputs', str(input_val)))

        for input_val in self.config.options('STO'):
            self.sto_values[input_val] = (self.config.get('STO', str(input_val)))

    def __open_io_mapping_panel(self):
        self.io.project_editor()
        self.io.io_mapping()
        self.io.maxx_io()

    def open_input_panel(self):
        self.__open_io_mapping_panel()
        self.io.maxx_inputs()

    def connect(self):
        self.io.open_cs()

    def disconnect_cs(self):
        self.io.close_cs()


class ReadInputs(Support):

    def read_return_all_inputs_status_terminal_dict(self, dic):
        dic_answer = {}
        self.io.open_panel_terminal()
        for key, value in dic.items():
            # print(key, value)
            print("Read in: " + str(key))
            dic_answer[key] = (self.io.write_panel_terminal("?sys.din[" + str(key) + "]"))

        self.io.press_close_terminal()

        return dic_answer

    def read_return_all_main_inputs_status_terminal(self):
        result = []
        self.io.open_panel_terminal()
        for value in range(len(self.main_inputs_values)):
            result.append(self.io.write_panel_terminal("?sys.din[" + str(1000 + value) + "]"))
        self.io.press_close_terminal()

        return result

    def read_return_all_temp_inputs_status_terminal(self):
        result = []
        self.io.open_panel_terminal()
        for key, value in self.temp_inputs_values.items():
            print(key)
            result.append(self.io.write_panel_terminal("?sys.din[" + str(key) + "]"))
        '''    
        for value in range(len(self.temp_inputs_values)):
            result.append(self.io.write_panel_terminal("?sys.din[" + str(1100 + value) + "]"))
        '''
        self.io.press_close_terminal()

        return result

    def read_return_all_safe_inputs_status_terminal(self):
        result = []
        self.io.open_panel_terminal()
        for key, value in self.safety_inputs_values.items():
            result.append(self.io.write_panel_terminal("?sys.din[" + str(key) + "]"))
        self.io.press_close_terminal()

        return result

    def read_return_all_safe_outs_status_terminal(self):
        result = []
        self.io.open_panel_terminal()
        for key, value in self.safety_outputs_values.items():
            result.append(self.io.write_panel_terminal("?sys.din[" + str(key) + "]"))
        self.io.press_close_terminal()

        return result

    def read_return_all_safe_sto_status_terminal(self):
        result = []
        self.io.open_panel_terminal()
        for key, value in self.sto_values.items():
            result.append(self.io.write_panel_terminal("?sys.din[" + str(key) + "]"))
        self.io.press_close_terminal()

        return result

    def read_all_inputs_status_terminal(self):
        result = []
        self.io.open_panel_terminal()
        for i in range(1000, 1016, 1):
            print("Read in: " + str(i))
            result.append(self.io.write_panel_terminal("?sys.din[" + str(i) + "]"))

        for i in range(1100, 1156, 1):
            print("Read in: " + str(i))
            result.append(self.io.write_panel_terminal("?sys.din[" + str(i) + "]"))

        self.io.press_close_terminal()
        return result


class ReadOutputs(Support):

    def read_single_out_status(self, out_name):
        self.io.open_panel_terminal()
        result = self.io.write_panel_terminal(out_name)
        self.io.press_close_terminal()
        return result

    def read_all_out_status(self):
        result = []
        self.io.open_panel_terminal()
        for i in range(16):
            out = str(1000 + i)
            print("Read out: " + out)
            result.append(self.io.write_panel_terminal("?sys.dout[" + out + "]"))

        self.io.press_close_terminal()
        return result


class SetResetOutput(Support):

    def set_reset_output(self, num_out):

        if (num_out > 1015) or (num_out < 1000):
            print(Fore.RED + "--> Number of output is out of range")

        out_selector = {"1000": self.io.press_out_1000,
                        "1001": self.io.press_out_1001,
                        "1002": self.io.press_out_1002,
                        "1003": self.io.press_out_1003,
                        "1004": self.io.press_out_1004,
                        "1005": self.io.press_out_1005,
                        "1006": self.io.press_out_1006,
                        "1007": self.io.press_out_1007,
                        "1008": self.io.press_out_1008,
                        "1009": self.io.press_out_1009,
                        "1010": self.io.press_out_1010,
                        "1011": self.io.press_out_1011,
                        "1012": self.io.press_out_1012,
                        "1013": self.io.press_out_1013,
                        "1014": self.io.press_out_1014,
                        "1015": self.io.press_out_1015}

        out_selector[str(num_out)]()  # Call function from dictionary

    def open_output_panel(self):
        self.__open_io_mapping_panel()
        self.io.maxx_outputs()

    @staticmethod
    def set_reset_all_outputs():
        pass
        '''
        out_selector = {1000: self.io.press_out_1000(),
                        1001: self.io.press_out_1001(),
                        1002: self.io.press_out_1002(),
                        1003: self.io.press_out_1003(),
                        1004: self.io.press_out_1004(),
                        1005: self.io.press_out_1005(),
                        1006: self.io.press_out_1006(),
                        1007: self.io.press_out_1007(),
                        1008: self.io.press_out_1008(),
                        1009: self.io.press_out_1009(),
                        1010: self.io.press_out_1010(),
                        1011: self.io.press_out_1011(),
                        1012: self.io.press_out_1012(),
                        1013: self.io.press_out_1013(),
                        1014: self.io.press_out_1014(),
                        1015: self.io.press_out_1015()}
        '''

    def set_all_outs_active_terminal(self):
        self.io.open_panel_terminal()
        for i in range(16):
            self.io.write_panel_terminal("sys.dout[" + str(1000 + i) + "] = 1")
        self.io.press_close_terminal()
