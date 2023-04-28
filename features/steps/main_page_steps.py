from behave import given, when, then


@given('Open CureSkin Shop Page')
def open_cureskin(context):
    context.app.main_page.open_main_url()


@given('Open search results page for cure')
def open_cure_search(context):
    context.app.main_page.open_cure_search()


@when('Click on first product')
def click_first_product(context):
    context.app.main_page.click_first_product()


@when('Close popup')
def close_popup(context):
    context.app.main_page.close_popup()


@then('Verify user is taken to main page')
def verify_main_page(context):
    context.app.main_page.verify_main_page()
