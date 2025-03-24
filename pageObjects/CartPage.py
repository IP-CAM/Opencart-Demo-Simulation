from selenium.webdriver.common.by import By

from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class CartPage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "#output-cart table tbody tr")
    product_title = (By.CSS_SELECTOR, "a")
    product_quantity = (By.CSS_SELECTOR, "input[name='quantity']")
    product_price_unit = (By.CSS_SELECTOR, "td:nth-child(4)")
    product_price_total = (By.CSS_SELECTOR, "td:nth-child(5)")
    product_remove_button = (By.CSS_SELECTOR, "td:nth-child(3) a[aria-label='Remove']")
    subtotal = (By.CSS_SELECTOR, "#checkout-total tr:nth-child(1) td:nth-child(2)")

    def get_products(self):
        return self.driver.find_elements(*CartPage.products)

    def get_product_title(self, product):
        return product.find_element(*CartPage.product_title).text

    def get_product_quantity(self, product):
        return product.find_element(*CartPage.product_quantity).get_attribute('value')

    def get_product_price_unit(self, product):
        return product.find_element(*CartPage.product_price_unit).text

    def get_product_price_total(self, product):
        return product.find_element(*CartPage.product_price_total).text

    def click_product_remove_button(self, product):
        return product.find_element(*CartPage.product_remove_button).click()

    def get_subtotal(self):
        return self.driver.find_element(*CartPage.subtotal).text



