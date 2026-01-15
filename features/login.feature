# feature file

Feature: Login Functionality

    Scenario Outline: Login with various credentials
        Given I launch the SwagLabs website
        When I enter username "<username>" and password "<password>"
        And I click the login button
        Then I should be logged in successfully

        Examples:
        | username                   | password |
        | standard_user              | secret_sauce |

