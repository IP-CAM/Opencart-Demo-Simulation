from selenium.webdriver.common.by import By

from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class ProductComparison(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "#product-compare table tr:first-child td:nth-child(n+2)") #selects all <td> elements from the second one onward (so it excludes the first cell which contains "Product").
    products_name = (By.CSS_SELECTOR, "a")
    add_to_cart_button = (By.CSS_SELECTOR,"form #button-confirm")
    remove_button = (By.CSS_SELECTOR, "form a")


    def get_products(self):
        return self.driver.find_elements(*ProductComparison.products)

    def get_product_name(self,product):
        return product.find_element(*ProductComparison.products_name).text

    def click_add_to_cart_button(self,product):
        return product.find_element(*ProductComparison.add_to_cart_button).click()

    def click_remove_button(self,product):
        return product.find_element(*ProductComparison.remove_button).click()




