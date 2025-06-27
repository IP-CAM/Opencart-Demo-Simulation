import time

from selenium.webdriver.common.by import By

from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class Wishlist(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    wishlist_menu = (By.ID, "wishlist-total")
    products = (By.XPATH, "//div[@id='wishlist']//table[@class='table table-bordered table-hover']//tbody/tr")
    product_name = (By.XPATH, ".//td[2]/a")
    product_add_to_cart = (By.XPATH, "//td[6]//button")
    product_remove = (By.XPATH, "//td[6]//a")
    products_quantity = (By.CSS_SELECTOR, "#wishlist-total span")

    def get_products(self):
        return self.driver.find_elements(*Wishlist.products)

    def click_wishlist_button(self):
        return self.driver.find_element(*Wishlist.wishlist_menu).click()

    def get_product_name(self,product):
        return product.find_element(*Wishlist.product_name).text

    def click_add_to_cart(self,product):
        return product.find_element(*Wishlist.product_add_to_cart).click()

    def remove_product(self,product):
        return product.find_element(*Wishlist.product_remove).click()

    def get_products_quantity(self):
        text = self.driver.find_element(*Wishlist.products_quantity).text
        number = text.split("(")
        number = number[1].split(")")
        return number[0]

    def add_products_wishlist(self):
        from OpenCartDemoSimulation.pageObjects.ProductsPage import ProductsPage
        products_page = ProductsPage(self.driver)
        products_page.click_category_phone()
        products = products_page.get_products()
        expected_products = []
        for product in products:
            product_title = products_page.get_product_name(product).text
            expected_products.append(product_title)
            products_page.click_product_add_to_wishlist(product)
        return expected_products
