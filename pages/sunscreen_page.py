from selenium.webdriver.common.by import By
from pages.base_page import Page


class SunscreenPage(Page):
    FIRST_PROD_VISIBLE = (By.CSS_SELECTOR, "#product-grid .card-wrapper")

    def verify_first_prod_visible(self):
        self.wait_for_element_appear(*self.FIRST_PROD_VISIBLE).is_displayed()
