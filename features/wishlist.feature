Feature: Wishlist Functionality

    # Background:
    #     Given the Wishlist is empty 

    # @browser
    # Scenario: Add Three Items to Wishlist While Logged In
    #     Given the user is logged in 
    #     #And the Wishlist is empty 
    #     When the user adds three products to the wishlist
    #     Then the wishlist should display the added products
    #     And number of wishlist items in the header should be three

    @browser
    Scenario: Add the same item twice to the wishlist
        Given the user is logged in 
        When the user adds the same item to the wishlist twice
        Then the whishlist should display the item only one time

    # @browser
    # Scenario: Add Item from Wishlist to the Cart
    #     Given the user is logged in 
    #     And the user adds three products to the wishlist
    #     When the user adds one of the items to the cart
    #     Then the cart should contain that item
    #     And the item should still be present in the wishlist
    
    # @browser
    # Scenario: Prompt login when adding to wishlist while not logged in
    #     Given the user is not logged in 
    #     When the user tries to add products to the wishlist
    #     Then the user should be prompted to log in
    #     And after logging in, the product should be added to the wishlist

