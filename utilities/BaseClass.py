import inspect
import logging
import os

import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#This class is used to hold all the common utilities, like reusable functions that need to be available for several test cases

@pytest.mark.usefixtures("setup")
class BaseClass:

    def safe_click(self, locator):
        # This function Uses the click with javascript because the regular click is returning an error “element click intercepted” meaning that while Selenium found the button, something (like an overlay, modal, or even the page not being scrolled properly) is preventing the click from being executed normally
        # If normal click fails, use JavaScript to click the element
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(expected_conditions.element_to_be_clickable(locator))
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def is_mobile_view(self):
        #Check if the current window size is mobile (width ≤ 768px)."""
        width = self.driver.get_window_size()["width"]
        return width <= 768

    def convert_price_to_float(self,price_str):
        return float(price_str.replace(",", "").replace("$", "").strip())

    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    # def selectOptionByText(self, locator, text):
    #     dropdown = Select(locator)
    #     dropdown.select_by_visible_text(text)

    def getLogger(self):
        #this log will also generate a screenshot of the tests that failed because of the method to capture screen in conftest.py
        logger_name = inspect.stack()[1][3]  # Get the calling test function name
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reports")
        log_file = os.path.join(reports_dir, "logfile.log")  # Save in reports folder

        if not os.path.exists(reports_dir):  # Ensure reports folder exists
            os.makedirs(reports_dir)

        logger = logging.getLogger(logger_name)
        if not logger.handlers:  # Prevent duplicate handlers
            file_handler = logging.FileHandler(log_file, mode='a')  # Append mode
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
            file_handler.setFormatter(formatter)
            # Format: 2025-02-05 11:21:11,574 : WARNING : pyTests.test_logging :Something is in warning mode

            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)

        logger.propagate = False #prevent duplicate logs
        return logger