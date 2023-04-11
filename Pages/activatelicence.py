from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time

class ActivateLicence:

    def __init__(self, driver):
        self.driver = driver

    def testsearch1_activate_licence_invalid_key(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//p[text()='Activate Now']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Activation Key: XXXX-XXXX-XXXX']").send_keys("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb3VudCI6MzIsInZhbGlkVGlsbCI6MTcxMjczMDAzMS4wNzgzNDgsIm1hY2hVdWlkIjoiVWRZaCtwSnphR2l4QXAzR2ZqIn0.Kz5pzTeuriPe7HJorC_-N6bJQ229xIXmKGpKsL0sHeY")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Activate']").click()
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "//p[text()='Invalid Activation Key please contact sales@aviznetworks.com']")
        if error_message:
            print("Error message: ", error_message.text)
            
        else:
            driver.close()

        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
