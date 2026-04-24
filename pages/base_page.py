"""
BasePage: The parent class for ALL page objects.
Common methods: find, click, enter_text, get_text, is_displayed, wait_for_url_contains, get_elements
All interactions include visual highlighting (UiPath-style element tracking)
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config
from utils.helper import highlight

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT_TIMEOUT)

    def find(self, locator):
        """Wait for element to be visible, highlight it, and return it"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        highlight(self.driver, element)
        return element

    def find_clickable(self, locator):
        """Wait for element to be clickable, highlight it, and return it"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        highlight(self.driver, element)
        return element

    def find_all(self, locator):
        """Wait for at least one element and return all matching elements (each highlighted)"""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        for element in elements:
            highlight(self.driver, element, duration=0.15)
        return elements

    def click(self, locator):
        """Wait for element to be clickable, highlight, then click"""
        element = self.find_clickable(locator)
        highlight(self.driver,element)
        element.click()

    def enter_text(self, locator, text):
        """Wait for element, highlight, clear it, then type text"""
        element = self.find(locator)
        highlight(self.driver, element)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_all_texts(self, locator):
        """Get text from all matching elements (each highlighted)"""
        elements = self.find_all(locator)
        return [element.text for element in elements]

    def is_displayed(self, locator):
        try:
            element = self.find(locator)
            return element.is_displayed()
        except:
            return False

    def wait_for_url_contains(self, text):
        """Wait until URL contains specific text"""
        self.wait.until(EC.url_contains(text))

    def get_current_url(self):
        """Return current page URL"""
        return self.driver.current_url

