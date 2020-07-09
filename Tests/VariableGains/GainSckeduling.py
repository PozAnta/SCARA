from Provider import Provide
from colorama import Fore, Style


class Main:

    def __init__(self, name_test="NA"):

        self.test = Provide.VariableGains("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")
        # self.test.connect_cs()
        self.name_test = name_test
        self.status = True

        self.warnings = ["(4202242)",
                         "(4202241)"]

        self.decsription = [
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis1\",\"AxisState\":[\"axis1_full;-130;130\"],\""
            "AxisUnits\":\"Deg\"}",
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis2\",\"AxisState\":[\"axis2_full;-140;140\"],\""
            "AxisUnits\":\"Deg\"}",
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis3\",\"AxisState\":[\"axis3_full;-170;40\"],\""
            "AxisUnits\":\"mm\"}",
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis4\",\"AxisState\":[\"axis4_full;-370;370\"],\""
            "AxisUnits\":\"Deg\"}"]

        self.decsription_neg = [
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis1\",\"AxisState\":[\"axis1_full;-130;110\"],\""
            "AxisUnits\":\"Deg\"}",
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis2\",\"AxisState\":[\"axis1_full;-140;140\"],\""
            "AxisUnits\":\"Deg\"}",
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis3\",\"AxisState\":[\"axis1_full;-150;10\"],\""
            "AxisUnits\":\"mm\"}",
            "{\"SystemType\":\"SCARA\",\"AxisName\":\"axis4\",\"AxisState\":[\"axis1_full;-360;360\"],\""
            "AxisUnits\":\"Deg\"}"]

        self.gainset_desc = ["{\"axis1\":\"axis1_full\",\"axis2\":\"axis2_full\",\"axis3\":\"axis3_full\",\"axis4\":\""
                             "axis4_full\",\"Payload\":\"0.0\"}",
                             "{\"axis1\":\"axis1_full\",\"axis2\":\"axis2_full\",\"axis3\":\"axis3_full\",\"axis4\":\""
                             "axis4_full\",\"Payload\":\"3.0\"}",
                             "{\"axis1\":\"axis1_full\",\"axis2\":\"axis2_full\",\"axis3\":\"axis3_full\",\"axis4\":\""
                             "axis4_full\",\"Payload\":\"6.0\"}"]

        self.negative_gainset_desc = [
            "{\"axis1\":\"axis1_full\",\"axis22\":\"axis2_full\",\"axis3\":\"axis3_full\",\"axis4\":\"axis4_full\","
            "\"Payload\":\"0.0\"}",
            "{\"axis1\":\"axis1_full\",\"axis22\":\"axis2_full\",\"axis3\":\"axis3_full\",\"axis4\":\"axis4_full\","
            "\"Payload\":\"3.0\"}",
            "{\"axis1\":\"axis1_full\",\"axis22\":\"axis2_full\",\"axis3\":\"axis3_full\",\"axis4\":\"axis4_full\","
            "\"Payload\":\"6.0\"}"]


class Support(Main):

    def change_description_axis(self):
        print(Fore.LIGHTBLUE_EX + "  --> Check that vargains.axis.desc is writable")
        end_status = True
        print(Fore.LIGHTBLUE_EX + "  --> Read saved values vargains.axis.desc")
        save_result = self.test.read_axis_description()
        print(Fore.LIGHTBLUE_EX + "  --> Write changed values to drive")
        self.test.write_axis_description(self.decsription)
        print(Fore.LIGHTBLUE_EX + "  --> Read changed values from drive")
        result = self.test.read_axis_description()
        count = 0
        print(Fore.LIGHTBLUE_EX + "\t\t--> Compare values from drive to sanded")
        for i in result:
            if i.find(self.decsription[count]) != -1:
                print(Fore.GREEN + "\t\t\t--Compare vargains.axis.desc with read value PASS--")
                print(i)
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "\t\t\t--Compare vargains.axis.desc with read value FAIL--")
                print(i)
                print(Style.RESET_ALL)
                self.status = False

            count += 1

        print(Fore.LIGHTBLUE_EX + "  --> Write saved values vargains.axis.desc")
        self.test.write_axis_description(save_result)

        print(Fore.LIGHTBLUE_EX + "  --> Check status of test writable/readable")
        if end_status:
            print(Fore.GREEN + "    --The check vargains.axis.desc is writable/readable PASS--")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "    --The check vargains.axis.desc is writable/readable FAIL--")
            print(Style.RESET_ALL)
            self.status = False

    def ckeck_description_readable(self):
        print(Fore.LIGHTBLUE_EX + "\t\t--> Check that vargains.axis.desc is readable")
        end_status = True
        result = self.test.read_axis_description()
        for i in result:
            if i.find("SystemType") == -1:
                end_status = False
                print(i)
                break
            else:
                print(i)
                end_status = True

        if end_status:
            print(Fore.GREEN + "\t\t\t\t--The check vargains.axis.desc is readable PASS--")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "\t\t\t\t--The check vargains.axis.desc is readable FAIL--")
            print(Style.RESET_ALL)
            self.status = False

    def negative_description_check(self, result):
        print(Fore.LIGHTBLUE_EX + "  --> Check negative execution status")
        if str(result).find("\"Error\":55,\"") != -1:
            print(result)
            print(Fore.GREEN + "    --The check negative execution PASS--")
            print(Style.RESET_ALL)
        else:
            print(result)
            print(Fore.RED + "    --The check negative execution FAIL--")
            print(Style.RESET_ALL)
            self.status = False

    def check_negative_wrn_status(self, result):
        print(Fore.LIGHTBLUE_EX + "  --> Check negative WRN status for all axis")
        for i in result:

            if str(i).find("GainSet Configuration/Parameters Changed - Execution Needed (4202241)") != -1:
                print(result)
                print(Fore.GREEN + "    --The check negative WRN status PASS--")
                print(Style.RESET_ALL)
            else:
                print(result)
                print(Fore.RED + "    --The check negative WRN status FAIL--")
                print(Style.RESET_ALL)
                self.status = False

    def check_clear_status(self, result):
        print(Fore.LIGHTBLUE_EX + "  --> Check FLT/WRN status for all axis")
        print(Style.RESET_ALL)
        for i in result:

            if int(i) != 0:
                print("Warning(s) are: ", i)
                print(Fore.RED + "    --The check WRN status FAIL--")
                print(Style.RESET_ALL)
                self.status = False
            else:
                print(Fore.GREEN + "    --The check WRN status PASS--")
                print(Style.RESET_ALL)

    def check_posfactor(self, pfac, direction, gear, posfac):
        print(Fore.LIGHTBLUE_EX + "  --> Check that posfactor from drive equivalent to MC")
        position_coefficent = []
        for i in range(len(pfac)):
            position_coefficent.append(float(pfac[i])*float(direction[i])*float(gear))

        count = 0
        for ind in posfac:
            if round(float(ind), 4) == round(position_coefficent[count], 4):
                print(Fore.GREEN + "    --Compare posfactor with read value PASS--")
                print("Measure value: " + str(ind) + " Readed value: " + ind)
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "    --Compare posfactor with read value FAIL--")
                print("Measure value: " + str(ind) + " Readed value: " + ind)
                print(Style.RESET_ALL)
                self.status = False
            count += 1

    def check_cplg(self, cplg_drive, cplg_mc):
        print(Fore.LIGHTBLUE_EX + "  --> Check that cplg from drive equivalent to MC")
        count = 0
        for ind in cplg_mc:
            if round(float(ind), 4) == round(float(cplg_drive[count]), 4):
                print(Fore.GREEN + "    --Compare cplg from MC with cplg from DRIVE value PASS--")
                # print("MC value: " + str(ind) + " Drive value: " + ind)
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "    --Compare cplg from MC with cplg from DRIVE value FAIL--")
                # print("MC value: " + str(ind) + " Drive value: " + ind)
                print(Style.RESET_ALL)
                self.status = False
            count += 1

    def check_params(self):
        print("Actual params: ", self.test.read_cntrl_act_params_from_drive())
        print("Params for gainset 0: ", self.test.read_cntrl_params_from_drive(0))
        print("Params for gainset 1: ", self.test.read_cntrl_params_from_drive(1))
        print("Params for gainset 2: ", self.test.read_cntrl_params_from_drive(2))

    def set_full_range_config(self):
        if self.test.write2drive_params_and_full_config(False):
            print(Fore.GREEN + "Set parameters - OK")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Set parameters - FAIL")
            print(Style.RESET_ALL)


class Test(Support):

    def vargains_description_test(self):
        print(Fore.LIGHTBLUE_EX + "-----Start " + self.name_test + " test----")
        self.ckeck_description_readable()
        # self.change_description_axis()

        # self.test.write_single_axis_description(self.decsription_neg, "[0][4]")
        # print(self.test.read_single_axis_description("[0][4]"))

        if self.status:
            print(Fore.GREEN + "--End " + self.name_test + " test with status PASS--")
        else:
            print(Fore.RED + "--End " + self.name_test + " test with status FAIL--")

        print(Style.RESET_ALL)

    def negative_vargains_axisdesc_axisname_test(self):
        print(Fore.LIGHTBLUE_EX + "-----Start " + self.name_test + " test----")
        # print(Fore.LIGHTBLUE_EX + "  --> Write/update axis description to drive")
        # self.test.write_axis_description(self.decsription_neg)
        # print(Fore.LIGHTBLUE_EX + "  --> Write/update gainset description to drive")
        # self.test.write_gainset_description(self.gainset_desc)
        # # TODO: verify
        # print(Fore.LIGHTBLUE_EX + "  --> Enable variable gains feature")
        # self.test.enable_vargains()
        # print(Fore.LIGHTBLUE_EX + "  --> Execute variable gains feature")
        # self.negative_description_check(self.test.execute_vargains())
        # self.check_negative_wrn_status(self.test.read_axis_wrn_status())
        #
        print(Fore.LIGHTBLUE_EX + "  --> Write/update original axis description to drive")
        self.test.write_axis_description(self.decsription)
        print(Fore.LIGHTBLUE_EX + "  --> Write/update original gainset description to drive")
        self.test.write_gainset_description(self.gainset_desc)
        self.test.execute_vargains()
        self.check_clear_status(self.test.wrn_status())

        if self.status:
            print(Fore.GREEN + "--End " + self.name_test + " test with status PASS--")
        else:
            print(Fore.RED + "--End " + self.name_test + " test with status FAIL--")

        print(Style.RESET_ALL)

    def posfactor_test(self):
        print(Fore.LIGHTBLUE_EX + "-----Start " + self.name_test + " test----")
        print(Fore.LIGHTBLUE_EX + "\t\t--> Perform communication with CS+")
        self.test.connect_cs()

        print(Fore.LIGHTBLUE_EX + "\t\t--> Read pfac value from MC")
        result_pfac = self.test.read_pfac_from_terminal()

        print(Fore.LIGHTBLUE_EX + "\t\t--> Read direction value from MC")
        result_dir = self.test.read_direction()

        print(Fore.LIGHTBLUE_EX + "\t\t--> Read gear feed factor value from MC")
        result_gear = self.test.read_gear_feed()

        print(Fore.LIGHTBLUE_EX + "\t\t--> Read variable.gain.posfactor value from MC")
        drive_posfactor = self.test.read_posfactor_from_drive()
        self.check_posfactor(result_pfac, result_dir, result_gear, drive_posfactor)

        if self.status:
            print(Fore.GREEN + "--End " + self.name_test + " test with status PASS--")
        else:
            print(Fore.RED + "--End " + self.name_test + " test with status FAIL--")

        print(Style.RESET_ALL)

    def cplg_test(self):
        print(Fore.LIGHTBLUE_EX + "-----Start " + self.name_test + " test----")
        print(Fore.LIGHTBLUE_EX + "  --> Perform communication with CS+")
        self.test.connect_cs()
        print(Fore.LIGHTBLUE_EX + "  --> Read cplg value from Drive")
        result_drive = self.test.read_coupling_factor_from_drive()
        print(Fore.LIGHTBLUE_EX + "  --> Read cplg value from MC")
        result_mc = self.test.read_coupling_factor_from_mc()
        self.check_cplg(result_drive, result_mc)

        if self.status:
            print(Fore.GREEN + "--End " + self.name_test + " test with status PASS--")
        else:
            print(Fore.RED + "--End " + self.name_test + " test with status FAIL--")

        print(Style.RESET_ALL)

    def payload_sanity_test(self):
        pass

    def end_effector_sanity_test(self):
        pass

    def offset_test(self):
        pass

    def full_range_payload_low_high_test(self):
        pass

    def full_range_payload_high_low_test(self):
        pass

    def full_range_endeff_low_high_test(self):
        pass

    def full_range_endeff_high_low_test(self):
        pass

    def partial_payload_low_high_test(self):
        pass

    def partial_payload_high_low_test(self):
        pass

    def partial_endeff_low_high_test(self):
        pass

    def partial_endeff_high_low_test(self):
        pass

obj = Test()
obj.posfactor_test()