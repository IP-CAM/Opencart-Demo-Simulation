import json
import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from OpenCartDemoSimulation.pageObjects.CartPage import CartPage
from OpenCartDemoSimulation.pageObjects.ProductsPage import ProductsPage
from OpenCartDemoSimulation.utilities.BaseClass import BaseClass

class TestCart(BaseClass):

    default_products = {"iPod Classic", "iPod Nano", "iPod Touch"}

    def test_1_verify_items_data(self):
        #TC1 - Verify if the items added to the cart have the same price and name displayed in products page
        logger = self.getLogger()
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        expected_cart = products_page.add_products_to_the_cart(self.default_products)

        #Check products in the cart
        cart_products = cart_page.get_products()
        cart_products_dict = {}
        for cart_product in cart_products:
            #print(f"Cart Products1: {cart_product.get_attribute("outerHTML")}")
            item_name = cart_page.get_product_title(cart_product)
            item_price = cart_page.get_product_price_unit(cart_product)
            item_quantity = int(cart_page.get_product_quantity(cart_product).get_attribute('value'))
            cart_products_dict[item_name] = [item_price,item_quantity]

        assert cart_products_dict == expected_cart, f"Expected {expected_cart} but got {cart_products_dict}" #the assertion of these two dictionaries doesn't consider the order of the elements
        logger.info("Assertion Passed: the products added to the cart match with the products in the cart.")


    @pytest.mark.parametrize("quantity", [9, 6])
    def test_2_verify_quantity_input(self, quantity):
        # TC 2 Change quantity typing number 9 and 6
        logger = self.getLogger()
        cart_page = CartPage(self.driver)
        products_page = ProductsPage(self.driver)
        products_page.add_products_to_the_cart(self.default_products)

        # Check products in the cart
        cart_products = cart_page.get_products()
        quantity_input = cart_page.get_product_quantity(cart_products[1])
        price_unit = self.convert_price_to_float(cart_page.get_product_price_unit(cart_products[1]))

        # quantity_input.clear()
        # quantity_input.send_keys(str(quantity))
        # cart_page.click_update_quantity_button(cart_products[1])
        cart_page.update_quantity(cart_products[1], quantity)
        time.sleep(3)

        # Re-fetch the cart products after the update, since this update re-renders the cart and causes the previously referenced element cart_products to become "stale."
        cart_products = cart_page.get_products()
        price_total = self.convert_price_to_float(cart_page.get_product_price_total(cart_products[1]))

        correct_total = price_unit * quantity
        assert price_total == correct_total , f"Expected total {correct_total} but got {price_total}"
        logger.info("Assertion Passed: the totals are correct after a change of quantity")


    def test_3_checkout_empty_cart_button(self):
        #TC3 - Verify checkout button is not displayed when cart is empty
        logger = self.getLogger()
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        products_page.add_products_to_the_cart(self.default_products)
        cart_page.remove_products_from_the_cart()

        assert len(cart_page.get_checkout_buttons()) == 0, "Checkout button is present when cart is empty."
        logger.info("Assertion Passed: Checkout button is not present when cart is empty")


    def test_4_remove_product(self):
        #TC4 - Test removing a product from the cart.
        logger = self.getLogger()
        #first add products
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        products_page.add_products_to_the_cart(self.default_products)
        #remove all the products
        cart_page.remove_products_from_the_cart()
        assert len(cart_page.get_products()) == 0
        logger.info("Assertion Passed: Products are being correctly removed.")

    def test_5_verify_total(self):
        #TC5 - Verify total is correct
        logger = self.getLogger()
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        expected_cart = products_page.add_products_to_the_cart(self.default_products)
        total_page = self.convert_price_to_float(cart_page.get_subtotal())
        print(expected_cart)
        price_total = 0
        # Using .items() method so I get both the key (product name) and the associated list of values
        for product, details in expected_cart.items():
            price = details[0]
            quantity = details[1]
            price_total += self.convert_price_to_float(price) * quantity
        print(price_total)

        assert total_page == price_total, f"Expected total {price_total} but got {total_page}"
        logger.info("Assertion Passed: Total amount is correct.")


