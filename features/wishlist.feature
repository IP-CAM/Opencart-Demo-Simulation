Feature: Wishlist Functionality

    # Background:
    #     Given the Wishlist is empty 

    @browser
    Scenario: Add Three Items to Wishlist While Logged In
        Given the user is logged in 
        #And the Wishlist is empty 
        When the user adds three products to the wishlist
        Then the wishlist should display the added products
        And number of wishlist items in the header should be three

    @skip
    Scenario: Prompt login when adding to wishlist while not logged in
        Given the user is not logged in 
        When the user tries to add a featured products to the wishlist
        Then the user should be prompted to log in
        And after logging in, the product should be added to the wishlist

    @skip
    Scenario: Add the same item twice to the wishlist
        Given the user is logged in 
        When the user adds the same item to the wishlist twice
        Then the whishlist should display the item only one time

    @skip
    Scenario: Add Item from Wishlist to the Cart
        Given the user is logged in 
        And the wishlist contains one or more items
        When the user adds one of the items to the cart
        Then the cart should contain that item
        And the item should still be present in the wishlist

    @skip
    Scenario: Remove item from wishlist
        Given the user is logged in 
        And the wishlist contains one or more items
        When the user deletes one item from wishlist 
        Then the item should not be in the wishlist