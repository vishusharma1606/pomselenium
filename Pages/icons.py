from selenium.webdriver.common.by import By

import time

class Icons:

    def __init__(self, driver):
        self.driver = driver
        self.refresh_xpath = "//img[@alt='Refresh Icon']"
        self.support_xpath = "//a[@href='https://support.aviznetworks.com']"
        self.document_xpath = "//a[@href='https://aviznetworks.gitbook.io/ones-user-guide/']"

    # refresh button 
    def testsearch1_refresh_button(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.refresh_xpath).click()
        time.sleep(1)
        

    # support portal 
    def testsearch2_support_button(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.support_xpath).click()
        time.sleep(1)
       

    # documentation
    def testsearch3_document_button(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.document_xpath).click()
        time.sleep(1)