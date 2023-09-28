import pytest
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= options)

driver.implicitly_wait(2)
driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
driver.find_element(By.ID, "adder").click()

added = driver.find_element(By.ID, "box0")

revealed = driver.find_element(By.ID, "revealed")
errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=2)

driver.find_element(By.ID, "reveal").click()
wait.until(lambda d : revealed.is_displayed())

revealed.send_keys("Displayed")