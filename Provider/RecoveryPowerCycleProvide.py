import time
from Provider import EnableDisableProvide


class RecoveryPowerCycle(EnableDisableProvide):

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

