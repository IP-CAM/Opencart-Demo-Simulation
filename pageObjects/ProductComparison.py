from selenium.webdriver.common.by import By

from OpenCartDemoSimulation.utilities.BaseClass import BaseClass


class ProductComparison(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "#product-compare table tr:first-child td:nth-child(n+2)") #selects all <td> elements from the second one onward (so it excludes the first cell which contains "Product").
    products_name = (By.CSS_SELECTOR, "a")
    add_to_cart_button = (By.CSS_SELECTOR,"form #button-confirm")
    remove_button = (By.XPATH, ".//a[contains(text(),'Remove')]")
    last_row = (By.CSS_SELECTOR, "#product-compare table tr")
    columns = (By.CSS_SELECTOR, "td")


    def get_products(self):
        return self.driver.find_elements(*ProductComparison.products)

    def get_product_name(self,product):
        return product.find_element(*ProductComparison.products_name).text

    def click_add_to_cart_button(self,product):
        return product.find_element(*ProductComparison.add_to_cart_button).click()

    def click_remove_button_by_index(self, index):
        # Get the last row with the Remove buttons
        last_row = self.driver.find_elements(*ProductComparison.last_row)[-1]
        columns = last_row.find_elements(*ProductComparison.columns)[1:]  # Skip the first column
        if index < len(columns):
            remove_btn = columns[index].find_element(*ProductComparison.remove_button)
            self.safe_click(remove_btn)
        else:
            raise IndexError("Index out of range when trying to click Remove button")

    def add_products_comparison_list(self):
        from OpenCartDemoSimulation.pageObjects.ProductsPage import ProductsPage
        products_page = ProductsPage(self.driver)
        products_page.click_category_phone()
        products = products_page.get_products()
        expected_products = []
        for product in products:
            product_title = products_page.get_product_name(product).text
            expected_products.append(product_title)
            products_page.click_product_add_to_comparison(product)
        # print(expected_products)
        products_page.click_product_compare_button()
        return expected_products





