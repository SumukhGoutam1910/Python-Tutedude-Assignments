import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.response=requests.get(url=self.url, headers=self.user_agent).text
        self.soup=BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title=self.soup.find("span",{id:"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price=self.soup.find("span",{id:"priceblock_ourprice"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag not found"

device=PriceTracer(url="https://www.amazon.in/Samsung-Storage-Display-Charging-Security/dp/B0DFY3XCB6/ref=sr_1_1?nsdOptOutParam=true&sr=8-1")
print(device.product_title())
print(device.product_price())