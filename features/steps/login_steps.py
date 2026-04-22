from behave import given, when, then
from pages.login_page import LoginPage
from utils.config import Config

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get(Config.BASE_URL)
    context.login_page = LoginPage(context.driver)

@when(u'I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when(u'I enter username "" and password ""')
def step_impl(context):
    # Fields are already empty — nothing to type
    pass

@when(u'I click the login button')
def step_impl(context):
    context.login_page.click_login()

@then(u'I should see the "{expected_result}"')
def step_impl(context, expected_result):
    if expected_result == "inventory page":
        context.login_page.wait_for_url_contains("inventory")
        assert "inventory" in context.login_page.get_current_url(), \
            f"Expected inventory page but got: {context.login_page.get_current_url()}"

    elif expected_result == "error message":
        assert context.login_page.is_error_displayed(), \
            "Error message is not displayed"

