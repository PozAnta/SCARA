from API import PortSerial, Telnet, Selector


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


class CommunicationSerial:

    def __init__(self, port):
        self.port = port
        self.serial = PortSerial

    def write_serial(self, cmd):
        self.serial.port(cmd, self.port, 1)

    def write_read_serial(self, cmd):
        return self.serial.port(cmd, self.port, 1)