from selenium.webdriver.common.by import By
from Locators.locators import Locators
import time

class ResetUser():

    def __init__(self, driver):
        self.driver = driver

# Reset password

    def testsearch1(self): 
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Users Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div[8]/div/div/button/div/div").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Reset Password']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Admin@123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("Admin@123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(1)