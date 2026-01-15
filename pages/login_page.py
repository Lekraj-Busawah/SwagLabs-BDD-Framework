# page objects
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    # locators (must be tuples)
    # structure: (By.STRATEGY, "value")
    txt_username = (By.ID,'user-name')
    txt_password = (By.ID, 'password')
    btn_login = (By.ID, 'login-button')
    # btn_login_id = 'loginbutton' # incorrect locator

    # Note: No __init__ needed - it's inherited from BasePage

    # actions
    def enter_username(self, username):
        # Using the methods from BasePage
        self.enter_text(self.txt_username, username)

    def enter_password(self, password):
        self.enter_text(self.txt_password, password)

    def click_login(self):
        self.click_element(self.btn_login)


