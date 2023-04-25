from pages.base_page import Page


class CartPage(Page):

    def verify_cart_opened(self, verify_pageopened):
        self.verify_url_contains_query(verify_pageopened)
