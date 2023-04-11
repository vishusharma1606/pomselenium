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

    def test01_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)
    
    def test02_Add_users_EnterPriseAdmin(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        ea = AccountPage(driver)
        ea.testsearch1_Add_enterprise_admin()
        print("Add_users_EnterPriseAdmin_passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout successfully")
        time.sleep(2)

    def test03_Add_users_EnterpriseStaff(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        es = AccountPage(driver)
        es.testsearch2_Add_enterprise_staff()
        print("Add_users_EnterpriseStaff_Passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout successfully")
        time.sleep(2)

    def test04_Add_users_vendorStaff(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        vs = AccountPage(driver)
        vs.testsearch3_Add_vendor_staff()
        print("Add_users_vendorStaff_passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout successfully")
        time.sleep(2)

    def test05_vendorstaff_login(self):
        driver = self.driver

        vendor = VendorStaff(driver)
        vendor.testsearch1()
        print("Login_vendorstaff")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout successfully")
        time.sleep(2)

    def test06_enterprisestaff_login(self):
        driver = self.driver

        vendor = EnterpriseStaff(driver)
        vendor.testsearch1()
        print("Login_enterprisestaff")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout successfully")
        time.sleep(2)


    def test07_enterpriseAdmin_login(self):
        driver = self.driver

        vendor = EnterpriseAdmin(driver)
        vendor.testsearch1()
        print("Login_EnterpriseAdmin")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout successfully")
        time.sleep(2)

    def test08_delete_user(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        delete = DeleteUser(driver)
        delete.testsearch1()
        delete.testsearch2()
        delete.testsearch3()
        time.sleep(2)
        print("suspend_restore_delete_user_passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test09_reset_valid(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        reset = ResetUser(driver)
        reset.testsearch1()
        time.sleep(2)
        print("Reset_passed")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    # def test11_Activate_licence_invalidkey(self):
    #     driver = self.driver
       
    #     login = LoginPage(driver)
    #     login.enter_username()
    #     login.enter_password()
    #     login.click_login()
    #     print("Login_succesfull")
    #     time.sleep(4)

    #     activate = ActivateLicence(driver)
    #     activate.testsearch1_activate_licence_invalid_key()

    def test10_login_valid(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        licencepage = Licence(driver)
        licencepage.testsearch1()
        print("check_licence_page")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\ones1.2\\reports'))