from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

class ConfigPage:

    def __init__(self, driver):
        self.driver = driver
        self.configurationIcon_xpath = "//img[@alt='Configurations Icon']"
        self.configurationdevice_xpath = "//p[text()='Configure Devices']"
        self.download_yaml_xpath = "//p[text()='Download YAML']"
        self.cancel_xpath = "//button[text()='Cancel']"
        self.applyconfig_xpath = "//button[text()='Apply Configs']"

# configuration functionality check
    def testsearch1(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.configurationIcon_xpath).click()
        time.sleep(1)    
        driver.find_element(By.XPATH, self.configurationdevice_xpath).click()
        time.sleep(1)
        driver.find_element(By.XPATH, self.download_yaml_xpath).click()
        time.sleep(1)
        driver.find_element(By.XPATH, self.cancel_xpath).click()
        time.sleep(1)
        driver.find_element(By.XPATH, self.configurationdevice_xpath).click()
        time.sleep(1)
        driver.find_element(By.XPATH, self.applyconfig_xpath).click()
        time.sleep(1)
  