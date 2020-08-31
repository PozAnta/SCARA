from Provider import CommProvide
import time
import matplotlib.pyplot as plt
import requests


class RecordMc:

    def __init__(self, points, gap):

        self.points = points
        self.gap = gap
        self.rec = CommProvide.Main("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")

    def start_record(self):
        pass


class RecordDrive:
    def __init__(self, ip, points, gap, prepoints, rec_params, rec_trigger, file_name):

        self.ip = ip
        self.points = points
        self.recoffs = prepoints
        self.gap = gap
        self.rec_params = rec_params
        self.file_name = file_name
        self.trigger = rec_trigger
        self.rec = CommProvide.CommunicationTelnet()

    def __start_record(self):
        self.rec.telnet_write("recoff")
        self.rec.telnet_write("recoff")
        self.rec.telnet_write("recoffs " + str(self.recoffs))
        self.rec.telnet_write("recgap " + str(self.gap))
        self.rec.telnet_write("rectrig " + self.trigger)
        print("Start record")
        record_string = ""
        for i in self.rec_params:
            record_string = record_string + str(i) + " "
        self.rec.telnet_write("record " + str(self.points) + " " + record_string)

        while True:
            # self.rec.telnet_write("recdone")
            read = self.rec.telnet_write_read("recdone")
            sring = read[read.index("Message") + len("Message") + 3: len(read) - 2]

            if sring.find("Complete") != -1:
                # print(sring)
                break
            time.sleep(1)
        print("Close record")
        self.rec.telnet_write("recordclose " + self.file_name)
        time.sleep(10)

    def __get_data_record(self):
        file_url = "http://" + self.ip + ":1207/drive/api/file/2:" + self.file_name + "?ip=192.168.57.100"
        # print(file_url)
        file_name = requests.get(file_url)
        # print(file_name)
        data = file_name.text
        # print(data)
        # print(data.find(self.rec_params))
        index = data.find(self.rec_params[len(self.rec_params)-1])
        data = data[index:]
        data = data[data.find("trigger") + len("trigger") + 1:]
        slit_data = data.split(",")
        # print(slit_data)
        w, h = len(self.rec_params), self.points
        matrix = [[0 for k in range(w)] for d in range(h)]
        filled_data_arr_1 = []
        fill_index_data = 0
        indx_first_param = []

        counter = 0
        offset = len(self.rec_params)*2 + 2

        data_error_counter = 0
        for koko in range(len(self.rec_params)):
            indx_first_param.append(fill_index_data)
            fill_index_data += 2

        for j in range(len(self.rec_params)):

            for i in range(0, int(self.points), 1):
                try:
                    filled_data_arr_1.append(float(slit_data[indx_first_param[j] + counter].replace("\n", " ")))
                    counter += offset

                except ValueError:
                    print("Value error!!!")
                    data_error_counter += 1
                    pass
                except IndexError:
                    print("Index Error!!!")
                    break

            matrix[j][:] = filled_data_arr_1
            # print(filled_data_arr_1)
            filled_data_arr_1 = []
            counter = 0
            plt.plot(matrix[j][:])

        print("Done! : Error counter: " + str(data_error_counter))
        plt.ylabel('[Counts]')
        plt.show()

    def record_and_plot(self):
        self.__start_record()
        self.__get_data_record()

    def __get_plot(self):
        self.__get_data_record()


arr = ["ptpvcmd[1]", "vact[1]", "icmd[1]", "fb.ecat.control[1]"]
obj = RecordDrive("192.168.0.1", 2000, 8, 10, arr, "en[1] == 0", "ref.csv")
obj.record_and_plot()
