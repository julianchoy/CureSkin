from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    FIRST_PROD_BTN = (By.CSS_SELECTOR, "div.card-wrapper")
    POPUP_CLOSE_BTN = (By.CSS_SELECTOR, ".popup-close")
    DUMMY_CHAT_LOADED = (By.CSS_SELECTOR, "#dummy-chat-button-iframe")
    POPUP_OVERLAY = (By.CSS_SELECTOR, ".is-active")

    def open_main_url(self):
        self.open_url("https://shop.cureskin.com/")

    def open_cure_search(self):
        self.open_url("https://shop.cureskin.com/search?q=cure")

    def click_first_product(self):
        self.wait_for_element_click(*self.FIRST_PROD_BTN)

    def verify_main_page(self):
        self.verify_url_contains_query("https://shop.cureskin.com/")

    def close_popup(self):
        self.wait_for_element_appear(*self.POPUP_CLOSE_BTN)
        self.wait_for_element_click(*self.POPUP_CLOSE_BTN)
        self.wait_for_element_disappear(*self.POPUP_OVERLAY)

    def dummy_chat_loaded(self):
        self.wait_for_element_appear(*self.DUMMY_CHAT_LOADED)
