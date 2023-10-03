from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Add Cookie
driver.add_cookie({"name": "key", "value": "value"})

# Get Named Cookie
print(driver.get_cookie("foo"))

# Get All Cookies
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Get all available cookies
print(driver..get_cookie())

# Delete a cookie with name 'test1'
driver.delete_cookie("test1")

# Delets all cookies
driver.delete_all_cookies()