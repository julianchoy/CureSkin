from behave import given, when, then


@when('Click on {menu_option} in side menu')
def click_header_logo(context, menu_option):
    context.app.side_menu.click_side_menu(menu_option)


@then('Verify Face Wash page is shown')
def verify_face_wash(context):
    context.app.search_results_page.verify_facewash_opened('https://shop.cureskin.com/collections/face-wash')