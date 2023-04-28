from pages.cart_popup_page import CartPopupPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.side_menu import ProductMenu
from pages.search_results_page import SearchResultsPage
from pages.sunscreen_page import SunscreenPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.product_page = ProductPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.cart_popup_page = CartPopupPage(self.driver)
        self.header = Header(self.driver)
        self.side_menu = ProductMenu(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sunscreen_page = SunscreenPage(self.driver)
