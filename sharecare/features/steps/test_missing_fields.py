import time

from behave import *

from sharecare.features.steps.test_api_calls import *


@given('I create and logged in with missing field user')
def login_missing_field_user(context):
    """
    Load login Screen
    """
    user = create_sso_user_missing_fields(context)
    print(user.email + " " + user.password)
    if 'android' in context.config.userdata.get('platform'):
        context.login_screen.tap_login()
        context.login_screen.enter_email(user.email)
        context.login_screen.enter_password(user.password)
        context.login_screen.tap_login()
    elif 'ios' in context.config.userdata.get('platform'):
        context.login_screen.tap_login_ios()
        context.login_screen.enter_email_ios(user.email)
        context.login_screen.enter_password_ios(user.password)
        context.login_screen.tap_login_ios()
    else:
        print("Incorrect Env")



@step('the user should be able to see the missing fields info screen')
def missing_field_screens(context):
    """
    Load Missing fields screen
    """

    context.missing_field_screen.validate_missing_fields_page_elements()
    context.missing_field_screen.tap_next()
