# Created by julian.choy at 4/25/23
Feature: Product Page

  Scenario: User can add product to cart
    Given Open CureSkin Shop Page
    When Close popup
    And Click header search button
    And Input text SPF
    And Click search input button
    And Store first item info
    And Add first item
    And Click on View Cart
    Then Verify same item is present in cart
    Then Verify price is same as shown in results