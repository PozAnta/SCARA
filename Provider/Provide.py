import time
from API import PortSerial, Telnet, Selector
from colorama import Fore


class Main:

    def __init__(self, ip, path, user, password):

        self.ip = ip
        self.path = path
        self.user = user
        self.password = password
        self._mc_terminal = Selector.Select(self.ip, self.path, self.user, self.password)


class CommunicationSerial:

    def __init__(self, port):
        self.port = port
        self.serial = PortSerial

    def write_serial(self, cmd):
        self.serial.port(cmd, self.port, 1)

    def write_read_serial(self, cmd):
        return self.serial.port(cmd, self.port, 1)


class CommunicationTelnet:

    def __init__(self):
        self.communication_count_attempt = 10
        self.__tn = Telnet.TelComm("192.168.57.100", "4000")

    def telnet_write(self, cmd):
        self.__tn.write(cmd)

    def telnet_read(self, cmd):
        return self.__tn.read(cmd)

    def telnet_write_read(self, cmd):
        return self.__tn.write_read(cmd)


class InputOutput:

    def __init__(self, ip, path, user, password):
        self.ip = ip
        self.path = path
        self.user = user
        self.password = password
        self.io = Selector.IO(self.ip, self.path, self.user, self.password)

    def connect(self):
        self.io.open_cs()

    def __open_io_mapping_panel(self):
        self.io.project_editor()
        self.io.io_mapping()
        self.io.maxx_io()

    def open_input_panel(self):
        self.__open_io_mapping_panel()
        self.io.maxx_inputs()

    def read_input_status(self):
        self.io.read_status_in5()

    def open_output_panel(self):
        self.__open_io_mapping_panel()
        self.io.maxx_outputs()
        pass

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

    def set_reset_all_outputs(self):
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

    def read_all_inputs_status_terminal_dict(self, dic):
        dic_answer = {}
        for key, value in dic.items():
            # print(key, value)

            print("Read in: " + str(key))
            dic_answer[key] = (self.io.write_panel_terminal("?sys.din[" + str(key) + "]"))

        self.io.press_close_terminal()

        return dic_answer

    def set_all_outs_active_terminal(self):
        self.io.open_panel_terminal()
        for i in range(16):
            out = str(1000 + i)
            self.io.write_panel_terminal("sys.dout[" + out + "] = 1")

        self.io.press_close_terminal()

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

    def read_out_status(self, out_name):
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


class EnableDisable:

    def __init__(self, ip, path, user, password):
        self.ip = ip
        self.path = path
        self.user = user
        self.password = password
        self.serial_port = "COM4"
        self.home = Selector.Home(self.ip, self.path, self.user, self.password)
        self.proj_editor = Selector.ProjectEditor(self.ip, self.path, self.user, self.password)
        self.tel_comm = CommunicationTelnet()
        self.serial_comm = CommunicationSerial(self.serial_port)

        self.enable_status_drive = "?EnableModule.Active"
        self.enable_status_mc = "?Scara.En"

    def connect(self):
        self.home.open_cs()

    def disconnect(self):
        self.home.close_cs()

    def enable_disable_button(self):
        self.home.power_button()

    def read_setup_active_status_from_terminal(self):
        self.proj_editor.open_panel_terminal()
        out = self.proj_editor.write_panel_terminal(self.enable_status_mc)
        self.proj_editor.press_close_terminal()
        return out

    def enable_setup_terminal(self):
        self.proj_editor.open_panel_terminal()
        self.proj_editor.write_panel_terminal("Scara.En=1")
        self.proj_editor.press_close_terminal()

    def disable_setup_terminal(self):
        self.proj_editor.open_panel_terminal()
        self.proj_editor.write_panel_terminal("Scara.En=0")
        self.proj_editor.press_close_terminal()

    def read_active_status_drive(self):
        result = []
        for i in range(1, 5, 1):
            result.append(self.tel_comm.telnet_write_read(self.enable_status_drive + "[" + str(i) + "]"))
        return result


class RecoveryPowerCycle(EnableDisable):

    def disconnect(self):
        self.disconnect()

    def perform_power_cycle(self):
        self.serial_comm.write_serial("outinv 2 0")
        time.sleep(5)
        self.serial_comm.write_serial("outinv 2 1")

    def perform_motion_adept_script(self):
        self.proj_editor.project_editor()
        self.proj_editor.apps_folder()
        self.proj_editor.adpt_folder()
        self.proj_editor.prog_adpt_folder()
        self.proj_editor.run_programm()

    def perform_kill_adept_script(self):
        self.proj_editor.kill_unload()


class VariableGains(CommunicationTelnet, Selector.ProjectEditor):

    def __init__(self, ip="192.168.0.1", path="C:\\WebDriver\\Test\\chromedriver.exe", user="admin", password="ADMIN"):
        super().__init__()
        self.ip = ip
        self.path = path
        self.user = user
        self.password = password
        self.serial_port = "COM4"

        self.path_full_config = 'C:\\Python\\Robot\\Scara\\Tests\\VariableGains\\Script\\config_full.txt'
        self.path_part_config = 'C:\\Python\\Robot\\Scara\\Tests\\VariableGains\\Script\\config_part.txt'
        self.path_params = 'C:\\Python\\Robot\\Scara\\Tests\\VariableGains\\Script\\'

        # self._mc_project = Selector.Home(self.ip, self.path, self.user, self.password)
        # self._mc_script = Selector.ProjectEditor(self.ip, self.path, self.user, self.password)
        # self.tel_comm = CommunicationTelnet()

        self.vargain_axis_disc = "vargains.axis.desc"
        self.vargain_enable = "vargains.enable"
        self.__execute_vargains = "vargains.execute"
        self.__cntrl_execute = "control.execute"

        self.actual_gains_params = ["vel.pdff.kp.act",
                                    "vel.pdff.kfr.act",
                                    "vel.pdff.ki.act",
                                    "pos.kafrc.act",
                                    "pos.kafrc.pole.f.act",
                                    "pos.kafrv.act",
                                    "pos.kp.act",
                                    "pos.kvfr.act",
                                    "pos.kvfr.pole.f.act"]

        self.gains_params = ["vel.pdff.kp",
                             "vel.pdff.kfr",
                             "vel.pdff.ki",
                             "pos.kafrc",
                             "pos.kafrc.pole.f",
                             "pos.kafrv",
                             "pos.kp",
                             "pos.kvfr",
                             "pos.kvfr.pole.f"]

    def read_axis_description(self):
        result = []
        for i in range(4):
            try:
                result.append(self.telnet_write_read("?" + self.vargain_axis_disc + "[0]" +
                                                              "[" + str(i) + "]"))
            except ValueError:
                return result
        return result

    def write_axis_description(self, command):
        index = 0
        for i in command:
            try:
               self.telnet_write(self.vargain_axis_disc + "[0]" + "[" + str(index) + "]" + "=" + i)
               index += 1

            except ValueError:
                return False

    def write_gainset_description(self, command):
        index = 0
        for i in command:
            try:
               self.telnet_write(self.vargain_axis_disc + "[0]" + "[" + str(index) + "]" + "=" + i)
               index += 1

            except:
                return False

    def write_single_axis_description(self, command, axis_set):
        try:
            self.telnet_write(self.vargain_axis_disc + axis_set + "=" + command)

        except:
            return False

    def read_single_axis_description(self, axis_set):
        try:
           result = self.telnet_write_read("?" + self.vargain_axis_disc + axis_set)
        except ValueError:
            return False

        return result

    def enable_vargains(self):
        try:
            result = self.telnet_write_read(self.vargain_enable + "=1")
        except ValueError:
            return False

        return result

    def disable_vargains(self):
        try:
            result = self.telnet_write_read(self.vargain_enable + "=0")
        except ValueError:
            return False

        return result

    def execute_vargains(self):

        try:
            result = self.telnet_write_read(self.__execute_vargains + "=1")
        except ValueError:
            return False
        return result

    def dis_execute_vargains(self):
        try:
            result = self.telnet_write_read(self.__execute_vargains + "=0")
        except ValueError:
            return False
        return result

    def read_axis_wrn_status(self):
        st1 = []
        for i in range(4):
            try:
                result = self.telnet_write_read("status" + " " + str(i + 1))
                # print(result)
                result = result[result.find("Active Warnings") + len("Active Warnings") + 1:result.find("PFB")]
                st1.append(result)
                # print(result)
            except ValueError:
                return False
        # print(st1)
        return st1

    def wrn_status(self):
        result = []
        for i in range(4):
            try:
                result.append(self.telnet_write_read("?wrn.exist" + "[" + str(i + 1) + "]"))
            except ValueError:
                return False
        return result

    def connect_cs(self):
        # self._mc_project = Selector.Home(self.ip, self.path, self.user, self.password)
        self.open_cs()

    def read_pfac_from_terminal(self):
        result = []
        self.open_panel_terminal()
        for i in range(4):
            result.append(self.write_panel_terminal("?a" + str(i+1) + ".pfac"))
        self.press_close_terminal()
        return result

    def read_gear_feed(self):
        self.open_panel_terminal()
        pnum_2 = float(self.write_panel_terminal("?ec_sdo_read(1,0x6091,2)"))
        pnum_1 = float(self.write_panel_terminal("?ec_sdo_read(1,0x6091,1)"))
        pden_2 = float(self.write_panel_terminal("?ec_sdo_read(1,0x6092,2)"))
        pden_1 = float(self.write_panel_terminal("?ec_sdo_read(1,0x6092,1)"))

        self.press_close_terminal()
        return (pden_2/pden_1)*(pnum_2/pnum_1)

    def read_direction(self):
        result = []
        self.open_panel_terminal()
        for i in range(4):
            result.append(self.write_panel_terminal("?a" + str(i + 1) + ".direction"))
        self.press_close_terminal()
        return result

    def read_posfactor_from_drive(self):
        result = []
        for i in range(4):
            try:
                result.append(self.telnet_write_read("?vargains.axis.posfactor" + "[" + str(i + 1) + "]"))
            except ValueError:
                return False
        return result

    def read_coupling_factor_from_drive(self):
        result = []
        for i in range(4):
            for j in range(4):
                try:
                    result.append(self.telnet_write_read("?vargains.axis.cplg" + "[" + str(i+1) + "]" +
                                                                  "[" + str(j) + "]"))
                except ValueError:
                    return False
        return result

    def read_coupling_factor_from_mc(self):
        result = []
        self.open_panel_terminal()
        for i in range(4):
            for j in range(4):
                try:
                    result.append(self.write_panel_terminal(
                        "?cplg" + "[" + str(i+1) + "]" + "[" + str(j+1) + "]"))
                except ValueError:
                    return False
        self.press_close_terminal()
        return result

    def read_cntrl_act_params_from_drive(self):
        result = []
        result1 = []
        w, h = 4, len(self.actual_gains_params)
        matrix = [[0 for k in range(w)] for d in range(h)]
        count = 0

        for parameter in self.actual_gains_params:
            for i in range(4):
                try:
                    result.append(self.telnet_write_read("?" + parameter + "[" + str(i+1) + "]"))
                    result1.append(self.telnet_write_read("?" + parameter + "[" + str(i + 1) + "]"))

                except ValueError:
                    return False
            matrix[count][:] = result1
            result1 = []
            count += 1

        return matrix

    def read_cntrl_params_from_drive(self, num_gainset):
        result = []
        w, h = 4, len(self.gains_params)
        matrix = [[0 for k in range(w)] for d in range(h)]
        count = 0
        for parameter in self.gains_params:
            for i in range(4):
                try:
                    # print("?" + parametr + "[" + str(i+1) + "]" + "[" + str(num_gainset) + "]")
                    result.append(self.telnet_write_read("?" + parameter + "[" + str(i+1) + "]" + "[" + str(num_gainset)
                                                         + "]"))

                except ValueError:
                    return False

            matrix[count][:] = result
            result = []
            count += 1

        return matrix

    def perform_execute(self):
        for i in range(4):
            try:
                self.telnet_write_read(self.__cntrl_execute + "["+str(i+1)+"]=1")
            except ValueError:
                return False
        self.telnet_write_read(self.__execute_vargains + "=1")

    def __write_params2drive(self, num_axis, display_out):

        path = self.path_params + '\\axis' + str(num_axis) + '.txt'
        datafile = open(path, 'r')
        stringfiles = datafile.read()
        split_data = stringfiles.split("\n")
        if display_out:
            print(split_data)
        for i in split_data:
            self.telnet_write_read("s " + str(i))

        self.perform_execute()
        if display_out:
            print(self.wrn_status())

    def __write_part_configuration_gainset2drive(self):

        datafile = open(self.path_part_config, 'r')
        stringfiles = datafile.read()
        split_data = stringfiles.split("\n")
        print(split_data)
        for i in split_data:
            self.telnet_write_read("s " + str(i))

        self.perform_execute()
        print(self.wrn_status())

    def __write_full_configuration_gainset2drive(self):
        datafile = open(self.path_full_config, 'r')
        stringfiles = datafile.read()
        split_data = stringfiles.split("\n")
        print(split_data)
        for i in split_data:
            self.telnet_write_read("s " + str(i))

        self.perform_execute()
        print(self.wrn_status())

    def write2drive_params_and_full_config(self, display_out):
        try:
            for axis in range(4):
                self.__write_params2drive(axis+1, display_out)
            self.__write_full_configuration_gainset2drive()
            return True
        except:
            return False

