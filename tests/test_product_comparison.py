from OpenCartDemoSimulation.pageObjects.ProductsPage import ProductsPage
from OpenCartDemoSimulation.pageObjects.ProductComparison import ProductComparison
from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class TestProductComparison(BaseClass):

    def test_1_verify_items(self):
        #TC1 - Verify if the items in comparison list are the correct ones
        logger = self.getLogger()
        products_page = ProductsPage(self.driver)
        product_comparison_page = ProductComparison(self.driver)
        products_page.click_category_phone()
        products = products_page.get_products()
        expected_products = []
        for product in products:
            product_title = products_page.get_product_name(product).text
            expected_products.append(product_title)
            products_page.click_product_add_to_comparison(product)
        #print(expected_products)
        products_page.click_product_compare_button()
        products_comparison = []
        products_comparison_list = product_comparison_page.get_products()
        for product_comparison in products_comparison_list:
            product_comparison_title = product_comparison_page.get_product_name(product_comparison)
            if product_comparison_title != "Remove":
                products_comparison.append(product_comparison_title)
        #print(products_comparison)
        assert set(expected_products) == set(products_comparison), f"AssertionError: Expected {expected_products}, but got {products_comparison}"
        logger.info("Assertion Passed: the products were correctly added to the comparison list")