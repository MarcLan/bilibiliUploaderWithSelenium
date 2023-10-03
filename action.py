from selenium import webdriver

driver = webdriver.Chrome()

clickable = driver.find_element(By.ID, "clickable")
ActionChains(driver) \
    .move_to_element(clickable) \
    .pause(1) \
    .click_and_hold()\
    .pause(1)\
    .send_keys("abc")
    .perform()

ActionBuilder(drvier).clear_action()