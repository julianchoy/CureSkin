from pages.cart_popup_page import CartPopupPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.product_page = ProductPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.cart_popup_page = CartPopupPage(self.driver)
