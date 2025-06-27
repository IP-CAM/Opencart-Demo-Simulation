import time

from behave import *


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
        email = "caioaza@gmail.com"
        password = "123456"
        context.login_page.enter_credentials(email, password)
        context.login_page.click_submit()


@when('the user adds three products to the wishlist')
def step_impl(context):
    context.expected_products = context.wishlist.add_products_wishlist()


@then('the wishlist should display the added products')
def step_impl(context):
    context.wishlist.click_wishlist_button()

    products_wishlist = []
    products = context.wishlist.get_products()
    for product in products:
        print(product.get_attribute("outerHTML"))
        product_name = context.wishlist.get_product_name(product)
        print(product_name)
        products_wishlist.append(product_name)
    print(context.expected_products)
    print(products_wishlist)
    assert set(context.expected_products) == set(products_wishlist), f"AssertionError: Expected {context.expected_products}, but got {products_wishlist}"
    context.logger.info("Assertion Passed: the products were correctly added to the wishlist")



@then('number of wishlist items in the header should be three')
def step_impl(context):
    quantity = int(context.wishlist.get_products_quantity())
    assert quantity == 3, f"AssertionError: Expected 3 products in the whishlist but got {quantity}"


@given('the user is not logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is not logged in')


@when('the user tries to add a featured products to the wishlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user tries to add a featured products to the wishlist')


@then('the user should be prompted to log in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user should be prompted to log in')


@then('after logging in, the product should be added to the wishlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then after logging in, the product should be added to the wishlist')


@when('the user adds the same item to the wishlist twice')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user adds the same item to the wishlist twice')


@then('the whishlist should display the item only one time')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the whishlist should display the item only one time')


@given('the wishlist contains one or more items')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the wishlist contains one or more items')


@when('the user adds one of the items to the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user adds one of the items to the cart')


@then('the cart should contain that item')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cart should contain that item')


@then('the item should still be present in the wishlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the item should still be present in the wishlist')


@when('the user deletes one item from wishlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user deletes one item from wishlist')


@then('the item should not be in the wishlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the item should not be in the wishlist')