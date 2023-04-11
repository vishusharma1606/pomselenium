import unittest
import time
import pytest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# from Locators.locators import Locators
from datetime import datetime
import os
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumTest(unittest.TestCase):

# url and credential login 
    @classmethod
    def setUp(self):
        # self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        driver = self.driver
        driver.get("https://192.168.74.129")

    def testsearch1_auto_refresh_interval_30_second(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("superadmin")
        driver.find_element("id", "password").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Settings Icon']").click()
        driver.find_element(By.XPATH, "//button[text()='Application']").click()
        driver.find_element(By.XPATH, "//div[@id='demo-multiple-name']").click()
        driver.find_element(By.XPATH, "//li[text()='30 Seconds']").click()
        driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-0']/button/div/p[text()='Save']").click()
        time.sleep(2)
        try: 
            valid_message = driver.find_element(By.XPATH, "//div[text()= 'Settings Updated Successful']")
            print("", valid_message.text)
        except:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\auto_refresh_interval_30_second_fail_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
                  

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\ones1.2\\reports'))

