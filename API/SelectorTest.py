import unittest
from API import Selector
from API import Address


class TestHome(unittest.TestCase):

    def setUp(self):
        self.obj = Selector.Home("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")
        self.obj.open_cs()
        # comment

    def test_power_button(self):
        # address = Address.HomeSection()
        self.assertTrue(self.obj.driver.find_element_by_xpath('').is_displayed())

    def test_write_terminal(self):
        self.assertTrue(self.obj.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                               'mat-sidenav-content/div/div/home-screen/div/mat-grid'
                                                               '-list/ '
                                                               'div/mat-grid-tile[2]/figure/mat-card/terminal/div/div/'
                                                               'div[2]/div[2]/textarea').is_displayed())

    def test_read_terminal(self):
        self.assertTrue(
            self.obj.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/mat-sidenav-content/'
                                                   'div/div/home-screen/div/mat-grid-list/div/mat-grid-tile[2]/'
                                                   'figure/mat-card/terminal').is_displayed())

    def tearDown(self):
        self.obj.close_cs()


class TestProjectEditor(unittest.TestCase):

    def setUp(self):
        self.project = Selector.ProjectEditor("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")
        self.project.open_cs()

    def test_open_panel_terminal(self):
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-toolbar/div/button[7]').
                        is_displayed())

    def test_write_panel_terminal(self):
        self.project.open_panel_terminal()
        self.assertTrue(self.project.driver.driver.find_element_by_xpath('//*[@id="container"]/div['
                                                                         '2]/terminal-window/terminal/ '
                                                                         'div/div/div[2]/div[2]/textarea')
                        .is_displayed())

    def test_close_terminal(self):
        self.project.open_panel_terminal()
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/button/'
                                                                  'span/mat-icon').is_displayed())

    def test_project_editor(self):
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                                  'mat-sidenav/div/main-menu/div/ul/li[4]/mat-icon')
                        .is_displayed())

    def test_apps_folder(self):
        self.project.project_editor()
        self.assertTrue(self.project.driver.driver.find_element_by_xpath('//*[@id="Apps"]/div/mat-icon[2]')
                        .is_displayed())

    def test_adpt_folder(self):
        self.project.project_editor()
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="App-ADPT_CYL"]/div/mat-icon[2]')
                        .is_displayed())

    def test_prog_adpt_folder(self):
        self.project.project_editor()
        self.project.apps_folder()

        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="App-ADPT_CYL-ul"]/mat-tree-node[1]/li/'
                                                                  'div/mat-icon').is_displayed())

    def test_save_and_load(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.project.adpt_folder()

        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                                  'mat-sidenav-content/div/div/program-editor/'
                                                                  'div/as-split/as-split-area[2]/as-split/'
                                                                  'as-split-area[1]/div[2]/div/div/img[1]')
                        .is_displayed())

    def test_run_programm(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.project.adpt_folder()
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                                  'mat-sidenav-content/div/div/program-editor/div/'
                                                                  'as-split/as-split-area[2]/as-split/as-split-area[1]/'
                                                                  'div[2]/div/div/mat-icon[2]').is_displayed())

    def test_kill_unload(self):
        self.project.project_editor()
        self.project.apps_folder()
        self.project.adpt_folder()

        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                                  'mat-sidenav-content/div/div/program-editor/div/as'
                                                                  '-split/ '
                                                                  'as-split-area[2]/as-split/as-split-area[1]/div['
                                                                  '2]/div/div/ '
                                                                  'mat-icon[1]').is_displayed())

    def test_io_mapping(self):
        self.project.project_editor()
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                                  'mat-sidenav-content/div/div/program-editor/div/'
                                                                  'as-split/as-split-area[1]/program-editor-side-menu/'
                                                                  'div/div/mat-tree/mat-tree-node[6]/li/div/mat-icon')
                        .is_displayed())

    def test_maxx_io(self):
        self.project.project_editor()
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/mat'
                                                                  '-sidenav-content/ '
                                                                  'div/div/program-editor/div/as-split/as-split-area['
                                                                  '2]/as-split/ '
                                                                  'as-split-area/io-mapping/div/as-split/as-split'
                                                                  '-area[1]/mat-tree/ '
                                                                  'mat-nested-tree-node[2]/li/div/mat-icon')
                        .is_displayed())

    def test_maxx_inputs(self):
        self.project.project_editor()
        self.project.maxx_io()
        self.assertTrue(
            self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/mat-sidenav-content/'
                                                      'div/div/program-editor/div/as-split/as-split-area[2]/as-split/'
                                                      'as-split-area/io-mapping/div/as-split/as-split-area[1]/'
                                                      'mat-tree/mat-nested-tree-node[2]/li/ul/mat-tree-node[1]/li')
                .is_displayed())

    def test_maxx_outputs(self):
        self.project.project_editor()
        self.project.maxx_io()
        self.assertTrue(self.project.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                                  'mat-sidenav-content/'
                                                                  'div/div/program-editor/div/as-split/as-split-area['
                                                                  '2]/as-split/ '
                                                                  'as-split-area/io-mapping/div/as-split/as-split'
                                                                  '-area[1]/ '
                                                                  'mat-tree/mat-nested-tree-node['
                                                                  '2]/li/ul/mat-tree-node[2]/li').is_displayed())

    def tearDown(self):
        self.project.close_cs()


if __name__ == '__main__':
    unittest.main()
