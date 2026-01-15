# step definitions

from behave import *
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utilities.custom_logger import LogGen

logger = LogGen.loggen()

@given(u'I launch the SwagLabs website')
def step_impl(context):
    # context is the "box" we carry between steps
    # use variable stored in environment.py
    logger.info("**** Starting Login Test ****")
    context.driver.get(context.base_url)
    logger.info("**** Opened URL ****")
    context.login_page = LoginPage(context.driver)

@when(u'I enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.login_page.enter_username(user)
    context.login_page.enter_password(pwd)
    logger.info("**** Entered username and password ****")

@when(u'I click the login button')
def step_impl(context):
    context.login_page.click_login()
    import time

@then(u'I should be logged in successfully')
def step_impl(context):
    # simple validation
    assert "inventory" in context.driver.current_url
    logger.info("**** Logged in successfully ****")

@given(u'I am logged in to SwagLabs')
def step_impl(context):
    # This runs existing steps exactly as if they were in the feature file
    context.execute_steps(u'''
        Given I launch the SwagLabs website
        When I enter username "standard_user" and password "secret_sauce"
        And I click the login button
    ''')