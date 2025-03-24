import configparser
import requests
import inspect
import logging
import os


def getConfig():
    config = configparser.ConfigParser()
    config.read('OpenCartDemoSimulation/utilities/properties.ini')
    return config

def get_headers():
    return {
        "X-Oc-Merchant-Id": "123", 
        "Accept": "application/json", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",  "Connection": "keep-alive"
    }

def send_get_request(url, headers):
    response = requests.get(url, headers=headers)
    return response

def getLogger():
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