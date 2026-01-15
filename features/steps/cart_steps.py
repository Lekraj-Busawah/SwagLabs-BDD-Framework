from behave import *
from pages.inventory_page import InventoryPage

@given(u'I click "Add to Cart" on a "{item_name}"')
def step_impl(context, item_name):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.click_add_to_cart(item_name)

@then(u'the cart icon should show 1 item')
def step_impl(context):
    count = context.inventory_page.get_cart_count()
    filename = f"screenshots/"
    context.driver.save_screenshot(filename)
    assert count == '1', f"Expected 1 item in cart but found {count}"