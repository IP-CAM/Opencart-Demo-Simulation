import time

import pytest

from OpenCartDemoSimulation.pageObjects.ProductsPage import ProductsPage
from OpenCartDemoSimulation.pageObjects.ProductComparison import ProductComparison
from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class TestProductComparison(BaseClass):




    def test_1_verify_items(self):
        #TC1 - Verify if the items in comparison list are the correct ones
        logger = self.getLogger()
        product_comparison_page = ProductComparison(self.driver)
        expected_products = product_comparison_page.add_products_comparison_list()
        products_comparison = []
        products_comparison_list = product_comparison_page.get_products()
        for product_comparison in products_comparison_list:
            product_comparison_title = product_comparison_page.get_product_name(product_comparison)
            if product_comparison_title != "Remove":
                products_comparison.append(product_comparison_title)
        #print(products_comparison)
        assert set(expected_products) == set(products_comparison), f"AssertionError: Expected {expected_products}, but got {products_comparison}"
        logger.info("Assertion Passed: the products were correctly added to the comparison list")


    def test_2_delete_items(self):
        #TC2 - Verify is the items are being correctly deleted from comparions products list
        logger = self.getLogger()
        product_comparison_page = ProductComparison(self.driver)
        product_comparison_page.add_products_comparison_list()
        product_comparison_list = product_comparison_page.get_products()
        for index, product_comparison in enumerate(product_comparison_list):
            product_comparison_title = product_comparison_page.get_product_name(product_comparison)
            if product_comparison_title == "iPhone":
                product_comparison_page.click_remove_button_by_index(index)
                break
        # Verify result
        products_comparison = []
        product_comparison_list = product_comparison_page.get_products()
        for product_comparison in product_comparison_list:
            product_comparison_title = product_comparison_page.get_product_name(product_comparison)
            if product_comparison_title != "Remove":
                products_comparison.append(product_comparison_title)
        expected_products_comparison_list = ['HTC Touch HD', 'Palm Treo Pro']
        assert set(products_comparison) == set(expected_products_comparison_list), f"AssertionError: Expected {expected_products_comparison_list}, but got {products_comparison}"
        logger.info("Assertion Passed: the product was correctly removed from the comparison list")





