import undetected_chromedriver as webdriver
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

        # Open chrome with user logged in to skip recaptcha
        user_data_dir = r"C:\Users\caioa\AppData\Local\Google\Chrome\User Data"
        profile_dir = "Default"

        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument(f"--profile-directory={profile_dir}")

        # Allow debugging port for remote debugging
        options.add_argument("--remote-debugging-port=9222")

        # Avoid crash issues
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")

        try:
            context.driver = webdriver.Chrome(options=options, version_main=133)
            context.driver.implicitly_wait(4)
            context.driver.get("https://demo.opencart.com/")
            context.login_page = LoginPage(context.driver)
            context.base_class = BaseClass()
            context.logger = context.base_class.getLogger()

        except Exception as e:
            print(f"🚨 Error starting Chrome WebDriver: {e}")
        
        # options = webdriver.ChromeOptions()
        # context.driver = webdriver.Chrome (options=options,                                       version_main=133)  # version 133 refers to chrome's version. Fix for incompatibility
        # context.driver.implicitly_wait(4)  # It tells Selenium to wait up to 4 seconds for an element to appear before throwing an exception (e.g., NoSuchElementException). It applies to all find_element or find_elements calls
        # time.sleep(7)  # fix for helping pass the humanity test
        # context.driver.get("https://demo.opencart.com/")
        # context.login_page = LoginPage(context.driver)
        # context.base_class = BaseClass()
        # context.logger = context.base_class.getLogger()
   

def after_scenario(context, scenario):
    if "browser" in scenario.tags:
        # Clean up the WebDriver after the scenario
        if context.driver:
            context.driver.quit()