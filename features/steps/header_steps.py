from behave import given, when, then
from support.logger import logger


@when('Click on {shop_category} in header shop categories')
def click_header_shop_category(context, shop_category):
    logger.info(f'Inputting text {shop_category}')
    context.app.header.click_header_shop_category(shop_category)


@when('Click on CureSkin logo in the header')
def click_header_logo(context):
    context.app.header.click_header_logo()


@when('Click header search button')
def click_search_button(context):
    context.app.header.search_btn_visible()
    context.app.header.click_header_search_btn()


@when('Click search input button')
def click_input_search_btn(context):
    context.app.search_results_page.click_input_search_btn()


@when('Store first item info')
def store_first_item_info(context):
    context.app.search_results_page.store_first_item_info()


@when('Input text {user_text}')
def user_text_input(context, user_text):
    context.app.header.user_text_input(user_text)
