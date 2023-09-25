from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
driver.implicitly_wait(100)

text_box = driver.find_element(by = By.NAME, value= "my-text")
submit_button = driver.find_element(by = By.CSS_SELECTOR, value = "button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by = By.ID, value = "message")
value = message.text
assert value == "Received!"

driver.implicitly_wait(60)

