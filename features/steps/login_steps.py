from behave import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from OpenCartDemoSimulation.utilities.configurations import user_opencart_credentials


@given('I open the OpenCart login page')
def step_impl(context):
    #login_page = LoginPage(context.driver)
    context.login_page.open_menu_myaccount()
    if context.login_page.check_if_logout_button():
        context.login_page.get_logout_button().click()
        context.login_page.open_menu_myaccount()
    context.login_page.open_login_page()


@when('I enter valid username and password in the login form')
def step_impl(context):
    email = user_opencart_credentials["email"]
    password = user_opencart_credentials["password"]
    context.login_page.enter_credentials(email, password)


@when('I submit the login form')
def step_impl(context):
    context.login_page.click_submit()


@then('I should be redirected to my account dashboard')
def step_impl(context):
    expected_title = "My Account"
    WebDriverWait(context.driver, 10).until(
                expected_conditions.title_is(expected_title)
            )
    assert context.driver.title == expected_title, "Login wasn't made successfully "
    context.logger.info("Assertion Passed: login was made successfully")

    
@when('I enter email "{email}" and password "{password}" in the login form')
def step_impl(context,email,password):
    if email == 'EMPTY':
        email = ""
    if password == 'EMPTY':
        password = ""
    context.login_page.enter_credentials(email, password)


@then('I should see an error message saying "Warning: No match for E-Mail Address and/or Password."')
def step_impl(context):
    assert "Warning: No match for E-Mail Address and/or Password." in context.login_page.get_login_error(), f"AssertionError: Expected 'Warning: No match for E-Mail Address and/or Password.', but got '{context.login_page.get_login_error()}'"
    context.logger.info("Assertion Passed: Invalid login error message was displayed.")