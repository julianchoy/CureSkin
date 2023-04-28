from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    DISPLAYED_ITEM_NAME = (By.CSS_SELECTOR, "td .link")
    DISPLAYED_ITEM_PRICE = (By.CSS_SELECTOR, ".price--end bdi")

    def verify_cart_opened(self, verify_pageopened):
        self.verify_url_contains_query(verify_pageopened)

    def verify_item(self):
        self.verify_text(self.driver.store_name, *self.DISPLAYED_ITEM_NAME)

    def verify_price(self):
        self.verify_text(self.driver.store_price, *self.DISPLAYED_ITEM_PRICE)
