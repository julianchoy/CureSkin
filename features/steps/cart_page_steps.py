from behave import given, when, then


@then('Verify Cart Page is opened')
def verify_page_opened(context):
    context.app.cart_page.verify_cart_opened('https://shop.cureskin.com/cart')


@then('Verify same item is present in cart')
def verify_item(context):
    context.app.cart_page.verify_item()


@then('Verify price is same as shown in results')
def verify_price(context):
    context.app.cart_page.verify_price()


@when('Click on Remove button')
def click_remove_btn(context):
    context.app.cart_page.click_remove_btn()


@then('Verify cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
