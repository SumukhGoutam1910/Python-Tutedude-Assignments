from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("laptop")
time.sleep(5)
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()
time.sleep(5)

driver.quit()