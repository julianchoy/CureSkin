from behave import given, when, then


@then('Verify Cart Page is opened')
def verify_page_opened(context):
    context.app.cart_page.verify_cart_opened('https://shop.cureskin.com/cart')
