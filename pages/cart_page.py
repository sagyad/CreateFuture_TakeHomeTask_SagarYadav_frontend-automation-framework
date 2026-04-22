"""
CartPage: Handles all interactions with the shopping cart.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # ===== LOCATORS =====
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[id^='remove']")
    # CSS: button[id^='remove'] means button whose id STARTS WITH 'remove'
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    @staticmethod
    def get_add_to_cart_button_locator(product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"add-to-cart-{formatted_name}")

    def add_product_to_cart(self, product_name):
        """Adds a specific product to the cart from the inventory page."""
        locator = self.get_add_to_cart_button_locator(product_name)
        self.click_element(locator)

    def go_to_cart(self):
        """Clicks the cart icon to navigate to the cart page."""
        self.click_element(self.CART_ICON)

    def get_cart_item_count(self):
        """Returns the number shown on the cart badge (icon)."""
        try:
            return int(self.get_element_text(self.CART_BADGE))
        except Exception:
            return 0  # No badge means cart is empty

    def get_cart_item_names(self):
        """Returns names of all items currently in the cart."""
        elements = self.driver.find_elements(*self.CART_ITEM_NAME)
        return [el.text for el in elements]

    def remove_first_item(self):
        """Removes the first item from the cart."""
        self.click_element(self.REMOVE_BUTTON)

    def is_cart_empty(self):
        """Checks if the cart has no items."""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items) == 0

    def click_checkout(self):
        """Clicks the Checkout button."""
        self.click_element(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        """Clicks Continue Shopping to go back to products."""
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)

