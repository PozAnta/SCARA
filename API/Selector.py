from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from API.Address import Login
from API.Address import ProjectEditorSection
from API.Address import HomeSection


class Select:

    def __init__(self, ip, path_web_driver, username, password):
        self.cs_username = username
        self.cs_pass = password
        self.path_chrome_driver = path_web_driver
        self.ip = "http://" + ip + ":1207/rs/login"
        self.driver = webdriver.Chrome(self.path_chrome_driver)
        self.login = Login()
        self.pr_edit = ProjectEditorSection()
        self.home = HomeSection()

        self.power_button_obj = ""
        self.terminal_obj = ""

    def open_cs(self):
        self.driver.set_page_load_timeout(50)
        count = 0
        while count < 10:

            try:
                self.driver.get(self.ip)
                time.sleep(10)
                # self.driver.maximize_window()
                self.driver.find_element_by_xpath(self.login.open_cs_addr())
                break
            except NoSuchElementException:
                count += 1
                pass

        username_obj = self.driver.find_element_by_id("username")
        username_obj.send_keys(self.cs_username)

        password_obj = self.driver.find_element_by_id("password")
        password_obj.send_keys(self.cs_pass)

        login_button_obj = self.driver.find_element_by_id("btnLogin")
        login_button_obj.click()

        time.sleep(15)

    def close_cs(self):
        self.driver.close()


class Graph(Select):

    def press_dashboard_button(self):
        dashboard_obj = self.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/mat-sidenav/'
                                                          'div/main-menu/div/ul/li[3]/mat-icon')
        dashboard_obj.click()

        time.sleep(3)

    def press_plus_graph_button(self):
        plus_button_obj = self.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                            'mat-sidenav-content/div/div/dashboard-screen/div/'
                                                            'app-recordings-screen/div/button')
        plus_button_obj.click()

        time.sleep(3)

    def press_selct_graph_selector(self):
        select_graph_obj = self.driver.find_element_by_xpath('//*[@id="mat-select-0"]/div/div[1]/span')
        select_graph_obj.click()

        time.sleep(3)

    def press_graph(self):
        graph_obj = self.driver.find_element_by_xpath('//*[@id="mat-option-1"]/span')
        graph_obj.click()
        time.sleep(3)

    def press_graph_show(self):
        show_graph_obj = self.driver.find_element_by_xpath('//*[@id="mat-dialog-1"]/app-external-graph-dialog/'
                                                           'div/div[2]/button[2]/span')
        show_graph_obj.click()

        time.sleep(5)

    def press_downolad_graph(self):
        download_obj = self.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                         'mat-sidenav-content/div/div/dashboard-screen/div/'
                                                         'app-recordings-screen/div/div/div[1]/button[4]')
        download_obj.click()

        time.sleep(3)


class Jog(Select):

    def open_jog_panel(self):
        jog_panel_obj = self.driver.find_element_by_xpath('//*[@id="container"]/mat-toolbar/div/div[2]/button')
        jog_panel_obj.click()
        time.sleep(3)

    def close_jog_panel(self):
        jog_panel_obj = self.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                          'mat-sidenav-content/div/mat-card/div[1]/button[2]')
        jog_panel_obj.click()
        time.sleep(3)

    def open_jog_control(self):
        control_obj = self.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                        'mat-sidenav-content/div/mat-card/div[1]/button[1]')
        control_obj.click()
        time.sleep(3)

    def slide_jog_velocity(self):
        slide_obj = self.driver.find_element_by_xpath('//*[@id="mat-dialog-6"]/jog-settings-dialog/div/div[1]/'
                                                      'div[2]/p/speed-changer/mat-slider/div/div[2]')
        slide_target = self.driver.find_element_by_xpath('//*[@id="mat-dialog-6"]/jog-settings-dialog/div/'
                                                         'div[1]/div[2]/p/speed-changer/mat-slider/div/div[3]')
        webdriver.ActionChains(self.driver).drag_and_drop(slide_obj, slide_target).perform()

        time.sleep(5)

    def press_j1_negative_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[1]/td[1]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()

        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def press_j1_positive_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[1]/td[3]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()
        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def press_j2_negative_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[2]/td[1]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()
        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def press_j2_positive_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[2]/td[3]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()
        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def press_j3_negative_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[3]/td[1]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()
        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def press_j3_positive_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[3]/td[3]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()
        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def press_j4_negative_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[4]/td[1]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()
        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def press_j4_positive_movement(self, duration):
        j1_negative = self.driver.find_element_by_xpath('//*[@id="jog-container"]/table/tr[4]/td[3]/button')
        webdriver.ActionChains(self.driver).click_and_hold(j1_negative).perform()
        time.sleep(duration)
        webdriver.ActionChains(self.driver).release().perform()
        time.sleep(3)

    def enable_disable_in_jog_panel(self):
        enable_jo_obj = self.driver.find_element_by_xpath('//*[@id="container"]/mat-sidenav-container/'
                                                          'mat-sidenav-content/div/mat-card/div[2]/button')
        enable_jo_obj.click()
        time.sleep(3)


class ProjectEditor(Select):

    def open_panel_terminal(self):
        terminal_onj = self.driver.find_element_by_xpath(self.pr_edit.open_panel_terminal_addr())
        terminal_onj.click()
        time.sleep(3)

    def write_panel_terminal(self, command):
        write_txt_obj = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/terminal-window/terminal/'
                                                          'div/div/div[2]/div[2]/textarea')
        write_txt_obj.send_keys(Keys.ENTER)
        time.sleep(1)
        write_txt_obj.send_keys("clear")
        time.sleep(1)
        write_txt_obj.send_keys(Keys.ENTER)
        time.sleep(1)
        write_txt_obj.send_keys(command)
        time.sleep(1)
        write_txt_obj.send_keys(Keys.ENTER)
        write_txt_obj.send_keys(Keys.ENTER)
        time.sleep(1)

        text_obj = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/terminal-window')
        out = str(text_obj.text)
        out = out[out.find(command) + len(command):]
        out = out[:out.find("-->")]
        # print(out)
        time.sleep(1)
        return out

    def press_close_terminal(self):
        close_term_obj = self.driver.find_element_by_xpath(self.pr_edit.press_close_terminal_addr())
        close_term_obj.click()

        time.sleep(1)

    def apps_folder(self):
        project_editor_obj = self.driver.find_element_by_xpath(self.pr_edit.apps_folder_addr())
        project_editor_obj.click()

    def adpt_folder(self):
        project_editor_obj = self.driver.find_element_by_xpath(self.pr_edit.adpt_folder_addr())
        project_editor_obj.click()

    def prog_adpt_folder(self):
        project_editor_obj = self.driver.find_element_by_xpath(self.pr_edit.prog_adpt_folder_addr())
        project_editor_obj.click()

    def save_and_load(self):
        project_editor_obj = self.driver.find_element_by_xpath(self.pr_edit.save_and_load_addr())
        project_editor_obj.click()

    def run_programm(self):
        project_editor_obj = self.driver.find_element_by_xpath(self.pr_edit.run_programm_addr())
        project_editor_obj.click()

    def kill_unload(self):
        kill_unload_obj = self.driver.find_element_by_xpath(self.pr_edit.kill_unload_addr())
        kill_unload_obj.click()
        time.sleep(3)

    def project_editor(self):
        project_editor_obj = self.driver.find_element_by_xpath(self.pr_edit.project_editor_addr())
        project_editor_obj.click()
        time.sleep(1)

    def io_mapping(self):
        io_mapping_obj = self.driver.find_element_by_xpath(self.pr_edit.io_mapping_addr())
        io_mapping_obj.click()
        time.sleep(1)

    def maxx_io(self):
        io_obj = self.driver.find_element_by_xpath(self.pr_edit.maxx_io_addr())
        io_obj.click()
        time.sleep(1)

    def maxx_inputs(self):
        inputs_obj = self.driver.find_element_by_xpath(self.pr_edit.maxx_inputs_addr())
        inputs_obj.click()
        time.sleep(3)

    def maxx_outputs(self):
        outputs_obj = self.driver.find_element_by_xpath(self.pr_edit.maxx_outputs_addr())
        outputs_obj.click()
        time.sleep(3)


class IO(ProjectEditor):

    def read_status_in5(self):
        input5_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-5-input"]')
        # print(input5_obj.find_element_by_link_text("disabled aria-checked"))

    def press_out_1000(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-2"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1001(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-3"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1002(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-4"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1003(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-5"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1004(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-6"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1005(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-7"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1006(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-8"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1007(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-9"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1008(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-10"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1009(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-11"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1010(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-12"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1011(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-13"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1012(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-14"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1013(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-15"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1014(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-16"]')
        out_obj.click()
        time.sleep(1)

    def press_out_1015(self):
        out_obj = self.driver.find_element_by_xpath('//*[@id="mat-slide-toggle-17"]')
        out_obj.click()
        time.sleep(1)


class Home(Select):

    def power_button(self):
        self.power_button_obj = self.driver.find_element_by_xpath(self.home.power_button_addr())
        self.power_button_obj.click()

    def write_terminal(self, command):
        write_txt_obj = self.driver.find_element_by_xpath(self.home.write_terminal_addr())
        write_txt_obj.send_keys(Keys.ENTER)
        time.sleep(1)
        write_txt_obj.send_keys("clear")
        time.sleep(1)
        write_txt_obj.send_keys(Keys.ENTER)
        time.sleep(5)
        write_txt_obj.send_keys(command)
        time.sleep(5)
        # write_txt_obj.send_keys(Keys.ENTER)
        write_txt_obj.send_keys(Keys.ENTER)
        time.sleep(5)

    def read_terminal(self):
        text_obj = self.driver.find_element_by_xpath(self.home.read_terminal_addr())

        time.sleep(1)
        return text_obj.text


# obj = Select("192.168.0.1", "C:\\WebDriver\\Test\\chromedriver.exe", "admin", "ADMIN")
# obj.open_cs()
