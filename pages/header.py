from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Header(Page):
    HEADER_LOGO = (By.CSS_SELECTOR, ".header__heading-link")
    HEADER_SEARCH_BTN = (By.CSS_SELECTOR, ".header__icons .header__search")
    SEARCH_TXT_FIELD = (By.CSS_SELECTOR, "input.search__input.field__input[aria-controls='predictive-search-results-list']")
    POP_UP_OVERLAY = (By.CSS_SELECTOR, ".popup-overlay")
    SHOP_CATEGORY = (By.XPATH, "//span[@class='label'][contains(text(), '{}')]")
    VERIFY_MOBILE = (By.CSS_SELECTOR, ".menu-mobile--open")
    OPEN_HAM_MENU = (By.CSS_SELECTOR, ".icon-hamburger")
    HAM_SHOP_CATEGORY = (By.XPATH, "//span[@class='menu-drawer__menu-item list-menu__item animate-arrow "
                                   "focus-inset'][contains(text(), '{}')]")
    MOBILE_HEADER_SEARCH_BTN = (By.CSS_SELECTOR, ".header__icons .header__search")

    def click_header_shop_category(self, shop_category):
        self.wait_for_element_click(*self.OPEN_HAM_MENU)
        ham_shop_category_xpath = self.HAM_SHOP_CATEGORY[1].format(shop_category)
        self.wait_for_element_click(self.SHOP_CATEGORY[0], ham_shop_category_xpath)

    #     shop_category_xpath = self.SHOP_CATEGORY[1].format(shop_category)
    #     self.wait_for_element_click(self.SHOP_CATEGORY[0], shop_category_xpath)

    def click_header_logo(self):
        self.wait_for_element_click(*self.HEADER_LOGO)

    def click_header_search_btn(self):
        self.wait_for_element_click(*self.HEADER_SEARCH_BTN)

    def user_text_input(self, user_input):
        self.open_url(f"https://shop.cureskin.com/")
        # self.wait_for_element_appear(*self.SEARCH_TXT_FIELD)
        # self.input_text(user_input, *self.SEARCH_TXT_FIELD)

    def search_btn_visible(self):
        self.wait_for_element_appear(*self.HEADER_SEARCH_BTN)
