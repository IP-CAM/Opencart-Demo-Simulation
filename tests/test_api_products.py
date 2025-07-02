import requests

from OpenCartDemoSimulation.utilities.configurations import getConfig, get_headers, send_get_request, getQuery
from OpenCartDemoSimulation.utilities.resources import ApiResources

def test_name_price():
    ## sends a get request to the API requesting all the products from category 24 so it can compare the name and price with the ones stored in the DB to see if API is bringing correct data
    category = "24"
    url = getConfig()['API']['endpoint']+ApiResources.products_category+category
    # print(url)
    headers = get_headers()
    # print(headers)
    response = send_get_request(url,headers)
    json_response = response.json()
    products_in_response = [(product["id"],  product["name"],  product["price_excluding_tax_formated"])  for product in json_response["data"]]  # This loops through each dictionary in the "data" list, assigning it to the variable product one at a time. For each product dictionary, it extracts the value associated with the key "name" and price, creating a list with dictionary with all these names
    print(products_in_response)
    #[(28, 'HTC Touch HD', '$122.00'), (29, 'Palm Treo Pro', '$337.99'), (40, 'iPhone', '$123.20')]

    ###############
    # get the data from the same products in the DB
    query = "SELECT oc_product.product_id, oc_product_description.name, CONCAT('$',CONVERT(ROUND(oc_product.price, 2),CHAR))  FROM oc_product LEFT JOIN oc_product_description ON (oc_product.product_id = oc_product_description.product_id) LEFT JOIN oc_product_to_category ON (oc_product.product_id = oc_product_to_category.product_id) LEFT JOIN oc_category ON (oc_product_to_category.category_id = oc_category.category_id) WHERE oc_category.category_id = 24;"
    list_items = getQuery(query)
    print(list_items)
    #[(28, 'HTC Touch HD', '$100.00'), (29, 'Palm Treo Pro', '$279.99'), (40, 'iPhone', '$100.00')]

    assert set(products_in_response) == set(list_items), f"Expected {products_in_response} but got {list_items}"


