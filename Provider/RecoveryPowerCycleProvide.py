import time
from Provider import EnableDisableProvide
from Provider import CommProvide


class Support(EnableDisableProvide):
    def __init__(self, name_ser_port):
        self.enable_disable = EnableDisableProvide.EnableProvide()
        self.serial_comm = CommProvide.CommunicationSerial(name_ser_port)


class RecoveryPowerCycle(Support):

    def connect(self):
        self.enable_disable.connect()

    def disconnect(self):
        self.enable_disable.disconnect()

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


objj = RecoveryPowerCycle()
