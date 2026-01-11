from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Gin_And_Juice:
    def __init__(self):
        options = Options()  # Initialize Chrome options
        # Open Chrome in guest mode
        options.add_argument('--guest')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        self.ViewAllProduct = '/html/body/div[2]/section/section/a'
        self.F_Product = '/html/body/div[2]/section/div/section[3]/a[1]/span[2]'
        self.S_Product = '/html/body/div[2]/section/div/section[3]/a[2]/span[2]'
        self.checkStock = '//*[@id="stockCheckForm"]/button'
        self.AddToCart = '//*[@id="addToCartForm"]/button'
        self.ViewCart = '/html/body/div[2]/section/div/section/div[2]/span[5]/a'

        self.PlaceOrder = '/html/body/div[2]/section/div/div/div[2]/div/form[2]/button'

        self.username = '/html/body/div/section/div/section/form/input[3]'

        self.login = '/html/body/div/section/div/section/form/button'

        self.password = '/html/body/div/section/div/section/form/input[4]'


    def getUrl(self, URL):
        self.driver.get(url=URL)

    def HomePage(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ViewAllProduct))).click()

    def ProductPage(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.F_Product))).click()

    def ProductView(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.AddToCart))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ViewCart))).click()

    def cart(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PlaceOrder))).click()

    def Login(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.username))).send_keys("carlos")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.password))).send_keys("hunter2")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login))).click()






obj = Gin_And_Juice()
obj.getUrl('https://ginandjuice.shop/')
obj.HomePage()
obj.ProductPage()
obj.ProductView()
obj.cart()
obj.Login()




