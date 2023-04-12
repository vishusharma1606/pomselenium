from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import os

import time

class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    def testsearch1_profile_change_firstname_lastname(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//div[@aria-label='Profile']//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        driver.find_element(By.XPATH, "//li[text()='Profile']").click()
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("vishu")
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("sharma")
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(4)
        valid_message = driver.find_element(By.XPATH, "//div[text()='Users Updated Successfully']")
        if valid_message:
            print("", valid_message.text)
        else:
            print("user not updated")
        driver.find_element(By.XPATH, "//div[@aria-label='Profile']//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        driver.find_element(By.XPATH, "//li[text()='Profile']").click()
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("superadmin")
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("aviz")
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(4)
        valid_message = driver.find_element(By.XPATH, "//div[text()='Users Updated Successfully']")
        if valid_message:
            print("", valid_message.text)
        else:
            print("user not updated")