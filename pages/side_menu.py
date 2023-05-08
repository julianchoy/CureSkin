from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductMenu(Page):
    MENU_OPTION = (By.CSS_SELECTOR, "[data-title='{}']")
    HAM_MENU_OPTION = (By.XPATH, "//a[contains(text(), '{}')]")

    def click_side_menu(self,menu_option):
        shop_category_xpath = self.HAM_MENU_OPTION[1].format(menu_option)
        self.wait_for_element_click(self.HAM_MENU_OPTION[0], shop_category_xpath)

        # shop_category_xpath = self.MENU_OPTION[1].format(menu_option)
        # self.wait_for_element_click(self.MENU_OPTION[0], shop_category_xpath)