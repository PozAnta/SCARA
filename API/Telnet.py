import telnetlib


class TelComm:

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        self.tn = telnetlib.Telnet(self.ip, self.port, timeout=5)
        self.communication_count_attempt = 10

    def __write(self, cmd):
        self.tn.write(bytes(cmd + "\n", 'ascii'))

    def write(self, cmd):
        self.__write(cmd)

    def read(self, cmd):
        self.__read(cmd)

    def __read(self, cmd):

        while True:
            value = ""
            if self.communication_count_attempt < 0:
                break

            x = self.tn.read_until(bytes('->', 'ascii'), 5)
            st1 = str(x)
            st1_split = st1.split("\\n\\r\\n")
            command = (st1_split[0])[2:len(st1_split[0])]

            for i in range(1, len(st1_split), 1):
                value += (st1_split[i])[:len(st1_split[i])]

            if command == cmd:
                break
            else:
                self.communication_count_attempt -= 1

        if value.find("-->") != -1:
            value = value[:value.find("-->")]

        value = value.replace("\\n", "")
        value = value.replace("\\r", "")

        return value

    def write_read(self, cmd):
        self.__write(cmd)
        return self.__read(cmd)

    def close(self):
        self.tn.close()


# obj = TelComm("192.168.57.100", 4000)
# result = obj.write_read("save")
# print(result)
# print(result[result.find("Active Warnings") + len("Active Warnings") + 1:result.find("PFB")])
