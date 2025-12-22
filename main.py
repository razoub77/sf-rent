import os

import dotenv
from selenium import webdriver

dotenv.load_dotenv()

FORM_LINK = str(os.getenv("FORM_LINK"))

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get(FORM_LINK)
