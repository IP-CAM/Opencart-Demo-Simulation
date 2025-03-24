Feature: Verify Product Search API Functionality
  # API Reference: https://opencart3-simple.api.opencart-api.com/demo/shopping-cart/#/Products/products.search
    
    @search_products_api
    Scenario Outline: Search for a product using the API
        Given I have a valid API endpoint and keyword <product> for product search
        When I send a request to the product search API
        Then the API should return a successful response
        And the response should contain the correct product details

            Examples:
            | product  |
            | sony     |
            | nikon    |