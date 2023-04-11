from selenium.webdriver.common.by import By
import time

class EnterpriseAdmin:

    def __init__(self, driver):
        self.driver = driver

    def testsearch1(self):
        driver = self.driver
        driver.find_element("id", "username").send_keys("vishu")
        driver.find_element("id", "password").send_keys("aviz@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//input[@id='confirmpassword']").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[text()='Reset password']").click()
        time.sleep(3)
        driver.find_element("id", "username").send_keys("vishu")
        driver.find_element("id", "password").send_keys("Admin@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)
