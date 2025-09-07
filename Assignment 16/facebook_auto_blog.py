from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# Add arguments to prevent Chrome crashes
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--start-maximized')


driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com")
driver.maximize_window()

email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("1234567890")

password = driver.find_element(By.XPATH, "//input[@id='pass']")
password.send_keys("password123")

driver.find_element(By.XPATH, "//button[@name='login']").click()
print("Login button clicked, waiting for page to load...")
time.sleep(10)

# Navigate to home page explicitly
driver.get("https://www.facebook.com/")
time.sleep(5)

# Try different selectors for the create post button
post_selectors = [
    "//div[@aria-label='Create a post'][@role='region']//div[@role='button'][@tabindex='0']",
    "//div[@aria-label='Create a post']//div[@role='button'][@tabindex='0']",
    "//div[@role='region'][@aria-label='Create a post']//div[@role='button']",
    "//div[@aria-label='Create a post']",
    "//div[contains(text(), \"What's on your mind, Sumukh?\")]",
    "//span[contains(text(), \"What's on your mind, Sumukh?\")]",
    "//div[@role='button' and contains(text(), \"What's on your mind\")]",
    "//div[contains(@aria-label, 'Create')]",
    "//div[@tabindex='0' and contains(text(), \"What's on your mind\")]",
    "//div[@role='button'][@tabindex='0'][contains(text(), \"What's on your mind\")]",
    "//div[@tabindex][contains(text(), 'Sumukh')]"
]

statuselement1 = None
for i, selector in enumerate(post_selectors):
    try:
        print(f"Trying selector {i+1}/{len(post_selectors)}: {selector}")
        statuselement1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
        print(f"✓ Found create post button with selector: {selector}")
        break
    except Exception as e:
        print(f"✗ Selector failed: {selector}")
        continue

if statuselement1 is None:
    print("Could not find create post button")
    driver.save_screenshot("debug_screenshot.png")
    driver.quit()
    exit()

statuselement1.click()
print("Clicked create post button, waiting for text input...")
time.sleep(5)

# Try different selectors for text input
text_selectors = [
    "//div[@role='textbox']",
    "//div[@contenteditable='true']",
    "//div[@aria-label=\"What's on your mind?\"]",
    "//p[@data-text='true']",
    "//div[@data-contents='true']"
]

statuselement2 = None
for i, selector in enumerate(text_selectors):
    try:
        print(f"Trying text selector {i+1}/{len(text_selectors)}: {selector}")
        statuselement2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
        print(f"✓ Found text input with selector: {selector}")
        break
    except Exception as e:
        print(f"✗ Text selector failed: {selector}")
        continue

if statuselement2 is None:
    print("Could not find text input")
    driver.save_screenshot("debug_text_input.png")
    driver.quit()
    exit()
statuselement2.send_keys("Hello Everyone, This is my second automated post using Selenium on Chrome!")
print("Text entered successfully")
time.sleep(3)

# Try different selectors for the Post button
post_button_selectors = [
    "//div[@aria-label='Post']",
    "//button[@aria-label='Post']",
    "//div[@role='button' and contains(text(), 'Post')]",
    "//button[contains(text(), 'Post')]",
    "//div[@tabindex='0' and contains(text(), 'Post')]",
    "//div[@role='button'][@tabindex='0'][contains(text(), 'Post')]",
    "//span[text()='Post']/parent::div[@tabindex]",
    "//div[@tabindex][contains(@aria-label, 'Post')]"
]

post_button = None
for i, selector in enumerate(post_button_selectors):
    try:
        print(f"Trying post button selector {i+1}/{len(post_button_selectors)}: {selector}")
        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
        print(f"✓ Found post button with selector: {selector}")
        break
    except Exception as e:
        print(f"✗ Post button selector failed: {selector}")
        continue

if post_button is None:
    print("Could not find post button")
    driver.save_screenshot("debug_post_button.png")
    driver.quit()
    exit()

post_button.click()
print("✓ Post published successfully!")

time.sleep(10)
driver.quit()