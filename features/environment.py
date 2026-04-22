import sys
import os
import time

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from selenium import webdriver
from utils.config import Config

def before_scenario(context, scenario):
    if Config.BROWSE.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif Config.BROWSE.lower() == "firefox":
        context.driver = webdriver.Firefox()

    context.driver.implicitly_wait(Config.IMPLICIT_WAIT)
    context.driver.maximize_window()
    # context.config_data = Config()

def after_scenario(context, scenario):
    # time.sleep(3)
    context.driver.quit()