from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class ProductsPage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    search_product = (By.CSS_SELECTOR, "input[placeholder='Search']")
    search_product_button = (By.XPATH, "//button[@class='btn btn-light btn-lg']")
    products = (By.XPATH, "(//div[@class='product-thumb'])")
    product_name = (By.XPATH, "div/div/h4/a")
    product_price = (By.CSS_SELECTOR, ".price-new")
    error_message = (By.CSS_SELECTOR, "#product-search p")

    def get_search_product(self):
        return self.driver.find_element(*ProductsPage.search_product) #the * unpacks the tuple (By.CSS_SELECTOR, "input[placeholder='Search']") in two elements, since find_element expects two elements

    def click_search_product_button(self):
        return self.driver.find_element(*ProductsPage.search_product_button).click()

    def get_products(self):
        # wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        # products_list = wait.until(expected_conditions.element_to_be_clickable(*ProductsPage.products))
        # return products_list
        return self.driver.find_elements(*ProductsPage.products)

    def get_product_name(self, product):
        return product.find_element(*ProductsPage.product_name)

    def get_product_price(self, product):
        return product.find_element(*ProductsPage.product_price)

    def get_error_message(self):
        return self.driver.find_element(*ProductsPage.error_message).text()