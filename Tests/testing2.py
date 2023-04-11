from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
import sys
sys.path.append('C:\\Users\\vishv\\Desktop\\ones1.2')

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.dashboardpage import DashboardPage
# from Pages.monitorpage import MonitorPage
from Pages.inventorypage import InventoryPage
from Pages.configurationPage import ConfigPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\vishv\\Desktop\\ones1.2\\Drivers\\chromedriver.exe")
        cls.driver.get("https://192.168.74.129")
        cls.driver.maximize_window()
 
    def test01_Dashboard_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        dashboard = DashboardPage(driver)
        dashboard.testsearch1()
        time.sleep(2)
        print("Dashboardpage_test_passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout_successfull")
        time.sleep(2)

    # def test02_Monitor_valid(self):
    #     driver = self.driver
       
    #     login = LoginPage(driver)
    #     login.enter_username("superadmin")
    #     login.enter_password("Admin@123")
    #     login.click_login()
    #     print("Login_succesfull")
    #     time.sleep(4)

    #     monitor = MonitorPage(driver)
    #     monitor.testsearch1()
    #     time.sleep(2)
    #     print("Monitorpage_test_passed")

    #     homepage = HomePage(driver)
    #     homepage.click_profile()
    #     homepage.click_logout()
    #     print("Logout_successfull")
    #     time.sleep(2)

    def test03_inventory_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        inventory = InventoryPage(driver)
        inventory.testsearch1()
        time.sleep(2)
        print("Inventorypage_test_passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout_successfull")
        time.sleep(2)

    def test04_configurationPage_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        config = ConfigPage(driver)
        config.testsearch1()
        time.sleep(2)
        print("configuration_test_passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout_successfull")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\ones1.2\\reports'))