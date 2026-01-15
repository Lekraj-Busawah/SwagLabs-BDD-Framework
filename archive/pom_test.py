from selenium import webdriver
from pages.login_page import LoginPage

# launch browser
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

# create an object of the page class
login_page = LoginPage(driver)

# use the methods
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login()

print("POM Test Completed")
driver.quit()