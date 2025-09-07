import selenium
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(5)

select=driver.find_element("link text","Mobiles")
select.click()
time.sleep(5)
select1=driver.find_element("link text","Customer Service")
select1.click()
time.sleep(5)
driver.quit()
