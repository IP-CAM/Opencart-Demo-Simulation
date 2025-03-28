#Static settings and environment variables.

import configparser
import requests
import inspect
import logging
import os

import mysql.connector 
from mysql.connector import Error



def getConfig():
    config = configparser.ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(base_dir, "properties.ini")
    config.read(config_file)
    return config

def get_headers():
    return {
        "X-Oc-Merchant-Id": "123", 
        "Accept": "application/json", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",  
        "Connection": "keep-alive",
        "X-Oc-Session": "80f1194132d731c4bc97ecf8a2"
    }

def send_get_request(url, headers):
    response = requests.get(url, headers=headers)
    return response

def send_post_request(url, headers, json_body ):
    response = requests.post(url, headers=headers, json=json_body)
    return response

connect_config = {
    'user' : getConfig()['SQL']['user'],
    'database' : getConfig()['SQL']['database'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
}

def getConnection():
    try: #we use try because if connection fails we need to know the error
        conn = mysql.connector.connect(**connect_config) #the ** tell it's nothing but a dicitonary
        if conn.is_connected():
            print("Connection successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn = getConnection()
    #cursor executes statements to communicate with the MySQL database
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


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