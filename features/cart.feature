Feature: Shopping Cart

    Scenario Outline: User can add an item to the cart
        Given I am logged in to SwagLabs
        And I click "Add to Cart" on a "<item_name>"
        Then the cart icon should show 1 item

        Examples:
        | item_name   | 
        | bike-light      | 