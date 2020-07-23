from API import Selector
from colorama import Fore
from configparser import ConfigParser
from Provider import CommProvide


class Support:
    def __init__(self, ip, path, user, password):
        self.ip = ip
        self.path = path
        self.user = user
        self.password = password
        self.serial_port = "COM4"

        config = ConfigParser()
        config.read('C:\\Python\\Robot\\Scara\\Tests\\VariableGains\\Script\\configurator.ini')

        self.path_full_config = config.get('PathFullConfig', 'Path')
        self.path_part_config = config.get('PathPartConfig', 'Path')
        self.path_negative_full_config = config.get('PathNegativeFull', 'Path')
        self.path_params = config.get('PathParameters', 'Path')

        # self._mc_project = Selector.Home(self.ip, self.path, self.user, self.password)
        self.mc_script = Selector.ProjectEditor(self.ip, self.path, self.user, self.password)
        self.system = Selector.SystemConfigurator(self.ip, self.path, self.user, self.password)
        self.tel_comm = CommProvide.CommunicationTelnet()

        self.vargain_axis_disc = config.get('VarGainAxisDescription', 'Name')
        self.vargain_gainset_disc = config.get('VarGainGainsetDescription', 'Name')
        self.vargain_enable = config.get('VarGainEnable', 'Name')
        self.__execute_vargains = config.get('VarGainExecute', 'Name')
        self.__cntrl_execute = config.get('VarGainCntrExecute', 'Name')

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

    def disconnect_cs(self):
        self.mc_script.close_cs()

    def connect_cs(self):
        self.system.open_cs()


class Config(Support):
    def disactivate_inuse_gainset(self, number_gainset):
        try:
            self.tel_comm.telnet_write("vargains.inuse[0][" + str(number_gainset) + "] = 0")
        except ValueError:
            print("Wrong responce")

    def activate_inuse_gainset(self, number_gainset):
        try:
            self.tel_comm.telnet_write("vargains.inuse[0][" + str(number_gainset) + "] = 1")
        except ValueError:
            print("Wrong responce")

    def __read_write_config_parser(self, use_configuration):
        datafile = open(use_configuration, 'r')
        stringfiles = datafile.read()
        split_data = stringfiles.split("\n")
        # print(split_data)
        for i in split_data:
            self.tel_comm.telnet_write_read("s " + str(i))

    def write_negative_full_config(self):
        self.__read_write_config_parser(self.path_negative_full_config)

    def enable_vargains(self):
        try:
            result = self.tel_comm.telnet_write_read(self.vargain_enable + "=1")
        except ValueError:
            return False

        return result

    def disable_vargains(self):
        try:
            result = self.tel_comm.telnet_write_read(self.vargain_enable + "= 0")
        except ValueError:
            return False

        return result

    def execute_vargains(self):

        try:
            result = self.tel_comm.telnet_write_read(self.__execute_vargains + "=1")
        except ValueError:
            return False
        return result

    def dis_execute_vargains(self):
        try:
            result = self.tel_comm.telnet_write_read(self.__execute_vargains + "=0")
        except ValueError:
            return False
        return result

    def perform_execute(self):
        for i in range(4):
            try:
                self.tel_comm.telnet_write_read(self.__cntrl_execute + "[" + str(i + 1) + "]=1")
            except ValueError:
                return False
        self.tel_comm.telnet_write_read(self.__execute_vargains + "=1")

    def __write_params2drive(self, num_axis):

        path = self.path_params + '\\axis' + str(num_axis) + '.txt'
        datafile = open(path, 'r')
        stringfiles = datafile.read()
        split_data = stringfiles.split("\n")

        for i in split_data:
            self.tel_comm.telnet_write_read("s " + str(i))

        self.perform_execute()

    def __write_part_configuration_gainset2drive(self):

        datafile = open(self.path_part_config, 'r')
        stringfiles = datafile.read()
        split_data = stringfiles.split("\n")
        # print(split_data)
        for i in split_data:
            self.tel_comm.telnet_write_read(str(i))

        self.perform_execute()
        # print(self.wrn_status())

    def __write_full_configuration_gainset2drive(self):
        datafile = open(self.path_full_config, 'r')
        stringfiles = datafile.read()
        split_data = stringfiles.split("\n")
        # print(split_data)
        for i in split_data:
            self.tel_comm.telnet_write_read("s " + str(i))

        self.perform_execute()
        # print(self.wrn_status())

    def write2drive_params_and_full_config(self):
        try:
            for axis in range(4):
                print(Fore.LIGHTBLUE_EX + "Set parameters for axis " + str(axis + 1))
                self.__write_params2drive(axis + 1)
            self.__write_full_configuration_gainset2drive()
            return True
        except:
            return False

    def write2drive_params_and_part_config(self):
        try:
            for axis in range(4):
                print(Fore.LIGHTBLUE_EX + "Set parameters for axis " + str(axis + 1))
                self.__write_params2drive(axis + 1)
            self.__write_part_configuration_gainset2drive()
            return True
        except:
            return False


class Description(Support):
    def write_single_axis_description(self, command, axis_set):
        try:
            self.tel_comm.telnet_write(self.vargain_axis_disc + "[0][" + str(axis_set) + "]=" + command)

        except:
            return False

    def read_single_axis_description(self, axis_set):
        try:
            result = self.tel_comm.telnet_write_read("?" + self.vargain_axis_disc + axis_set)
        except ValueError:
            return False

        return result

    def write_single_gainset_description(self, command, gainset_set):
        try:
            self.tel_comm.telnet_write(self.vargain_gainset_disc + "[0][" + str(gainset_set) + "]=" + command)

        except:
            return False

    '''
    def write_axis_description(self, command):
        index = 0
        for i in command:
            try:
                self.tel_comm.telnet_write(self.vargain_axis_disc + "[0]" + "[" + str(index) + "]" + "=" + i)
                index += 1

            except ValueError:
                return False

    def write_gainset_description(self, command):
        index = 0
        for i in command:
            try:
                self.tel_comm.telnet_write(self.vargain_axis_disc + "[0]" + "[" + str(index) + "]" + "=" + i)
                index += 1

            except:
                return False
    '''


class ReadData(Support):
    def wrn_status(self):
        result = []
        for i in range(4):
            try:
                result.append(self.tel_comm.telnet_write_read("?wrn.exist" + "[" + str(i + 1) + "]"))
            except ValueError:
                return False
        return result

    def read_axis_description(self):
        result = []
        for i in range(4):
            try:
                result.append(
                    self.tel_comm.telnet_write_read("?" + self.vargain_axis_disc + "[0]" + "[" + str(i) + "]"))
            except ValueError:
                return result
        return result

    def read_drive_version(self):
        return self.tel_comm.telnet_write_read("?ver")

    def read_offset_mastering(self):
        result = []
        self.system.open_panel_terminal()
        for i in range(4):
            result.append(self.mc_script.write_panel_terminal("?a" + str(i + 1) + ".disp"))
        self.mc_script.press_close_terminal()
        return result

    def read_gainset_from_drive(self):
        try:
            return self.tel_comm.telnet_write_read("?vargains.active")
        except:
            print("Something wrong when trying to read from drive")

    def read_axis_wrn_status(self):
        st1 = []
        for i in range(4):
            try:
                result = self.tel_comm.telnet_write_read("status" + " " + str(i + 1))
                # print(result)
                result = result[result.find("Active Warnings") + len("Active Warnings") + 1:result.find("PFB")]
                st1.append(result)
                # print(result)
            except ValueError:
                return False
        # print(st1)
        return st1

    def read_pfac_from_terminal(self):
        result = []
        self.mc_script.open_panel_terminal()
        for i in range(4):
            result.append(self.mc_script.write_panel_terminal("?a" + str(i + 1) + ".pfac"))
        self.mc_script.press_close_terminal()
        return result

    def read_gear_feed(self):
        self.mc_script.open_panel_terminal()
        pnum_2 = float(self.mc_script.write_panel_terminal("?ec_sdo_read(1,0x6091,2)"))
        pnum_1 = float(self.mc_script.write_panel_terminal("?ec_sdo_read(1,0x6091,1)"))
        pden_2 = float(self.mc_script.write_panel_terminal("?ec_sdo_read(1,0x6092,2)"))
        pden_1 = float(self.mc_script.write_panel_terminal("?ec_sdo_read(1,0x6092,1)"))

        self.mc_script.press_close_terminal()
        return (pden_2 / pden_1) * (pnum_2 / pnum_1)

    def read_direction(self):
        result = []
        self.mc_script.open_panel_terminal()
        for i in range(4):
            result.append(self.mc_script.write_panel_terminal("?a" + str(i + 1) + ".direction"))
        self.mc_script.press_close_terminal()
        return result

    def read_posfactor_from_drive(self):
        result = []
        for i in range(4):
            try:
                result.append(self.tel_comm.telnet_write_read("?vargains.axis.posfactor" + "[" + str(i + 1) + "]"))
            except ValueError:
                return False
        return result

    def read_coupling_factor_from_drive(self):
        result = []
        for i in range(4):
            for j in range(4):
                try:
                    result.append(self.tel_comm.telnet_write_read("?vargains.axis.cplg" + "[" + str(i + 1) + "]" +
                                                                  "[" + str(j) + "]"))
                except ValueError:
                    return False
        return result

    def read_coupling_factor_from_mc(self):
        result = []
        self.mc_script.open_panel_terminal()
        for i in range(4):
            for j in range(4):
                try:
                    result.append(self.mc_script.write_panel_terminal(
                        "?cplg" + "[" + str(i + 1) + "]" + "[" + str(j + 1) + "]"))
                except ValueError:
                    return False
        self.mc_script.press_close_terminal()
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
                    result.append(self.tel_comm.telnet_write_read("?" + parameter + "[" + str(i + 1) + "]"))
                    result1.append(self.tel_comm.telnet_write_read("?" + parameter + "[" + str(i + 1) + "]"))

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
                    result.append(
                        self.tel_comm.telnet_write_read(
                            "?" + parameter + "[" + str(i + 1) + "]" + "[" + str(num_gainset)
                            + "]"))

                except ValueError:
                    return False

            matrix[count][:] = result
            result = []
            count += 1

        return matrix


class WriteData(Support):
    def write_offset_mastering_for_all_axis(self, arr_offset):
        self.system.open_system_configurator()
        self.system.open_system()

        self.system.write_axis1_offset(arr_offset[0])
        self.system.write_axis2_offset(arr_offset[1])
        self.system.write_axis3_offset(arr_offset[2])
        self.system.write_axis4_offset(arr_offset[3])

    def write_offset_mastering_for_one_axis(self, axis, value):
        self.system.open_system_configurator()
        self.system.open_system()
        if int(axis) == 1:
            self.system.write_axis1_offset(str(value))
        if int(axis) == 2:
            self.system.write_axis2_offset(str(value))
        if int(axis) == 3:
            self.system.write_axis3_offset(str(value))
        if int(axis) == 4:
            self.system.write_axis4_offset(str(value))

    def set_drive_payload(self, payload_value):
        try:
            self.tel_comm.telnet_write("vargains.payload = " + str(payload_value))
        except ValueError:
            print("Wrong responce")


class VariableGains():
    def __init__(self):
        self.descript = Description()






