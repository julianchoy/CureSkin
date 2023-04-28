from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page


class Header(Page):
    SHOP_CATEGORY = (By.XPATH, "//span[@class='label'][contains(text(), '{}')]")
    HEADER_LOGO = (By.CSS_SELECTOR, ".header__heading-link")
    HEADER_SEARCH_BTN = (By.CSS_SELECTOR, ".header__search")
    SEARCH_TXT_FIELD = (By.CSS_SELECTOR, "#Search-In-Modal")

    def click_header_shop_category(self, shop_category):
        shop_category_xpath = self.SHOP_CATEGORY[1].format(shop_category)
        self.wait_for_element_click(self.SHOP_CATEGORY[0], shop_category_xpath)

    def click_header_logo(self):
        self.wait_for_element_click(*self.HEADER_LOGO)

    def click_header_search_btn(self):
        self.wait_for_element_click(*self.HEADER_SEARCH_BTN)

    def user_text_input(self, user_input):
        self.input_text(user_input, *self.SEARCH_TXT_FIELD)