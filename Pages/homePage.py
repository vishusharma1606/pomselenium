from selenium.webdriver.common.by import By
from Locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.profile_xpath = Locators.profile_xpath
        self.logout_xpath = Locators.logout_xpath

    def click_profile(self):
        self.driver.find_element(By.XPATH, self.profile_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()


        