from behave import given, when, then
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utils.config import Config

# Background step — runs before every scenario in this feature
@given(u'I am logged in as a standard user')
def step_impl(context):
    context.driver.get(Config.BASE_URL)
    context.login_page = LoginPage(context.driver)
    context.login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    context.search_page = SearchPage(context.driver)

@when(u'I am on the inventory page')
def step_impl(context):
    context.search_page.wait_for_url_contains("inventory")
    assert context.search_page.is_inventory_page_loaded(), \
        "Inventory page is not loaded"

@then(u'I should see 6 products listed')
def step_impl(context):
    product_count = context.search_page.get_product_count()
    assert product_count == 6, \
        f"Expected 6 products but found: {product_count}"

@when(u'I sort products by "{sort_option}"')
def step_impl(context, sort_option):
    context.search_page.sort_products_by(sort_option)

@then(u'the products should be sorted by price in ascending order')
def step_impl(context):
    prices = context.search_page.get_all_prices()
    assert prices == sorted(prices), \
        f"Prices are not in ascending order: {prices}"

@when(u'I click on the product "{product_name}"')
def step_impl(context, product_name):
    context.search_page.click_product(product_name)

@then(u'I should see the product detail page')
def step_impl(context):
    assert context.search_page.is_product_detail_page_loaded(), \
        "Product detail page is not displayed"
    assert context.search_page.is_back_button_displayed(), \
        "Back to products button is not displayed"

