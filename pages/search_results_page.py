from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class SearchResultsPage(Page):
    SEARCH_RESULT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.card-information__button')
    INPUT_SEARCH_BTN = (By.XPATH, "//button[contains(text(),' Search for')]")
    ITEM_NAME = (By.CSS_SELECTOR, ".card-information a")
    ITEM_PRICE = (By.CSS_SELECTOR, ".price-item--sale bdi")

    def verify_facewash_opened(self, verify_pageopened):
        self.verify_url_contains_query(verify_pageopened)

    def click_first_item(self):
        search_results = self.find_element(*self.SEARCH_RESULT_ADD_TO_CART_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_results)
        actions.click()
        actions.perform()

    def click_input_search_btn(self):
        self.wait_for_element_click(*self.INPUT_SEARCH_BTN)

    def store_first_item_info(self):
        self.driver.store_name = self.find_element(*self.ITEM_NAME).text
        self.driver.store_price = self.find_element(*self.ITEM_PRICE).text
