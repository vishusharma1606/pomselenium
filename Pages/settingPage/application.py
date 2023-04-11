from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os

class SettingPage:

    def __init__(self, driver):
        self.driver = driver
        self.setting_xpath = "//img[@alt='Settings Icon']"
        self.applicationicon_xpath = "//button[text()='Application']"
        self.selecttimer_xpath = "//div[@id='demo-multiple-name']"
        self.select30_second_xpath = "//li[text()='30 Seconds']"
        self.select60_second_xpath = "//li[text()='60 Seconds']"
        self.select90_second_xpath = "//li[text()='90 Seconds']"
        self.select120_second_xpath = "//li[text()='120 Seconds']"
        self.savebutton_xpath = "//div[@class='MuiBox-root css-0']/button/div/p[text()='Save']"
        self.reset_button_xpath = "//p[text()='Reset']"
        self.clear_xpath = "//input[@type='number']"
        self.enter_no_xpath = "//input[@type='number']"
        self.save_button = "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button/div/p"
        

# check functionality Setting page (--Auto Refresh Interval and Application Idle Time in Minutes--) 

    def testsearch1_auto_refresh_interval_30_second(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.setting_xpath).click()
        driver.find_element(By.XPATH, self.applicationicon_xpath).click()
        driver.find_element(By.XPATH, self.selecttimer_xpath).click()
        driver.find_element(By.XPATH, self.select30_second_xpath).click()
        driver.find_element(By.XPATH, self.savebutton_xpath).click()
        time.sleep(2) 
        
        valid_message = driver.find_element(By.XPATH, "//div[text()= 'Settings Updated Successful']")
       
        if valid_message:
            print("", valid_message.text)
        else:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = f'screenshot\\auto_refresh_interval_30_second_fail_{now}.png'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)

    def testsearch2_auto_refresh_interval_60_second(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.setting_xpath).click()
        driver.find_element(By.XPATH, self.applicationicon_xpath).click()
        driver.find_element(By.XPATH, self.selecttimer_xpath).click()
        driver.find_element(By.XPATH, self.select60_second_xpath).click()
        driver.find_element(By.XPATH, self.savebutton_xpath).click()
        time.sleep(2)
        valid_message = driver.find_element(By.XPATH, "//div[text()= 'Settings Updated Successful']")
        if valid_message:
            print("", valid_message.text)
        else:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\auto_refresh_interval_60_second_fail_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)

    def testsearch3_auto_refresh_interval_90_second(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.setting_xpath).click()
        driver.find_element(By.XPATH, self.applicationicon_xpath).click()
        driver.find_element(By.XPATH, self.selecttimer_xpath).click()
        driver.find_element(By.XPATH, self.select90_second_xpath).click()
        driver.find_element(By.XPATH, self.savebutton_xpath).click()
        time.sleep(2)
        valid_message = driver.find_element(By.XPATH, "//div[text()= 'Settings Updated Successful']")
        if valid_message:
            print("", valid_message.text)
        else:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\auto_refresh_interval_90_second_fail_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
    
    def testsearch4_auto_refresh_interval_120_second(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.setting_xpath).click()
        driver.find_element(By.XPATH, self.applicationicon_xpath).click()
        driver.find_element(By.XPATH, self.selecttimer_xpath).click()
        driver.find_element(By.XPATH, self.select120_second_xpath).click()
        driver.find_element(By.XPATH, self.savebutton_xpath).click()
        time.sleep(2)
        valid_message = driver.find_element(By.XPATH, "//div[text()= 'Settings Updated Successful']")
        if valid_message:
            print("", valid_message.text)
        else:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\auto_refresh_interval_120_second_fail_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)

    def testsearch5_application_idle_time_in_3_Minutes(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.reset_button_xpath).click()
        driver.find_element(By.XPATH, self.clear_xpath).send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        driver.find_element(By.XPATH, self.enter_no_xpath).send_keys(3)
        driver.find_element(By.XPATH, self.save_button).click()
        valid_message = driver.find_element(By.XPATH, "//div[text()= 'Settings Updated Successful']")
        if valid_message:
            print("", valid_message.text)
        else:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\application_idle_time_in_3_Minutes_fail_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)

    def testsearch6_application_idle_time_in_2_Minutes(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.reset_button_xpath).click()
        driver.find_element(By.XPATH, self.clear_xpath).send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        driver.find_element(By.XPATH, self.enter_no_xpath).send_keys(2)
        driver.find_element(By.XPATH, self.save_button).click()
        error_message = driver.find_element(By.XPATH, "//p[text()='Value Should be higher than 2']")
        if error_message: 
            print("", error_message.text)
        else:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\application_idle_time_in_2_Minutes_fail_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)

    def testsearch7_application_idle_time_in_50dot22_Minutes(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.reset_button_xpath).click()
        driver.find_element(By.XPATH, self.clear_xpath).send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        driver.find_element(By.XPATH, self.enter_no_xpath).send_keys(50.222)
        driver.find_element(By.XPATH, self.save_button).click()
        error_message = driver.find_element(By.XPATH, "//p[text()='Enter correct value']")
        if error_message: 
            print("", error_message.text)
        else:
            now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = 'screenshot\\application_idle_time_in_50.22_Minutes_fail_{}.png'.format(now)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
               


       