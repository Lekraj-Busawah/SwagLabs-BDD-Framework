from datetime import datetime
from selenium import webdriver
from utilities.read_properties import ReadConfig
from behave import *
from utilities.custom_logger import LogGen
import os
import allure
import logging

def before_scenario(context, scenario):
    # runs before every single test case

    # 1. Read the URL from Config
    context.base_url = ReadConfig.get_application_url()

    # 2. Setup browser    
    # use before_scenario to open a fresh browser after every test
    browser_name = ReadConfig.get_browser()
    if browser_name == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        context.driver = webdriver.Firefox()
    elif browser_name == 'edge':
        context.driver = webdriver.Edge()
    elif browser_name == 'safari':
        context.driver = webdriver.Safari()
    context.driver.maximize_window()
    logger.info(f"**** Started Scenario: {scenario.name} ****")

logger = LogGen.loggen()

def after_step(context, step):
    if step.status != 'passed':
        # Create a name for the screenshot based on the step name
        screenshot_name = step.name.replace(" ", "_")

        # 1. Take screenshot as binary data
        screenshot_binary = context.driver.get_screenshot_as_png()

        # 2. Attach it to the Allure report
        allure.attach(
            screenshot_binary,
            screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )

        # (Optional) Save file locally
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        filename = f"screenshots/{screenshot_name}_{datetime.now().strftime('%H%M%S')}.png"
        context.driver.save_screenshot(filename)
        logger.info(f"**** Screenshot saved as {screenshot_name} ****")
        browser_logs = context.driver.get_log('browser')
        allure.attach(
            str(browser_logs),
            name="Browser_Console_logs",
            attachment_type=allure.attachment_type.TEXT
        )

def after_scenario(context, scenario):
    # 1. Log error
    if scenario.status != "passed":
        if hasattr(context, 'driver'):
            logging.error(f"Scenario failed: {scenario.name}. Screenshot attached.")

    # Closing the browser
    if hasattr(context, 'driver'):
        context.driver.quit()
        logging.info(f"**** Finished Scenario: {scenario.name} - Browser Closed ****")
    