from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import os

import time

class MultipleLoginCheck:

    def __init__(self, driver):
        self.driver = driver
    
    def testsearch01_Invalid_login(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("superadmin")
        driver.find_element("id", "password").send_keys("Aviz@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)
        error_message = driver.find_element(By.XPATH, "//p[text()= 'Invalid username/password. Please try again or click Forgot password to reset.']")
        # assert error_message.text == "Invalid username/password. Please try again or click Forgot password to reset."
        if error_message:
            print("Invalid username/password", error_message.text)
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\testsearch01_Invalid_login_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
            exit
        else:
            print("enter valid password")

    def testsearch02_valid_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@id= 'username']").clear()
        driver.find_element(By.XPATH, "//input[@id= 'username']").send_keys("superadmin")
        driver.find_element("id", "password").clear()
        driver.find_element("id", "password").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)
        valid_message = driver.find_element(By.XPATH, "//li[text()='v1.2.0']")
        
        if valid_message:
            print("Login Success", valid_message.text)
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\testsearch02_valid_login_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
            exit
        else:
            print("login Failed")

    def testsearch03_login_with_missing_credentials(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("")
        driver.find_element("id", "password").send_keys("")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "//p[text()='This field cannot be empty']")
        if error_message:
            print("This field cannot be empty", error_message.text)
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\testsearch03_login_with_missing_credentials_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
            exit
        else:
            print("enter valid password")

    def testsearch04_forgot_password(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//p[text()='Forgot password']").click()
        time.sleep(1)
        valid_message = driver.find_element(By.XPATH, "//span[text()='`Please contact the super admin to reset your password.`']")
        if valid_message:
            print("", valid_message.text)
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\testsearch04_Forgot_Password_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
            exit
        else:
            print("Failed")

    def testsearch05_terms_page(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[text()='Terms']").click()
        time.sleep(10)
        print("Terms_Page_Passed")
        now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        filename = 'screenshot\\testsearch05_terms_page_{}.png'.format(now)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        driver.save_screenshot(filename)

    def testsearch06_privacy_page(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[text()='Privacy']").click()
        time.sleep(10)
        print("Privacy_Page_Passed")
        now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        filename = 'screenshot\\testsearch06_privacy_page_{}.png'.format(now)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        driver.save_screenshot(filename)
        
