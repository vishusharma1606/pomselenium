from selenium.webdriver.common.by import By
import time

class Licence():

    def __init__(self, driver):
        self.driver = driver
        self.profile_xpath = "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']"
        self.licence_xpath = "//li[text()='License']"
        self.logout_xpath = "//li[text()='Logout']"

    def testsearch1(self):
        self.driver.find_element(By.XPATH, self.profile_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.licence_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.profile_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
        time.sleep(4)

    
