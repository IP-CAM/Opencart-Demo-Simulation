import time

from behave import *

from OpenCartDemoSimulation.utilities.configurations import user_opencart_credentials


@given('the Wishlist is empty')
def step_impl(context):
    context.quantity = int(context.wishlist.get_products_quantity())
    if context.quantity > 0:
        context.wishlist.click_wishlist_button()

        products = context.wishlist.get_products()
        for product in products:
            context.wishlist.remove_product(product)



@given('the user is logged in')
def step_impl(context):
    if not context.login_page.check_if_logout_button():
        context.login_page.open_menu_myaccount()
        context.login_page.open_login_page()
        email = user_opencart_credentials["email"]
        password = user_opencart_credentials["password"]
        context.login_page.enter_credentials(email, password)
        context.login_page.click_submit()

@when('the user tries to add products to the wishlist')
@step('the user adds three products to the wishlist')
def step_impl(context):
    context.expected_products = context.wishlist.add_products_wishlist("distinct")


@then('the wishlist should display the added products')
def step_impl(context):
    context.wishlist.click_wishlist_button()
    products_wishlist = context.wishlist.get_all_product_names()
    assert set(context.expected_products) == set(products_wishlist), f"AssertionError: Expected {context.expected_products}, but got {products_wishlist}"
    context.logger.info("Assertion Passed: the products were correctly added to the wishlist")



@then('number of wishlist items in the header should be three')
def step_impl(context):
    quantity = int(context.wishlist.get_products_quantity())
    assert quantity == 3, f"AssertionError: Expected 3 products in the whishlist but got {quantity}"


@given('the user is not logged in')
def step_impl(context):
    if not context.login_page.check_if_logout_button:
        context.login_page.get_logout_button().click()


@then('the user should be prompted to log in')
def step_impl(context):
    alert_text = context.wishlist.get_alert_login_text()
    assert "You must login or create an account" in alert_text, "AssertionError: User is not being asked to login."

@then('after logging in, the product should be added to the wishlist')
def step_impl(context):
    # First login
    context.login_page.open_menu_myaccount()
    if context.login_page.check_if_logout_button():
        context.login_page.get_logout_button().click()
        context.login_page.open_menu_myaccount()
    context.login_page.open_login_page()
    email = "caioaza@gmail.com"
    password = "123456"
    context.login_page.enter_credentials(email, password)
    context.login_page.click_submit()

   # Check wishlist
    time.sleep(1)
    context.wishlist.click_wishlist_button()
    products_wishlist = context.wishlist.get_all_product_names()
    assert set(context.expected_products) == set(
        products_wishlist), f"AssertionError: Expected {context.expected_products}, but got {products_wishlist}"
    context.logger.info("Assertion Passed: the products were correctly added to the wishlist")



@when('the user adds the same item to the wishlist twice')
def step_impl(context):
    context.expected_products = context.wishlist.add_products_wishlist("same")

@then('the whishlist should display the item only one time')
def step_impl(context):
    context.wishlist.click_wishlist_button()
    products = context.wishlist.get_all_product_names()
    assert products.count("iPhone") == 1, f"AssertionError: same item was displayed {count} times in the wishlist."


@when('the user adds one of the items to the cart')
def step_impl(context):
    context.wishlist.click_wishlist_button()
    products = context.wishlist.get_products()
    for product in products:
        product_name = context.wishlist.get_product_name(product)
        if product_name == "iPhone":
            context.wishlist.click_add_to_cart(product)
            break


@then('the cart should contain that item')
def step_impl(context):
    context.products_page.click_cart_button()
    products = context.cart_page.get_products()
    assert context.cart_page.contains_product("iPhone"), "AssertionError: cart doesn't have product added from wishlist"

@then('the item should still be present in the wishlist')
def step_impl(context):
    context.wishlist.click_wishlist_button()
    products = context.wishlist.get_products()
    assert context.wishlist.contains_product("iPhone"), "AssertionError: Product was removed from wishlist after being added to the cart"
    assert contain == "yes", "AssertionError: Product was removed from wishlist after being added to the cart"
