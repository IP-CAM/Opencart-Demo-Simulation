Feature: User Authentication

    Background: 
        Given I open the OpenCart login page 


    @browser
    Scenario: Verify login with valid credentials
        When I enter valid username and password in the login form
        And I submit the login form
        Then I should be redirected to my account dashboard


    @browser
    Scenario Outline: Verify login with invalid combinations of email and password
        When I enter email "<email>" and password "<password>" in the login form
        And I submit the login form
        Then I should see an error message saying "Warning: No match for E-Mail Address and/or Password."

        Examples:
            | email                 | password     |
            | EMPTY            | 123456 |
            | caioaza@gmail.com       |   EMPTY      |
            |    EMPTY          |   EMPTY     |
            | invalid@email.com     | 123456 |
            | caioaza@gmail.com       | wrongpass456 |
            | wrong@email.com       | wrongpass789 |
            