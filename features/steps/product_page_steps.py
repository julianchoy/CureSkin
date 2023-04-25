from behave import given, when, then


@when('Click on Add to Cart')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()



