import sys
import os

# Make sure we always add the actual project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from selenium import webdriver
from OpenCartDemoSimulation.pageObjects.LoginPage import LoginPage
import time
from OpenCartDemoSimulation.utilities.BaseClass import BaseClass

def before_all(context):
    #Initialize global variables before any test runs
    context.products_name = []  # persists across all scenarios

def before_scenario(context, scenario):
    if "browser" in scenario.tags:
        # Initialize WebDriver here
        # IMPORTANT: Because of the fixes to skip recaptcha, before runing the tests, all the Chrome windows need to be closed: taskkill /IM chrome.exe /F (windows command)     
        options = webdriver.ChromeOptions()

        try:
            context.driver = webdriver.Chrome(options=options)
            context.driver.get("http://localhost/opencart/")
            context.login_page = LoginPage(context.driver)
            context.base_class = BaseClass()
            context.logger = context.base_class.getLogger()

        except Exception as e:
            print(f"🚨 Error starting Chrome WebDriver: {e}")

   

def after_scenario(context, scenario):
    if "browser" in scenario.tags:
        # Clean up the WebDriver after the scenario
        if context.driver:
            context.driver.quit()