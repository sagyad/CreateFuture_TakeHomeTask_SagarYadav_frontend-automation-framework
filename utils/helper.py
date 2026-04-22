import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def highlight(driver, element, duration=0.3, color="yellow", border="3px solid red"):
    """Highlights a web element temporarily — visual tracking like UiPath"""
    original_style = element.get_attribute("style") or ""
    driver.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        f"background: {color}; border: {border};"
    )
    time.sleep(duration)
    driver.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        original_style
    )
