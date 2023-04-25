from behave import given, when, then


@given('Open CureSkin page')
def open_cureskin(context):
    context.app.main_page.open_main_url()


@when('Click on first product')
def click_first_product(context):
    context.app.main_page.click_first_product()
