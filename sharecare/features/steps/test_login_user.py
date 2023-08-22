import os
import string
import time
import random

from behave import *
from faker import Faker

from sharecare.features.steps.test_api_calls import create_sso_user, create_user, terminate_session
from sharecare.keywords.android.android_locator_keywords import error_messages_screen, error_messages, home_screen, \
    settings_screen
from sharecare.test_data.test_data import users, select_random_choice, country_code


# use_step_matcher("re") -enable only if using matchers
from sharecare.utilities.custom_logger import CustomLogger

user_account = []
logger = CustomLogger.custom_logger()

@given('"{user_type}" user clicks login')
def tap_login(context, user_type):
    """
    Load login Screen
    """
    if 'android' in context.config.userdata.get('platform'):
        context.login_screen.tap_login()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('the "{user_type}" user tries to log in')
def set_email_pass(context, user_type):
    """
    set username and password
    """
    if 'android' in context.config.userdata.get('platform'):
        print("Hello" + users[user_type]['email'])
        email = context.login_screen.enter_email(users[user_type]['email'])
        print(email)
        context.login_screen.enter_password(users[user_type]['password'])
        # time.sleep(5)
        context.login_screen.tap_login()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("an error message should be displayed")
def validate_error_message(context):
    """
    Error message check
    """
    print()
    # message = context.helper_functions.contains_content(error_messages_screen['_INVALID_CREDENTIALS_'],
    #                                                   error_messages['_INVALID_CREDENTIALS_'])
    # assert message
    # ToDo Fix Validation Issues here --- Check if element is visible
    if 'android' in context.config.userdata.get('platform'):
        if context.helper_functions.contains_content(error_messages_screen['_INVALID_CREDENTIALS_'],
                                                     error_messages['_INVALID_CREDENTIALS_']):
            message = context.helper_functions.contains_content(error_messages_screen['_INVALID_CREDENTIALS_'],
                                                                error_messages['_INVALID_CREDENTIALS_'])
            context.helper_functions.tap_element(error_messages_screen['_CLOSE_BTN_'])
            assert message
        elif context.helper_functions.contains_content(error_messages_screen['_INVALID_ERROR_'],
                                                       error_messages['_INVALID_EMAIL_']):
            message = context.helper_functions.contains_content(error_messages_screen['_INVALID_ERROR_'],
                                                                error_messages['_INVALID_EMAIL_'])
            assert message
        elif context.helper_functions.contains_content(error_messages_screen['_INVALID_ERROR_'],
                                                       error_messages['_MISSING_PASSWORD_']):
            message = context.helper_functions.contains_content(error_messages_screen['_INVALID_ERROR_'],
                                                                error_messages['_MISSING_PASSWORD_'])
            assert message
        else:
            assert False
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("the user should be able to see the home screen")
def validate_home_screen(context):
    """
    Validate Home Screen content
    """
    time.sleep(30)
    # ToDo - Add request for IDs to make it faster
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.validate_element_presence(home_screen['_NOTIFICATION_ICON_'])
        assert context.helper_functions.validate_element_presence(home_screen['_SEARCH_ICON_'])
        assert context.helper_functions.validate_element_presence(home_screen['_FILTER_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("the user taps you")
def tap_you(context):
    """
    Begn logout process
    """
    # time.sleep(5)
    if 'android' in context.config.userdata.get('platform'):
        context.you.tap_you()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@step("the user taps settings")
def tap_settings(context):
    """
    Click Settings
    """
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_settings()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@step("user validates the settings page")
def validate_settings_page(context):
    """
    Validate settings page
    """
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.validate_element_presence(settings_screen['_ACCOUNT_'])
        assert context.helper_functions.validate_element_presence(settings_screen['_APPEARANCE_'])
        assert context.helper_functions.validate_element_presence(settings_screen['_VIDEO_AUTOPLAY_'])
        assert context.helper_functions.validate_element_presence(settings_screen['_LEGAL_PRIVACY_'])
        assert context.helper_functions.validate_element_presence(settings_screen['_SIGN_OUT_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@step("user clicks sign out")
def complete_sign_out(context):
    """
    Click Sign out
    """
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_sign_out()
        context.helper_functions.android_default_ok()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('I tap on "{text}"')
def step_impl(context, text):
    context.helper_functions.tap_element_by_xpath(text)


@given("user logs in")
def login(context):
    # @todo - Create a separate function for this

    if 'cf' in context.config.userdata.get('label').lower():
        user = create_user()
        user.email ='cf1stg3@scqa.me'
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
        if 'android' in context.config.userdata.get('platform'):
            user = create_user()
            if 'prod' in context.config.userdata.get('env'):
                user.email = os.environ.get('PROD_USERNAME')
                user.password = os.environ.get('PROD_PASS')
            else:
                context.login_screen.tap_login()
                context.login_screen.enter_email(user.email)
                context.login_screen.enter_password(user.password)
                context.login_screen.tap_login()
        elif 'ios' in context.config.userdata.get('platform'):
            user = create_user()
            if 'prod' in context.config.userdata.get('env'):
                user.email = os.environ.get['PROD_USERNAME']
                user.password = os.environ.get['PROD_PASS']
            else:
                context.login_screen.tap_login_ios()
                context.login_screen.enter_email_ios(user.email)
                context.login_screen.enter_password_ios(user.password)
                context.login_screen.tap_login_ios()


@given("A Non US user logs in")
def login(context):
    country = select_random_choice(country_code)
    user = create_user(country)
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
        print('not found')


@given("user terminates session")
def terminate_login_session(context):
    user = terminate_session(user_account[0], user_account[1])
    user_account.clear()


@given("existing user logs in with {email}, and {password}")
def login(context, email, password):
    """
        Without user creation, existing user can log in
    """
    if 'android' in context.config.userdata.get('platform'):
        context.login_screen.tap_login()
        context.login_screen.enter_email(email)
        context.login_screen.enter_password(password)
        context.login_screen.tap_login()
    elif 'ios' in context.config.userdata.get('platform'):
        context.login_screen.tap_login_ios()
        context.login_screen.enter_email_ios(email)
        context.login_screen.enter_password_ios(password)
        context.login_screen.tap_login_ios()
    else:
        print('not found')


@given("blocking user logs in")
def login(context):
    user = create_user()
    if 'cf' in context.config.userdata.get('label').lower():
        user.email = 'cf1stg4@scqa.me'
    user_account.append(user.account_id)
    user_account.append(user.access_token)
    print(user_account)
    logger.info(user.bearerToken)
    faker = Faker()
    gen_pass = faker.bban()
    if 'android' in context.config.userdata.get('platform'):
        context.login_screen.tap_login()
        context.login_screen.enter_email(user.email)
        context.login_screen.enter_password(gen_pass)
        context.login_screen.tap_login()
    elif 'ios' in context.config.userdata.get('platform'):
        context.login_screen.tap_login_ios()
        context.login_screen.enter_email_ios(user.email)
        context.login_screen.enter_password_ios(gen_pass)
        context.login_screen.tap_login_ios()
    else:
        print('not found')



