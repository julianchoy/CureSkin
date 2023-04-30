from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    DISPLAYED_ITEM_NAME = (By.CSS_SELECTOR, "td .link")
    DISPLAYED_ITEM_PRICE = (By.CSS_SELECTOR, ".price--end bdi")
    REMOVE_BTN = (By.CSS_SELECTOR, "[name='minus']")
    VERIFY_CART_EMPTY = (By.CSS_SELECTOR, ".cart__empty-text")

    def verify_cart_opened(self, verify_pageopened):
        self.verify_url_contains_query(verify_pageopened)

    def verify_item(self):
        self.verify_text(self.driver.store_name, *self.DISPLAYED_ITEM_NAME)

    def verify_price(self):
        self.verify_text(self.driver.store_price, *self.DISPLAYED_ITEM_PRICE)

    def click_remove_btn(self):
        self.wait_for_element_click(*self.REMOVE_BTN)

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.VERIFY_CART_EMPTY)
