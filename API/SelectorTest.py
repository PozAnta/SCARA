import unittest
from API import Selector


class TestHome(unittest.TestCase):

    def setUp(self):
        self.home = Selector.Home("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")
        self.home.open_cs()

    def test_power_button(self):
        self.assertTrue(self.home.driver.find_element_by_xpath('//*[@id="container"]/mat-toolbar/div/div[2]/button')
                         .is_displayed())

    def test_write_terminal(self):
        self.assertTrue(self.home.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                          'mat-sidenav-content/div/div/home-screen/div/mat-grid-list/'
                                                          'div/mat-grid-tile[2]/figure/mat-card/terminal/div/div/'
                                                          'div[2]/div[2]/textarea').is_displayed())

    def test_read_terminal(self):
        self.assertTrue(self.home.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/mat-sidenav-content/'
                                                     'div/div/home-screen/div/mat-grid-list/div/mat-grid-tile[2]/'
                                                     'figure/mat-card/terminal').is_displayed())

    def tearDown(self):
        self.home.close_cs()


if __name__ == '__main__':
    unittest.main()
