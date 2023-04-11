from selenium.webdriver.common.by import By
# from Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_xpath = "//button[@type='submit']"

    def enter_username(self):
        self.driver.find_element("id", self.username_textbox_id).clear()
        self.driver.find_element("id", self.username_textbox_id).send_keys("superadmin")

    def enter_password(self):
        self.driver.find_element('id', self.password_textbox_id ).clear()
        self.driver.find_element('id', self.password_textbox_id).send_keys("Admin@123")

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()
