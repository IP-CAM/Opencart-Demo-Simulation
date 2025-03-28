Feature: Verify Bulk Add to Cart API
# API Reference: https://opencart3-simple.api.opencart-api.com/demo/shopping-cart/#/Cart/cart_add_bulk_item

  Scenario: Successfully add multiple items to the cart in one call
    Given I have a valid bulk add-to-cart API endpoint
    When I send a POST request with a payload containing multiple items with their product IDs and quantities
    Then the API should return a 200 OK response
    And the response should include the product id for each added item
