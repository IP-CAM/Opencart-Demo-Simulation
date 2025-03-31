from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from OpenCartDemoSimulation.utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    search_product = (By.CSS_SELECTOR, "input[placeholder='Search']")
    search_product_button = (By.XPATH, "//button[@class='btn btn-light btn-lg']")
    products = (By.XPATH, "//div[@class='product-thumb']")
    product_name = (By.XPATH, "div/div/h4/a")
    product_price = (By.CSS_SELECTOR, ".price-new")
    error_message = (By.CSS_SELECTOR, "#product-search p")
    category_phones = (By.XPATH, "//a[normalize-space()='Phones & PDAs']")
    menu_mobile = (By.CSS_SELECTOR, "button.navbar-toggler")
    #product_add_to_cart = (By.XPATH, ".//form//button[1]") #the .// enforces this element is a relative path from the parent element (product)
    product_add_to_cart = (By.CSS_SELECTOR, "div.button > button:first-of-type")
    cart_button = (By.CSS_SELECTOR, "a[title='Shopping Cart']")

    def get_search_product(self):
        return self.driver.find_element(*ProductsPage.search_product) #the * unpacks the tuple (By.CSS_SELECTOR, "input[placeholder='Search']") in two elements, since find_element expects two elements

    def click_search_product_button(self):
        return self.driver.find_element(*ProductsPage.search_product_button).click()

    def get_products(self):
        return self.driver.find_elements(*ProductsPage.products)

    def get_product_name(self, product):
        return product.find_element(*ProductsPage.product_name)

    def get_product_price(self, product):
        return product.find_element(*ProductsPage.product_price)

    def get_error_message(self):
        return self.driver.find_element(*ProductsPage.error_message)

    def click_menu_mobile(self):
        return self.driver.find_element(*ProductsPage.menu_mobile).click()

    def search_for_product(self, product):
        search_element = self.get_search_product()
        search_element.clear()
        search_element.send_keys(product)
        self.click_search_product_button()

    def click_category_phone(self):
        if self.is_mobile_view():
            self.click_menu_mobile()
        return self.driver.find_element(*ProductsPage.category_phones).click()

    def click_product_add_to_cart(self, product):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(product, 10)
        # Wait until the button is visible and clickable
        add_to_cart_button = wait.until(EC.element_to_be_clickable(ProductsPage.product_add_to_cart))

        try:
            add_to_cart_button.click()
        except Exception as e:
            # Using the click with javascript here because the regular click is returning an error “element click intercepted” meaning that while Selenium found the button, something (like an overlay, modal, or even the page not being scrolled properly) is preventing the click from being executed normally
            # If normal click fails, use JavaScript to click the element
            self.driver.execute_script("arguments[0].click();", add_to_cart_button)
        #self.safe_click(ProductsPage.product_add_to_cart)

    def click_cart_button(self):
        self.safe_click(ProductsPage.cart_button)

    def add_products_to_the_cart(self,products_to_add):
        product = "ipod"
        #products_page = ProductsPage(self.driver)
        self.search_for_product(product)
        products = self.get_products()
        expected_cart = {}
        # Add products to the cart and capture expected values before the click
        for product in products:
            product_title = self.get_product_name(product).text
            product_price = self.get_product_price(product).text
            product_quantity = 1
            if product_title in products_to_add:
                # Capture the data before clicking, avoiding stale element issues
                expected_cart[product_title] = [product_price, product_quantity]
                self.click_product_add_to_cart(product)
        # print(expected_cart) #{'iPod Classic': ['$122.00', 1], 'iPod Nano': ['$122.00', 1], 'iPod Touch': ['$122.00', 1]}
        # expected_cart is a dictionary where the product title is the key and the quantity and price form a list, used as value for that key
        self.click_cart_button()
        return expected_cart