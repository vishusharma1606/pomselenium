from selenium.webdriver.common.by import By

import time

class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        
        self.accounts_xpath = "//img[@alt='Users Icon']"
        self.add_xpath = "//button//span[text()='Add']"
        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.confirmpasssword_textbox_id = "confirmPassword"
        self.firstname_textbox_id = "firstName"
        self.lastname_textbox_id = "lastName"
        self.selectrole_xpath = "//div[@id='mui-component-select-role']"
        self.role1_xapth = "//li[text()='Enterprise Admin']"
        self.role2_xpath = "//li[text()='Enterprise Staff']"
        self.role3_xpath = "//li[text()='Vendor Staff']"
        self.save_path = "//button[text()='Save']"
        
    def testsearch1_Add_enterprise_admin(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.accounts_xpath).click()
        driver.find_element(By.XPATH, self.add_xpath).click()
        time.sleep(1)
        driver.find_element("name", self.username_textbox_id).send_keys("vishu")
        driver.find_element("name", self.password_textbox_id).send_keys("aviz@123")
        driver.find_element("name", self.confirmpasssword_textbox_id).send_keys("aviz@123")
        driver.find_element("name", self.firstname_textbox_id).send_keys("vishu")
        driver.find_element("name", self.lastname_textbox_id).send_keys("sharma")
        driver.find_element(By.XPATH, self.selectrole_xpath).click()
        driver.find_element(By.XPATH, self.role1_xapth).click()
        driver.find_element(By.XPATH, self.save_path).click()
        time.sleep(3)

    def testsearch2_Add_enterprise_staff(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.accounts_xpath).click()
        driver.find_element(By.XPATH, self.add_xpath).click()
        time.sleep(1)
        driver.find_element("name", self.username_textbox_id).send_keys("ravi")
        driver.find_element("name", self.password_textbox_id).send_keys("aviz@123")
        driver.find_element("name", self.confirmpasssword_textbox_id).send_keys("aviz@123")
        driver.find_element("name", self.firstname_textbox_id).send_keys("ravi")
        driver.find_element("name", self.lastname_textbox_id).send_keys("kumar")
        driver.find_element(By.XPATH, self.selectrole_xpath).click()
        driver.find_element(By.XPATH, self.role2_xpath).click()
        driver.find_element(By.XPATH, self.save_path).click()
        time.sleep(2)

    def testsearch3_Add_vendor_staff(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.accounts_xpath).click()
        driver.find_element(By.XPATH, self.add_xpath).click()
        time.sleep(1)
        driver.find_element("name", self.username_textbox_id).send_keys("Neeraj")
        driver.find_element("name", self.password_textbox_id).send_keys("aviz@123")
        driver.find_element("name", self.confirmpasssword_textbox_id).send_keys("aviz@123")
        driver.find_element("name", self.firstname_textbox_id).send_keys("Neeraj")
        driver.find_element("name", self.lastname_textbox_id).send_keys("Kamboj")
        driver.find_element(By.XPATH, self.selectrole_xpath).click()
        driver.find_element(By.XPATH, self.role3_xpath).click()
        driver.find_element(By.XPATH, self.save_path).click()
        time.sleep(2)

