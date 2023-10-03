from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to URl
driver.get("https://www.google.com")

driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

# Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("title")
print(attr)

# Get element with tag name 'div'
element = driver.find_element(By.TAG_NAME, 'div')

# Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)