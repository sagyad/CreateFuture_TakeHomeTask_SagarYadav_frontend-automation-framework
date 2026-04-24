Feature: Request Demo for SauceLabs AU Capabilities
  As a Senior Automation Quality Engineer
  I want to request a demo of the SauceLabs AI-powered testing platform,
  So that I can evaluate and leverage AI-driven capabilities to enhance my automation testing strategy

#  Background:
#    Given I am logged in as a standard user

    Scenario: Navigate to Request a Demo Page
      Given I navigate to "https://saucelabs.com/" url
      When I click on Request a Demo Button
      Then I should see "Book Your Demo Here" form