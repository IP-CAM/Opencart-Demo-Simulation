import sys
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from OpenCartDemoSimulation.pageObjects.LoginPage import LoginPage
from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    def login(self, email, password):
        """Reusable login function to avoid duplication."""
        login_page = LoginPage(self.driver)
        login_page.open_menu_myaccount()

        if login_page.check_if_logout_button():
            login_page.get_logout_button().click()
            login_page.open_menu_myaccount()

        login_page.open_login_page()
        login_page.enter_credentials(email, password)
        login_page.click_submit()

    def test_1_enter_valid_credentials(self):
        #TC 1 Test for valid username and password
        logger = self.getLogger()
        email = "caioaza@gmail.com"
        password = "1234"
        #time.sleep(5) #this sleep time helps to validate the verify human blockage
        try:
            self.login(email, password)
            expected_title = "My Account"
            WebDriverWait(self.driver, 10).until(
                expected_conditions.title_is(expected_title)
            )
            logger.info("Logging in with valid credentials. E-mail: %s / Password: %s", email, password)
            assert self.driver.title == expected_title, "Login wasn't made successfully "
            logger.info("Assertion Passed: login was made successfully")
        except AssertionError as e:
            logger.error("Assertion Failed! login wasn't made successfully")
            sys.stdout.flush()
            raise  # Re-raise the assertion error to ensure test failure is properly registered

    def test_2_enter_invalid_credentials(self):
        #TC 2 Test for invalid username and password
        logger = self.getLogger()
        email = "fgsdf@gmail.com"
        password = "sdfgsfdg"
        #time.sleep(5) #this sleep time helps to validate the verify human blockage
        try:
            self.login(email, password)
            time.sleep(2)
            login_page = LoginPage(self.driver)
            logger.info("Logging in with invalid credentials. E-mail: %s / Password: %s", email, password)
            assert "Warning: No match for E-Mail Address and/or Password." in login_page.get_login_error(), "Invalid login error message was displayed."
            logger.info("Assertion Passed: Invalid login error message was displayed.")
        except AssertionError as e:
            logger.error("Assertion Failed! Invalid login error message wasn't displayed.")
            sys.stdout.flush()
            raise  # Re-raise the assertion error to ensure test failure is properly registered

    def test_3_empty_credentials(self):
        #TC 3 Test for empty username and password
        logger = self.getLogger()
        time.sleep(5) #this sleep time helps to validate the verify human blockage
        try:
            login_page = LoginPage(self.driver)
            login_page.open_menu_myaccount()
            if login_page.check_if_logout_button():
                login_page.get_logout_button().click()
                login_page.open_menu_myaccount()
            login_page.open_login_page()
            login_page.click_submit()
            time.sleep(2)
            logger.info("Logging in with empty credentials.")
            assert "Warning: No match for E-Mail Address and/or Password." in login_page.get_login_error(), "Invalid login error message was displayed."
            logger.info("Assertion Passed: Invalid login error message was displayed.")
        except AssertionError as e:
            logger.error("Assertion Failed! Invalid login error message wasn't displayed.")
            sys.stdout.flush()
            raise  # Re-raise the assertion error to ensure test failure is properly registered


