from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def find_element(self, locator):
        """Wait for element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        """Wait for element to be visible and click it."""
        return self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def enter_text(self, locator, text):
        """Wait for element, clear it, and type text."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_title(self):
        return self.driver.title