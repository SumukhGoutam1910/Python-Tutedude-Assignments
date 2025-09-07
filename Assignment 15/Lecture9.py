from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

driver.maximize_window()

driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("iphone")
time.sleep(2)
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()
time.sleep(2)

list=driver.find_elements("xpath","//a[@class='a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal']")

for i in list:
    print(i.text)

driver.quit()