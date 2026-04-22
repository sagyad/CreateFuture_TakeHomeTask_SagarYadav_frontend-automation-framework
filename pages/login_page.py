"""
LoginPage: Encapsulates all elements and actions on the Login page.
Each page in POM has:
  1. LOCATORS — how to find elements (stored as class variables)
  2. METHODS — actions a user can perform on this page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # ===== LOCATORS (Tuples) =====
    # Stored as class-level constants — easy to update if the UI changes
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Complete login flow — enter credentials and click login"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Return the error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        """Check if error message is visible"""
        return self.is_displayed(self.ERROR_MESSAGE)

