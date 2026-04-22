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
    ERROR_MESSAGE = (By.CSS_SELECTOR,"[data-test='error']")

def enter_username(self,username):
    self.enter_text(self.USERNAME_FIELD,username)

def enter_password(self,password):
    self.enter_password(self.PASSWORD_FIELD,password)

def click_login(self):
    self.click(self.LOGIN_BUTTON)

def login(self,username,password):
    """"""