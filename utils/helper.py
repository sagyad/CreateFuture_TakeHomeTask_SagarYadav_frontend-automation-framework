import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_find(driver, locator, timeout=10):
    """Explicit wait — waits until element is present before returning it"""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def wait_and_click(driver, locator, timeout=10):
    """Explicit wait — waits until element is clickable before clicking"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def highlight(driver,element,duration=0.5,color="yellow",border="3px solid red"):
    """Highlights a web element temporarily — like UiPath visual tracking"""
    original_style = element.get_attribute("style")

    # Apply highlight style
    driver.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        f"background: {color}; border: {border};"
    )
    time.sleep(duration)

    # Restore original style
    driver.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        original_style
    )
