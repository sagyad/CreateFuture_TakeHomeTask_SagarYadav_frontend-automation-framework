"""
SearchPage (Inventory Page): Represents the products listing page
that appears after successful login on Sauce Demo.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    # ===== LOCATORS =====
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_item_name")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    # Dynamic locator — we'll build XPath at runtime based on product name
    # XPath: A query language for selecting nodes in an XML/HTML document


def get_all_product_names(self):
    """Returns a list of all visible product names."""
    elements = self.driver.find_elements(*self.PRODUCT_TITLE)
    # The * operator UNPACKS the tuple: (By.CLASS_NAME, "inventory_item_name")
    # becomes two separate arguments: By.CLASS_NAME, "inventory_item_name"
    return [element.text for element in elements]
    # List comprehension: A concise way to create a list from a loop


def get_all_product_prices(self):
    """Returns a list of all product prices as floats."""
    elements = self.driver.find_elements(*self.PRODUCT_PRICES)
    return [float(el.text.replace("$", "")) for el in elements]


def sort_products(self, sort_option):
    """
    Selects a sort option from the dropdown.
    Select class: Selenium's built-in class for handling HTML <select> dropdowns.
    """
    from selenium.webdriver.support.ui import Select
    dropdown = self.find_element(self.SORT_DROPDOWN)
    select = Select(dropdown)
    select.select_by_visible_text(sort_option)


def click_product_by_name(self, product_name):
    """Clicks on a product using a dynamic XPath locator."""
    dynamic_locator = (By.XPATH, f"//div[text()='{product_name}']")
    # f-string: Python's string formatting — inserts the product_name variable
    self.click_element(dynamic_locator)


def is_inventory_page_displayed(self):
    """Verifies the inventory/products page is loaded."""
    return self.is_element_displayed(self.INVENTORY_LIST)


def get_product_count(self):
    """Returns the number of products displayed."""
    elements = self.driver.find_elements(*self.PRODUCT_TITLE)
    return len(elements)