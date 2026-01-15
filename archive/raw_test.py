from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# launch browser
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

# find element and interact
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# verify login worked by checking 'product' title is visible
try:
    assert driver.find_element(By.XPATH, "//span[@class='title']").text.__eq__("Products")
    print("Test Passed: Login Successful")
except Exception as e:
    print("Test Failed")

# close browser
time.sleep(2)
driver.close()