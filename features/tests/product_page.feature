# Created by julian.choy at 4/23/23
Feature: Product Page

  Scenario: User can add product to cart
    Given Open CureSkin Shop Page
    When Close popup
    And Click on first product
    And Click on Add to Cart
    Then Verify Cart pop up visible
    When Click on View Cart
    Then Verify Cart Page is opened