from Provider import InputOutputProvide
from colorama import Fore, Style


class Main:

    def __init__(self, name_test="NA"):
        self.test = InputOutputProvide.IOProvide()
        self.name_test = name_test
        self.status = True
        '''
        self.dict = {1000: 1,
                     1001: 1,
                     1002: 1,
                     1003: 1,
                     1004: 1,
                     1005: 1,
                     1006: 1,
                     1007: 1,
                     1008: 1,
                     1009: 1,
                     1010: 1,
                     1011: 1,
                     1012: 1,
                     1013: 1,
                     1014: 1,
                     1015: 1}

        self.dict_temp_input = {1100: 0,
                                1101: 0,
                                1102: 0,
                                1103: 0,
                                1104: 0,
                                1105: 0,
                                1106: 0,
                                1107: 0,
                                1116: 0,
                                1117: 0,
                                1118: 0,
                                1119: 0,
                                1120: 0,
                                1121: 0,
                                1122: 0,
                                1123: 0,
                                1133: 0,
                                1134: 0,
                                1135: 0,
                                1136: 0,
                                1137: 0,
                                1144: 0,
                                1145: 0,
                                1146: 0,
                                1147: 0,
                                1151: 0}

        self.dict_brakes_sto = {1138: 0,
                                1139: 0,
                                1140: 0,
                                1141: 1,
                                1142: 1,
                                1143: 1}

        self.dict_ss1 = {1148: 0,
                         1149: 0,
                         1150: 0}

        self.dict_ss2 = {1152: 0,
                         1153: 0,
                         1154: 0,
                         1155: 0}

        self.dict_save_di = {1108: 0,
                             1109: 0,
                             1110: 0,
                             1111: 0,
                             1112: 0,
                             1113: 0,
                             1114: 0,
                             1115: 0}

        self.dict_save_d0 = {1124: 0,
                             1125: 0,
                             1126: 0,
                             1127: 0,
                             1128: 0,
                             1129: 0,
                             1130: 0,
                             1131: 0,
                             1132: 0}
        '''


class Support(Main):

    def compare_default_status_inputs_terminal_with_ref(self):
        print(Fore.LIGHTBLUE_EX + "-->Check default status input")
        print(Style.RESET_ALL)
        main_inputs = self.test.read_return_all_main_inputs_status_terminal()
        tem_inputs = self.test.read_return_all_temp_inputs_status_terminal()
        safe_inputs = self.test.read_return_all_safe_inputs_status_terminal()
        safe_sto = self.test.read_return_all_safe_sto_status_terminal()
        safe_out = self.test.read_return_all_safe_outs_status_terminal()
        count = 0

        for key, value in self.test.main_inputs_values.items():

            if int(value) == int(main_inputs[count]):
                print(Fore.GREEN + "--The status of input " + str(value) + "...OK")
                print(Style.RESET_ALL)
                count += 1
            else:
                print(Fore.RED + "--The status of input measured: " + str(value) + " The status of input master: "
                      + str(main_inputs[count]) + " FAIL--")
                print(Style.RESET_ALL)
                self.status = False
                count += 1

        for key, value in self.test.temp_inputs_values.items():

            if int(value) == int(tem_inputs[count]):
                print(Fore.GREEN + "--The status of input " + str(value) + "...OK")
                print(Style.RESET_ALL)
                count += 1
            else:
                print(Fore.RED + "--The status of input measured: " + str(value) + " The status of input master: "
                      + str(tem_inputs[count]) + " FAIL--")
                print(Style.RESET_ALL)
                self.status = False
                count += 1


class Test(Support):

    def inputs_test(self):
        self.test.connect()
        self.status = True

        print(Fore.LIGHTBLUE_EX + "--Start " + self.name_test + " test--")
        self.compare_default_status_inputs_terminal_with_ref()

        if self.status:
            print(Fore.GREEN + "--End " + self.name_test + " test with status PASS--")
        else:
            print(Fore.RED + "--End " + self.name_test + " test with status FAIL--")

        print(Style.RESET_ALL)
        self.test.disconnect_cs()

    def output_test(self):
        self.test.connect()
        self.status = True
        print(Fore.LIGHTBLUE_EX + "--Start " + self.name_test + " test--")

        if self.status:
            print(Fore.GREEN + "--End " + self.name_test + " test with status PASS--")
        else:
            print(Fore.RED + "--End " + self.name_test + " test with status FAIL--")

        print(Style.RESET_ALL)
        self.test.disconnect_cs()


new_test = Test("input")
new_test.inputs_test()
