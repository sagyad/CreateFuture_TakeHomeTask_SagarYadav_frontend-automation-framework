# Feature: A high-level description of the functionality being tested
# Scenario: A specific test case written in Given/When/Then format
# Given: The precondition (setup)
# When: The action being performed
# Then: The expected outcome (assertion)

Feature: Login Functionality
  As a user of Sauce Demo
  I want to be able to log in with valid credentials
  So that I can access the product inventory

  # Scenario Outline: A template that runs the same scenario with DIFFERENT data
  # Examples table: Provides the data sets — each row is a separate test run
  # <placeholder>: Variables that get replaced with values from the Examples table
  @wip
  Scenario Outline: Login with different credentials
    Given I am on the login page
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then I should see the "<expected_result>"

    Examples:
      | username        | password     | expected_result |
      | standard_user   | secret_sauce | inventory page  |
      | locked_out_user | secret_sauce | error message   |

  @wip
  Scenario: Login with empty credentials
    Given I am on the login page
    When I enter username "" and password ""
    And I click the login button
    Then I should see the "error message"
