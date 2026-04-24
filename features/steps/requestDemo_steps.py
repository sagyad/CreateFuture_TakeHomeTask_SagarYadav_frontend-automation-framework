from behave import given,when,then
from pages.requestDemo_pages import RequestDemoPage
from selenium import webdriver

@given(u'I navigate to "{url}" url')
def step_impl(context,url):
    context.driver.get(url)
    context.requestDemoPage = RequestDemoPage(context.driver)


@when(u'I click on Request a Demo Button')
def step_impl(context):
    context.requestDemoPage.click_request_demo_button()


@then(u'I should see "Book Your Demo Here" form')
def step_impl(context):
    assert context.requestDemoPage.is_demo_form_displayed()
