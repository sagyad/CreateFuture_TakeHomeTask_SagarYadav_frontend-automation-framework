"""
SearchPage (InventoryPage): Encapsulates all elements and actions on the Inventory page.
Handles: product listing, sorting, and product detail navigation
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage

class SearchPage(BasePage):
    # ===== LOCATORS =====
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_DETAIL_CONTAINER = (By.CLASS_NAME, "inventory_details_container")
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")

    def is_inventory_page_loaded(self):
        """Verify inventory page is loaded"""
        return self.is_displayed(self.INVENTORY_LIST)

    def get_product_count(self):
        """Return the number of products displayed"""
        products = self.find_all(self.INVENTORY_ITEMS)
        return len(products)

    def sort_products_by(self, sort_option):
        """Select a sort option from the dropdown"""
        dropdown = self.find(self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(sort_option)

    def get_all_prices(self):
        """Return all product prices as a list of floats"""
        price_texts = self.get_all_texts(self.ITEM_PRICES)
        # Remove "$" and convert to float e.g. "$29.99" -> 29.99
        return [float(price.replace("$", "")) for price in price_texts]

    def click_product(self, product_name):
        """Click on a specific product by its name"""
        product_locator = (By.LINK_TEXT, product_name)
        self.click(product_locator)

    def is_product_detail_page_loaded(self):
        """Verify product detail page is loaded"""
        return self.is_displayed(self.PRODUCT_DETAIL_CONTAINER)

    def is_back_button_displayed(self):
        """Verify back to products button is visible"""
        return self.is_displayed(self.BACK_TO_PRODUCTS_BUTTON)

