from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= options)

# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
driver.title
driver.current_url
driver.back()
driver.refresh()

driver.find_element(By.LINK_TEXT, "See an example alert").click()
alert = wait.until(expected_conditions.alert_is_present())
text = alert.text
alert.accept()

driver.find_element(By.LINK_TEXT, "See a sample prompt").click()
wait.until(expeted_conditions.alert_is_present())
alert = Alert(driver)
alert.send_keys("Selenium")
alert.accept()

driver.find_element(By.LINK_TEXT, "See a sample confirm").click()
wait.until(expected_conditions.alert_is_present())
alert = driver.switch_to.alert
text = alert.text
alert.dismiss()

isEmailVisibe = driver.find_element(By.NAME, "email_input").is_displayed()
value = driver.find_element(By.NAME, "button_input").is_enabled()
value = driver.find_element(By.NAME, "checkbox_input").is_selected()

cssValue = driver.find_element(By.ID, "namedColor").value_of_css_property('background-color')

text = driver.find_element(By.ID, "justanotherlink").text
email_txt = driver.find_element(By.NAME, "email_input")
value_info = email_txt.get_attribute("value")

# attr = driver.find_element(By.NAME, "email_input").tag_name()
# res = driver.find_element(By.NAME, "range_input").rect

#driver.find_element(By.NAME, "color_input").click()
#driver.find_element(By.NAME, "email_input").clear()
#driver.find_element(By.NAME, "email_input").send_keys("admin@localhost.dev")


