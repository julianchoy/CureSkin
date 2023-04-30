from behave import given, when, then


@when('Click on {menu_option} in side menu')
def click_header_logo(context, menu_option):
    context.app.side_menu.click_side_menu(menu_option)


