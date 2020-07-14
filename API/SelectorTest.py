import unittest
from API import Selector
from API import Address


class TestHome(unittest.TestCase):

    def setUp(self):
        self.obj = Selector.Home("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")
        self.obj.open_cs()
        # comment

    def test_power_button(self):
        self.assertTrue(self.obj.driver.find_element_by_xpath(Address.HomeSection().power_button_addr()).is_displayed())

    def test_write_terminal(self):
        self.assertTrue(
            self.obj.driver.find_element_by_xpath(Address.HomeSection().write_terminal_addr()).is_displayed())

    def test_read_terminal(self):
        self.assertTrue(
            self.obj.driver.find_element_by_xpath(Address.HomeSection().read_terminal_addr()).is_displayed())

    def tearDown(self):
        self.obj.close_cs()


class TestProjectEditor(unittest.TestCase):

    def setUp(self):
        self.project = Selector.ProjectEditor("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")
        self.project.open_cs()

    def test_open_panel_terminal(self):
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection()
                                                                  .open_panel_terminal_addr()).is_displayed())

    def test_write_panel_terminal(self):
        self.project.open_panel_terminal()
        self.assertTrue(self.project.driver.driver.find_element_by_xpath(Address.ProjectEditorSection()
                                                                         .write_panel_terminal_addr()).is_displayed())

    def test_close_terminal(self):
        self.project.open_panel_terminal()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection()
                                                                  .press_close_terminal_addr()).is_displayed())

    def test_project_editor(self):
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().project_editor_addr())
                        .is_displayed())

    def test_apps_folder(self):
        self.project.project_editor()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().apps_folder_addr())
                        .is_displayed())

    def test_adpt_folder(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().adpt_folder_addr())
                        .is_displayed())

    def test_prog_adpt_folder(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection()
                                                                  .prog_adpt_folder_addr()).is_displayed())

    def test_save_and_load(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.project.adpt_folder()

        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().save_and_load_addr())
                        .is_displayed())

    def test_run_programm(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.project.adpt_folder()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().run_programm_addr())
                        .is_displayed())

    def test_kill_unload(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.project.adpt_folder()

        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().kill_unload_addr())
                        .is_displayed())

    def test_io_mapping(self):
        self.project.project_editor()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().io_mapping_addr())
                        .is_displayed())

    def test_maxx_io(self):
        self.project.project_editor()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().maxx_io_addr())
                        .is_displayed())

    def test_maxx_inputs(self):
        self.project.project_editor()
        self.project.maxx_io()
        self.assertTrue(
            self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().maxx_inputs_addr())
                .is_displayed())

    def test_maxx_outputs(self):
        self.project.project_editor()
        self.project.maxx_io()
        self.assertTrue(self.project.driver.find_element_by_xpath(Address.ProjectEditorSection().maxx_outputs_addr())
                        .is_displayed())

    def tearDown(self):
        self.project.close_cs()


if __name__ == '__main__':
    unittest.main()
