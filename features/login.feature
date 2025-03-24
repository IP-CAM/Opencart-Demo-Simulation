Feature: User Authentication

    Background: 
        Given I open the OpenCart login page 

    @browser
    Scenario: Verify login with valid credentials
        When I enter valid username and password in the login form
        And I submit the login form
        Then I should be redirected to my account dashboard
    
    @browser
    Scenario: Verify login with invalid credentials
        When I enter invalid username and password in the login form
        And I submit the login form
        Then I should see an error message saying "Warning: No match for E-Mail Address and/or Password."
    
    @browser
    Scenario: Verify login with empty credentials
        When I submit the login form
        Then I should see an error message saying "Warning: No match for E-Mail Address and/or Password."