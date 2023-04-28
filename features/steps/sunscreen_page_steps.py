from behave import given, when, then


@then("Verify the first product in Sunscreen page")
def verify_first_prod_visible(context):
    context.app.sunscreen_page.verify_first_prod_visible()
