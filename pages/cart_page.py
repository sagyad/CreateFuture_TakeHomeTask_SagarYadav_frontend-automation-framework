"""
CartPage: Encapsulates all elements and actions on the Inventory and Cart pages.
Handles: adding/removing products, cart badge, cart contents
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # ===== LOCATORS =====
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".cart_item .btn_secondary")

    def get_add_to_cart_button(self, product_name):
        """Generate the add-to-cart button locator for a specific product.
        Sauce Demo uses a naming pattern: add-to-cart-sauce-labs-backpack"""
        button_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        return (By.ID, button_id)

    def add_product_to_cart(self, product_name):
        """Click the Add to Cart button for a specific product"""
        add_button_locator = self.get_add_to_cart_button(product_name)
        self.click(add_button_locator)

    def get_cart_badge_count(self):
        """Return the number shown on the cart badge"""
        badge_text = self.get_text(self.CART_BADGE)
        return int(badge_text)

    def go_to_cart(self):
        """Click the cart icon to navigate to the cart page"""
        self.click(self.CART_LINK)

    def get_cart_item_count(self):
        """Return the number of items in the cart"""
        items = self.find_all(self.CART_ITEMS)
        return len(items)

    def remove_first_item(self):
        """Remove the first item from the cart"""
        self.click(self.REMOVE_BUTTON)

    def is_cart_empty(self):
        """Check if the cart has no items"""
        try:
            items = self.driver.find_elements(*self.CART_ITEMS)
            return len(items) == 0
        except:
            return True

    def is_cart_badge_displayed(self):
        """Check if cart badge is visible (hidden when cart is empty)"""
        try:
            self.driver.find_element(*self.CART_BADGE)
            return True
        except:
            return False
