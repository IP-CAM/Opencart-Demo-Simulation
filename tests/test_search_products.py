import json
import sys
import time

from OpenCartDemoSimulation.pageObjects.ProductsPage import ProductsPage
from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class TestSearchProducts(BaseClass):

    def compare_dict_lists(self,list1, list2):
        # Put the dictionaries in a set and convert them to a JSON string with sorted keys in alphabetic order. Json dumps converts the dictionaries in strings so they're in an immutable format, so they can be put in a set to be compared easily, since the order won't matter
        set1 = {json.dumps(dic, sort_keys=True) for dic in list1}
        set2 = {json.dumps(dic, sort_keys=True) for dic in list2}
        return set1 == set2

    def test_1_enter_valid_product_name(self):
        #TC 1 Test search for valid product
        logger = self.getLogger()
        product = "ipod"
        expected_products = [
            {
                "name": "iPod Classic",
                "price": "$122.00"
            },
            {
                "name": "iPod Nano",
                "price": "$122.00"
            },
            {
                "name": "iPod Shuffle",
                "price": "$122.00"
            },
            {
                "name": "iPod Touch",
                "price": "$122.00"
            }
        ] #expected_products is list with many dictionaries inside
        logger.info(f"Starting product search test with product: {product}")

        products_page = ProductsPage(self.driver)
        products_page.search_for_product(product)
        products = products_page.get_products()
        products_displayed = []
        for product in products:
            product_displayed = {}
            product_name = products_page.get_product_name(product).text
            product_price = products_page.get_product_price(product).text
            product_displayed["name"] = product_name
            product_displayed["price"] = product_price
            #print(product_displayed)
            products_displayed.append(product_displayed)
        #print(products_displayed)
        logger.info(f"Displayed products: {products_displayed}")

        assert self.compare_dict_lists(expected_products, products_displayed), \
                f"Expected {expected_products}, but got {products_displayed}"
        logger.info("Assertion Passed: the displayed products match with the expected products.")


    def test_2_enter_invalid_product_name(self):
        # TC 2 Test search for valid product
        logger = self.getLogger()
        product = "xyz5441"
        logger.info(f"Starting invalid product search test with product: {product}")
        products_page = ProductsPage(self.driver)
        products_page.search_for_product(product)
        error_message = products_page.get_error_message().text
        assert error_message == "There is no product that matches the search criteria.", "Assertion Failed! Error message was not displayed"
        logger.info("Assertion Passed: error message %s was displayed.")

    def test_3_verify_category_menu(self):
        logger = self.getLogger()
        expected_products = [
            {
                "name": "HTC Touch HD",
                "price": "$122.00"
            },
            {
                "name": "iPhone",
                "price": "$123.20"
            },
            {
                "name": "Palm Treo Pro",
                "price": "$337.99"
            }
        ]  # expected_products is list with many dictionaries inside
        products_page = ProductsPage(self.driver)
        products_page.click_category_phone()
        products = products_page.get_products()
        products_displayed = []
        for product in products:
            product_displayed = {}
            product_name = products_page.get_product_name(product).text
            product_price = products_page.get_product_price(product).text
            product_displayed["name"] = product_name
            product_displayed["price"] = product_price
            # print(product_displayed)
            products_displayed.append(product_displayed)
        # print(products_displayed)
        logger.info(f"Displayed products: {products_displayed}")

        assert self.compare_dict_lists(expected_products, products_displayed), \
            f"Expected {expected_products}, but got {products_displayed}"
        logger.info("Assertion Passed: the displayed products match with the expected products.")







