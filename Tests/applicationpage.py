from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
import sys
sys.path.append('C:\\Users\\vishv\\Desktop\\ones1.2')

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.accountpage import AccountPage
from Pages.icons import Icons
from Pages.settingPage.application import SettingPage
from Pages.deleteuser import DeleteUser
from Pages.resetuser import ResetUser
from Pages.activatelicence import ActivateLicence
from Pages.vendorstaff import VendorStaff
from Pages.enterpriseadmin import EnterpriseAdmin
from Pages.enterprisestaff import EnterpriseStaff
from Pages.licencepage import Licence


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\vishv\\Desktop\\ones1.2\\Drivers\\chromedriver.exe")
        cls.driver.get("https://192.168.74.129")
        cls.driver.maximize_window()

    def test01_Auto_Refresh_Interval_30_second(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        ari30 = SettingPage(driver)
        ari30.testsearch1_auto_refresh_interval_30_second()
        
 

    def test02_Auto_Refresh_Interval_60_second(self):
        driver = self.driver


        ari60 = SettingPage(driver)
        ari60.testsearch2_auto_refresh_interval_60_second()


    def test03_Auto_Refresh_Interval_90_second(self):
        driver = self.driver



        ari90 = SettingPage(driver)
        ari90.testsearch3_auto_refresh_interval_90_second()
 


    def test04_Auto_Refresh_Interval_120_second(self):
        driver = self.driver



        ari120 = SettingPage(driver)
        ari120.testsearch4_auto_refresh_interval_120_second()



    def test05_Application_Idle_Time_in_3_Minutes(self):
        driver = self.driver


        setting = SettingPage(driver)
        setting.testsearch5_application_idle_time_in_3_Minutes()

    def test06_Application_Idle_Time_in_2_Minutes(self):
        driver = self.driver

        setting = SettingPage(driver)
        setting.testsearch6_application_idle_time_in_2_Minutes()

    def test07_Application_Idle_Time_in_50dot22_Minutes(self):
        driver = self.driver

        setting = SettingPage(driver)
        setting.testsearch7_application_idle_time_in_50dot22_Minutes()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\ones1.2\\reports'))