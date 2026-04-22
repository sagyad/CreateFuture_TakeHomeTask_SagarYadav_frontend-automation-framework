from behave import when, then
from pages.cart_page import CartPage
from utils.config import Config

@when(u'I add "{product_name}" to the cart')
def step_impl(context, product_name):
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    context.cart_page.add_product_to_cart(product_name)

@then(u'the cart badge should show {count:d} item')
def step_impl(context, count):
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    actual_count = context.cart_page.get_cart_badge_count()
    assert actual_count == count, \
        f"Expected cart badge to show {count} but got: {actual_count}"

@when(u'I go to the cart')
def step_impl(context):
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    context.cart_page.go_to_cart()

@then(u'I should see {count:d} items in the cart')
def step_impl(context, count):
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    actual_count = context.cart_page.get_cart_item_count()
    assert actual_count == count, \
        f"Expected {count} items in cart but found: {actual_count}"

@when(u'I remove the first item from the cart')
def step_impl(context):
    context.cart_page.remove_first_item()

@then(u'the cart should be empty')
def step_impl(context):
    assert context.cart_page.is_cart_empty(), \
        "Cart is not empty"
    assert not context.cart_page.is_cart_badge_displayed(), \
        "Cart badge is still showing"

