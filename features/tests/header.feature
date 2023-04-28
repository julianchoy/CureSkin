# Created by julian.choy at 4/25/23
Feature: Main Page

  Scenario: User can shop by product Face Washes
    Given Open CureSkin Shop Page
    When Click on Shop by Product in header shop categories
    And Click on Face Washes in side menu
    Then Verify Face Wash page is shown

  Scenario: User can shop by product Sunscreens
    Given Open CureSkin Shop Page
    When Click on Shop by Product in header shop categories
    And Click on Sunscreens in side menu
    Then Verify the first product in Sunscreen page

  Scenario: Top logo takes user to main page
    Given Open search results page for cure
    When Click on CureSkin logo in the header
    Then Verify user is taken to main page
