from behave import given, when, then


@when('Click on View Cart')
def cart_popup_view_cart_btn(context):
    context.app.cart_popup_page.click_view_cart_btn()


@then('Verify Cart pop up visible')
def cart_popup_visible(context):
    context.app.cart_popup_page.cart_popup_visible()
