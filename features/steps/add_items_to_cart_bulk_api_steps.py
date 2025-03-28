from behave import *
from utilities.configurations import *
from OpenCartDemoSimulation.utilities.resources import ApiResources
from utilities.payload import *

@given('I have a valid bulk add-to-cart API endpoint')
def step_impl(context):
    context.url = getConfig()['API']['endpoint']+ApiResources.add_items_to_cart_bulk
    context.headers = get_headers()

@when('I send a POST request with a payload containing multiple items with their product IDs and quantities')
def step_impl(context):
    query = "select oc_product.product_id from oc_product left JOIN oc_product_to_category ON (oc_product.product_id = oc_product_to_category.product_id) left JOIN oc_category ON (oc_product_to_category.category_id = oc_category.category_id) left JOIN oc_category_description ON (oc_category.category_id = oc_category_description.category_id) WHERE oc_category_description.name LIKE 'Phones%'"
    context.expected_items = buildPayLoadFromDB(query)
    context.response = send_post_request(context.url, context.headers, context.expected_items)
    #print(f"Expected items: {context.expected_items}") [{'product_id': 28, 'quantity': 2}, {'product_id': 29, 'quantity': 2}, {'product_id': 40, 'quantity': 2}]
    

@then('the API should return a 200 OK response')
def step_impl(context):
    context.status = context.response.status_code
    assert context.status == 200, f"Not expected response: {context.status}"
    
    
@then('the response should include the product id for each added item')
def step_impl(context):
    json_response = context.response.json()
    #print(f"Json response: {json_response}")
    id_products = [] 
    for product in context.expected_items:
        id_products.append(product["product_id"])
    
    assert isinstance(json_response['data']['product'], list), \
    "Expected a list of products but got a single product."
    
    products_list = json_response['data']['product']
    expected_count = len(id_products)  # The number of product IDs sent
    actual_count = len(products_list)
    assert actual_count == expected_count, f"Expected {expected_count} products but got {actual_count}"

    # Now, check if the product IDs are as expected.
    expected_ids = id_products
    actual_ids = {prod['product_id'] for prod in products_list}
    assert actual_ids == expected_ids, f"Expected product IDs {expected_ids}, but got {actual_ids}"
    
    