from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class CartPopupPage(Page):
    CART_POPUP_VISIBLE = (By.ID, "mini-cart")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "a.button--secondary")

    def cart_popup_visible(self):
        self.wait_for_element_appear(*self.CART_POPUP_VISIBLE)

    def click_view_cart_btn(self):
        self.wait_for_element_appear(*self.VIEW_CART_BTN)
        search_results = self.find_element(*self.VIEW_CART_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_results)
        actions.perform()
        self.wait_for_element_click(*self.VIEW_CART_BTN)
