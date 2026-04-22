Feature: Shopping Cart Functionality
  As a logged-in user
  I want to add and remove items from my cart
  So that I can manage my purchases before checkout

  Background:
    Given I am logged in as a standard user

  Scenario: Add a product to the cart
    When I add "Sauce Labs Backpack" to the cart
    Then the cart badge should show 1 item

  Scenario: Add multiple products and verify cart
    When I add "Sauce Labs Backpack" to the cart
    And I add "Sauce Labs Bike Light" to the cart
    And I go to the cart
    Then I should see 2 items in the cart

  Scenario: Remove a product from the cart
    When I add "Sauce Labs Backpack" to the cart
    And I go to the cart
    And I remove the first item from the cart
    Then the cart should be empty
