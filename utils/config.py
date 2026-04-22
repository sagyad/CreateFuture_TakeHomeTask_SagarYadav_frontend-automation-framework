"""
Configuration file: Stores all project-wide settings in one place.
Single source of truth — change URLs, timeouts, browser here only.
"""

class Config:
    BASE_URL = "https://www.saucedemo.com/"
    BROWSE = "chrome"
    IMPLICIT_WAIT = 10 # in seconds - global wait for all element lookups
    EXPLICIT_WAIT_TIMEOUT  = 15 # seconds - max wait for specific condiction

    # Test credentials 
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    LOCKED_USERNAME = "locked_out_user" # To Test Scenario when user is locked out due to variours reasons.

class StatingCongif(Config):
    BASE_URL = "https://www.saucedemo.com/"

class ProductionCongif(Config):
    BASE_URL = "https://www.saucedemo.com/"
    IMPLICIT_WAIT = 15