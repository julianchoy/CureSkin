from behave import given, when, then


@then('Verify Face Wash page is shown')
def verify_face_wash(context):
    context.app.facewash_page.verify_facewash_opened('https://shop.cureskin.com/collections/face-wash')
