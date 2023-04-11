from selenium.webdriver.common.by import By

import time

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver


# Dashboard functionality check
    def testsearch1(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='Hardware']").click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        # driver.execute_script("window.scrollTo(0, 0);")
        driver.find_element(By.XPATH, "//button[text()='Components']").click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        # driver.execute_script("window.scrollTo(0, 0);")
        driver.find_element(By.XPATH, "//button[text()='Software']").click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[text()='Fabric Manager']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[text()='Interfaces']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@tabindex='-1']").click()
        time.sleep(2)