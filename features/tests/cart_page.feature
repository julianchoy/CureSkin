# Created by julian.choy at 4/25/23
Feature: Cart Page

  Scenario: Verify item and price in cart are correct
    Given Open CureSkin Shop Page
    When Close popup
    And Click header search button
    And Input text SPF
    And Click search input button
    And Store first item info
    And Add first item
    And Click on View Cart
    Then Verify same item is present in cart
    And Verify price is same as shown in results

  Scenario: Update Cart Functionality
    Given Open CureSkin Shop Page
    When Close popup
    And Click header search button
    And Input text SPF
    And Click search input button
    And Add first item
    And Click on View Cart
    And Click on Remove button
    Then Verify cart is empty