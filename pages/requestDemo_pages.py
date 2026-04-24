from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class RequestDemoPage(BasePage):
    # ==================== LOCATORS ====================
    REQUEST_DEMO_BUTTON = (By.XPATH, "//a[contains(text(), 'Book a demo') or contains(text(), 'Book a Demo')]")
    DEMO_FORM_HEADING = (By.XPATH, "//span[contains(text(), 'Book Your Demo Here')]")
    BUSINESS_EMAIL = (By.ID, "business-email")
    COMPANY = (By.ID, "company")
    INTEREST_DROPDOWN = (By.ID, "interest")
    COMMENTS = (By.ID, "comments")
    CONSENT_CHECKBOX = (By.ID, "consent-checkbox")
    CONSENT_TEXT = (By.CSS_SELECTOR, "label[for='consent-checkbox']")
    LETS_TALK_BUTTON = (By.XPATH, "//button[text()=\"Let's Talk\"]")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, ".confirmation-message")

    FIELD_MAP = {
        "Business Email": BUSINESS_EMAIL,
        "Company": COMPANY,
        "Interest": INTEREST_DROPDOWN,
        "Comments": COMMENTS,
    }


    # ==================== ACTIONS ====================
    def click_request_demo_button(self):
        self.click(self.REQUEST_DEMO_BUTTON)


    def is_demo_form_displayed(self):
        return self.is_displayed(self.DEMO_FORM_HEADING)


    def is_field_displayed(self, field_name):
        locator = self.FIELD_MAP.get(field_name)
        return self.is_displayed(locator)


    def enter_field_value(self, field_name, value):
        locator = self.FIELD_MAP.get(field_name)
        self.enter_text(locator, value)


    def select_interest(self, option_text):
        dropdown = self.find(self.INTEREST_DROPDOWN)
        Select(dropdown).select_by_visible_text(option_text)


    def enter_comments(self, text):
        self.enter_text(self.COMMENTS, text)


    def check_consent_checkbox(self):
        checkbox = self.find_clickable(self.CONSENT_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()


    def get_consent_text(self):
        return self.get_text(self.CONSENT_TEXT)


    def click_lets_talk_button(self):
        self.click(self.LETS_TALK_BUTTON)


    def is_lets_talk_button_visible(self):
        return self.is_displayed(self.LETS_TALK_BUTTON)


    def is_lets_talk_button_enabled(self):
        element = self.find(self.LETS_TALK_BUTTON)
        return element.is_enabled()


    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)