import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class selenium:
    def __init__(self):
        options = Options()  # Initialize Chrome options
        # Open Chrome in guest mode
        options.add_argument('--guest')
        self.driver = webdriver.Chrome(options=options)

        self.btnLogin = '//input[@id="login-button"]'
        self.username= '//input[@id="user-name"]'
        self.password = '//input[@id="password"]'
        self.text = '//div[@class="login_logo"]'

    def get(self,url):
        self.driver.get(url=url)

    def click(self):
        self.driver.find_element(By.XPATH,self.btnLogin).click()

    def sendKeys(self):
        self.driver.find_element(By.XPATH,self.username).send_keys("standard_user")
        self.driver.find_element(By.XPATH,self.password).send_keys("secret_sauce")

    def heading(self):
        headingcheck = self.driver.find_element(By.XPATH, self.text).text
        print(headingcheck)
        assert headingcheck == "Swag Labs"
        print("Test passed")

obj = selenium()
obj.get("https://www.saucedemo.com/")
obj.heading()
obj.sendKeys()
obj.click()
time.sleep(3)

