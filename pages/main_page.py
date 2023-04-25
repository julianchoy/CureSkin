from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    FIRST_PROD_BTN = (By.CSS_SELECTOR, "div.card-wrapper")

    def open_main_url(self):
        self.open_url("https://shop.cureskin.com/")

    def click_first_product(self):
        self.click(*self.FIRST_PROD_BTN)
