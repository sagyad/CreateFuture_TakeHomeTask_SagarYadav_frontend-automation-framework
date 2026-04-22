"""
BasePage: The parent class for ALL page objects.
Common methods - (click, type, wait) # Update this list when new methods are added for clear visibility
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,Config.EXPLICIT_WAIT_TIMEOUT)

    def find_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
