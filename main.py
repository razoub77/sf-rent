import os
import re

import dotenv
import requests as req
from bs4 import BeautifulSoup

# from selenium import webdriver

dotenv.load_dotenv()

RENT_LINK = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK = str(os.getenv("FORM_LINK"))

r = req.get(RENT_LINK)
r.raise_for_status()
webpage = r.text

soup = BeautifulSoup(webpage, "html.parser")
rental_listings = soup.select(
    ".ListItem-c11n-8-84-3-StyledListCardWrapper .StyledPropertyCardDataWrapper"
)
rental_prices = []
rental_addresses = []
rental_links = []


def format_price(price_str):
    match = re.search(r"\$(\d[\d,]*)", price_str)
    if match:
        raw_num = match.group(1).replace(",", "")
        return f"${int(raw_num):,}"
    return None


for i in range(len(rental_listings)):
    price_tag = rental_listings[i].select_one('span[data-test="property-card-price"]')
    if price_tag is not None:
        price = format_price(price_tag.text)
        rental_prices.append(price)

    address_tag = rental_listings[i].select_one(
        'address[data-test="property-card-addr"]'
    )
    if address_tag is not None:
        address = address_tag.text.strip().replace(" | ", ", ")
        rental_addresses.append(address)

    link_tag = rental_listings[i].select_one('a[data-test="property-card-link"]')
    if link_tag is not None:
        rental_links.append(link_tag["href"])


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options)
# driver.get(FORM_LINK)
