from behave import given, when, then


@when('Add first item')
def click_first_search(context):
    context.app.search_results_page.click_first_item()
