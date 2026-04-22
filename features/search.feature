Feature: Product Search and Sort Functionality
  As a logged-in user
  I want to browse and sort products
  So that I can find items I want to purchase

  Background:
    # Background: Steps that run BEFORE every scenario in this feature file.
    # Avoids repeating the same setup steps in each scenario.
    Given I am logged in as a standard user

  Scenario: Verify all products are displayed
    When I am on the inventory page
    Then I should see 6 products listed

  Scenario: Sort products by price low to high
    When I sort products by "Price (low to high)"
    Then the products should be sorted by price in ascending order

  Scenario: Click on a specific product
    When I click on the product "Sauce Labs Backpack"
    Then I should see the product detail page
