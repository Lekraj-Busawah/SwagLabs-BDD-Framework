from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):

    # locators
    inventory_item_name = (By.XPATH, "//div[@class='inventory_item_name']")
    btn_add_to_cart = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')

    # actions
    def click_add_to_cart(self, item_name):
        """
        Dynamically clicks the 'Add to cart' button for a specific item.
        Example: 'jacket' -> 'add-to-cart-sauce-labs-fleece-jacket'
        """
        item_map = {
            "jacket": "add-to-cart-sauce-labs-fleece-jacket",
            "t-shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "bike-light": "add-to-cart-sauce-labs-bike-light"
        }
        
        button_id = item_map.get(item_name.lower())

        if button_id:
            dynamic_locator = (By.ID, button_id)
            self.click_element(dynamic_locator)
        else:
            raise ValueError(f"Item '{item_name}' not found in the item map!")
        
    
    def get_cart_count(self):
        return self.find_element(self.shopping_cart_badge).text
    

    