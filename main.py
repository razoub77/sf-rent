import os
import re
import time

import dotenv
import requests as req
from bs4 import BeautifulSoup

from form import FormInput

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
    address_tag = rental_listings[i].select_one(
        'address[data-test="property-card-addr"]'
    )
    if address_tag is not None:
        address = address_tag.text.strip().replace(" | ", ", ")
        rental_addresses.append(address)

    price_tag = rental_listings[i].select_one('span[data-test="property-card-price"]')
    if price_tag is not None:
        price = format_price(price_tag.text)
        rental_prices.append(price)

    link_tag = rental_listings[i].select_one('a[data-test="property-card-link"]')
    if link_tag is not None:
        rental_links.append(link_tag["href"])

form_input = FormInput(FORM_LINK)

for i in range(len(rental_listings)):
    time.sleep(0.5)
    form_input.address_input(rental_addresses[i])
    form_input.price_input(rental_prices[i])
    form_input.link_input(rental_links[i])
    form_input.send()
    time.sleep(1)
    form_input.refresh()
