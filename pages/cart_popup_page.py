from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPopupPage(Page):
    CART_POPUP_VISIBLE = (By.ID, "mini-cart")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "a.button--secondary")

    def cart_popup_visible(self):
        self.wait_for_element_appear(*self.CART_POPUP_VISIBLE)

    def click_view_cart_btn(self):
        self.wait_for_element_click(*self.VIEW_CART_BTN)
