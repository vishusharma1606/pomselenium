from selenium.webdriver.common.by import By
from Locators.locators import Locators
import time

class DeleteUser():

    def __init__(self, driver):
        self.driver = driver

# check functionality Account page (suspend user and restore user and delete user)

    def testsearch1(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Users Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Suspend']").click()
        driver.find_element(By.XPATH, "//button[text()='Yes']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='/static/media/refresh.d8d17dec.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Restore']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Remove']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        

    def testsearch2(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Users Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Suspend']").click()
        driver.find_element(By.XPATH, "//button[text()='Yes']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='/static/media/refresh.d8d17dec.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Restore']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Remove']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        

    def testsearch3(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Users Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Suspend']").click()
        driver.find_element(By.XPATH, "//button[text()='Yes']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='/static/media/refresh.d8d17dec.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Restore']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Remove']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
       