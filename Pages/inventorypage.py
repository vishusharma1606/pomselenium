from selenium.webdriver.common.by import By

import time

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver



# check functionality inventory page
    def testsearch1(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Inventory Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='PrivateSwitchBase-input css-1m9pwf3'][@type='checkbox'][@aria-label='Select all rows']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Custom Upgrade']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Upgrade via ZTP']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Reboot Devices']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@type='checkbox'][@aria-label='Unselect all rows']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[text()='Add/Remove Devices']").click()
        time.sleep(2)        
        driver.find_element(By.XPATH, "//p[text()='Download YAML']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Add/Remove Devices']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Save & Apply']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@tabindex='-1']").click()
        time.sleep(2)