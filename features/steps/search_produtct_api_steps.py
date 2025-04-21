from behave import *
from utilities.configurations import *
from OpenCartDemoSimulation.utilities.resources import ApiResources


@given('I have a valid API endpoint and keyword {product} for product search')
def step_impl(context,product):
    context.url = getConfig()['API']['endpoint']+ApiResources.search_product+product    
    context.headers = get_headers()
    
@given('I have a valid API endpoint and empty keyword for product search')
def step_impl(context):
    context.url = getConfig()['API']['endpoint']+ApiResources.search_product    
    context.headers = get_headers()

@when('I send a request to the product search API')
def step_impl(context):
    context.response = send_get_request(context.url, context.headers)


@then('the API should return a successful response')
def step_impl(context):
    context.status = context.response.status_code
    #print(context.status)
    assert context.status == 200, f"Not expected response: {context.status}"


@then('the response should contain the correct product details') #this step is running twice because of the two product examples in the scenario
def step_impl(context):
    logger = getLogger()
    json_response = context.response.json()
    
    products_in_response = [product["name"] for product in json_response["data"]] #This loops through each dictionary in the "data" list, assigning it to the variable product one at a time. For each product dictionary, it extracts the value associated with the key "name", creating a list with all these names

    # Append results to persistent list from `before_all`
    context.products_name.extend(products_in_response)

    print("RESPOSTA:", context.products_name)  # Debugging
    logger.info(f"Collected product names: {context.products_name}")

    expected_products = {"Sony VAIO", "Nikon D300"} # expected_products is a set, not a dictionary, because it doesn't have key-value pairs (where the keys act like indexes).
    # Ensure final assertion runs only when both products are collected
    if len(set(context.products_name)) == len(expected_products): #set() transforms the list into a set, allowing then a comparation not taking into consideration the order, or repeated values. Safer than comparing two lists 
        assert set(context.products_name) == expected_products, \
            f"Expected {expected_products}, but got {set(context.products_name)}" # the \ is just to line continuation character, just for better readability
            
@then('the response data should be empty') 
def step_impl(context):
    logger = getLogger()
    json_response = context.response.json()
    
    assert json_response["data"] == [], f"Expected empty list of products, but got {json_response['data']}"