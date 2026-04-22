from behave import given, when, then
from selenium.webdriver.common.by import By
from utils.config import Config
from utils.helper import highlight, wait_and_find, wait_and_click

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get(Config.BASE_URL)
    wait_and_find(context.driver, (By.ID, "user-name"), Config.EXPLICIT_WAIT_TIMEOUT)

@when(u'I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    username_field = wait_and_find(context.driver, (By.ID, "user-name"), Config.EXPLICIT_WAIT_TIMEOUT)
    highlight(context.driver, username_field)
    username_field.send_keys(username)

    password_field = wait_and_find(context.driver, (By.ID, "password"), Config.EXPLICIT_WAIT_TIMEOUT)
    highlight(context.driver, password_field)
    password_field.send_keys(password)

@when(u'I enter username "" and password ""')
def step_impl(context):
    username_field = wait_and_find(context.driver, (By.ID, "user-name"), Config.EXPLICIT_WAIT_TIMEOUT)
    highlight(context.driver, username_field)

    password_field = wait_and_find(context.driver, (By.ID, "password"), Config.EXPLICIT_WAIT_TIMEOUT)
    highlight(context.driver, password_field)

@when(u'I click the login button')
def step_impl(context):
    login_button = wait_and_click(context.driver, (By.ID, "login-button"), Config.EXPLICIT_WAIT_TIMEOUT)
    highlight(context.driver, login_button)
    login_button.click()

@then(u'I should see the "{expected_result}"')
def step_impl(context, expected_result):
    if expected_result == "inventory page":
        # Wait for inventory page to load
        wait_and_find(context.driver, (By.CLASS_NAME, "inventory_list"), Config.EXPLICIT_WAIT_TIMEOUT)
        assert "inventory" in context.driver.current_url, \
            f"Expected inventory page but got: {context.driver.current_url}"

    elif expected_result == "error message":
        # Wait for error message to appear
        error_element = wait_and_find(context.driver, (By.CSS_SELECTOR, "[data-test='error']"), Config.EXPLICIT_WAIT_TIMEOUT)
        highlight(context.driver, error_element)
        assert error_element.is_displayed(), "Error message is not displayed"

