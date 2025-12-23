from selenium import webdriver
from selenium.webdriver.common.by import By


class FormInput:
    def __init__(self, link: str) -> None:
        self.link = link
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.options)
        self.driver.get(self.link)
        self.driver.implicitly_wait(3)

    def address_input(self, address: str):
        self.driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
        ).send_keys(address)

    def price_input(self, price: str):
        self.driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
        ).send_keys(price)

    def link_input(self, link: str):
        self.driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
        ).send_keys(link)

    def send(self):
        self.driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span",
        ).click()

    def refresh(self):
        self.driver.get(self.link)
