from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

input=driver.find_element("name","q")
input.send_keys("Tutedude")

time.sleep(5)

button=driver.find_element("name","btnK")
button.click()
time.sleep(5)