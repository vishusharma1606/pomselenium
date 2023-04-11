from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
import sys
sys.path.append('C:\\Users\\vishv\\Desktop\\ones1.2')

from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Pages.Loginpage.Multiplelogincheck import MultipleLoginCheck
from Pages.icons import Icons

class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\vishv\\Desktop\\ones1.2\\Drivers\\chromedriver.exe")
        self.driver.get("https://192.168.74.129")
        self.driver.maximize_window()
 
    def test01_Invalid_login_credential(self):
        driver = self.driver
        loginwrong = MultipleLoginCheck(driver)
        loginwrong.testsearch01_Invalid_login()
        
    def test02_valid_login_credential(self):
        driver = self.driver
        validlogin = MultipleLoginCheck(driver)
        validlogin.testsearch02_valid_login()

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("Logout successfully")

    def test03_Login_With_Missing_Credentials(self):
        driver = self.driver
        loginmissing = MultipleLoginCheck(driver)
        loginmissing.testsearch03_login_with_missing_credentials()

    def test04_Forgot_Password(self):
        driver = self.driver
        forgotpassword = MultipleLoginCheck(driver)
        forgotpassword.testsearch04_forgot_password()

    def test05_Terms_Page(self):
        driver = self.driver
        terms = MultipleLoginCheck(driver)
        terms.testsearch05_terms_page()

    def test06_Privacy_Page(self):
        driver = self.driver
        privacy = MultipleLoginCheck(driver)
        privacy.testsearch06_privacy_page()

    def test07_refresh_button_check(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        rb = Icons(driver)
        rb.testsearch1_refresh_button()
        print("refresh_successfull")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test08_support_button_check(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        sp = Icons(driver)
        sp.testsearch2_support_button()
        print("support_successfull")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)

    def test09_document_button_check(self):
        driver = self.driver
       
        login = LoginPage(driver)
        login.enter_username()
        login.enter_password()
        login.click_login()
        print("Login_succesfull")
        time.sleep(4)

        db = Icons(driver)
        db.testsearch3_document_button()
        print("open_document_successfull")

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()
        print("logout_successfull")
        time.sleep(2)
        

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\ones1.2\\reports'))