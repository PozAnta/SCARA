import time
from API import PortSerial, Telnet, Selector
from Provider import CommProvide


class EnableDisable:

    def __init__(self, ip, path, user, password):
        self.ip = ip
        self.path = path
        self.user = user
        self.password = password
        self.serial_port = "COM4"
        self.home = Selector.Home(self.ip, self.path, self.user, self.password)
        self.proj_editor = Selector.ProjectEditor(self.ip, self.path, self.user, self.password)
        self.tel_comm = CommProvide.CommunicationTelnet()
        self.serial_comm = CommProvide.CommunicationSerial(self.serial_port)

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
