from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()

# File Upload
driver.implicitly_wait(10)
driver.get('https://the-internet.herokuapp.com/upload')

driver.find_element(By.ID, 'file-upload').send_keys("selenium-snapshot.jpg")
driver.find_element(By.ID, 'file-submit').submit()
if (driver.page_source.find('File Uploaded!')):
    print('File upload success')
else:
    print('File upload not successful')
driver.quite()

# Locator
driver.find_element(By.CLASS_NAME, "information")
driver.find_element(By.CSS_SELECTOR, "#fname")
driver.find_element(By.ID, "lname")
driver.find_element(By.NAME, "newletter")
driver.find_element(By.LINK_TEXT, "Selenium Official Page")
driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
driver.find_element(By.TAG_NAME, "a")
driver.find_element(By.XPATH, "//input[@value='f']")
email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})
password_locator = locate_with(By.TAG_NAME, "input").below({By.ID: "email"})
cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})
submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})
email_locator = locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})
submit_locator = locate_with(By.TAG_NAME, "button").below({By.ID: "email"}).to_right_of({By.ID: "cancel"})