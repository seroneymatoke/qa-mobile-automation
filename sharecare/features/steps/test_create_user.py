"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 08.11.21
Purpose:
Implementation: 
TestData: Faker Test data generation used to fill in params
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from behave import given, then, when
from faker import Faker
from random import randint

from sharecare.keywords.android.android_locator_keywords import welcome_screen, you_screen
from sharecare.test_data.test_data import registration

faker = Faker()


@given('user clicks create account')
def click_create_account(context):
    """
    Load registration screen
    """
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.click_create_account()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios stuff')
    else:
        print('platform unavailable')


@given('"{user_type}" user selects country')
def select_country(context, user_type):
    """
    Uses faker to get country
    """
    country = registration[user_type]['country']
    if 'android' in context.config.userdata.get('platform'):

        print(country)
        context.create_account.confirm_country(country)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('user clicks continue')
def click_continue(context):
    #time.sleep(5)
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.click_continue()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('user validates page elements')
def validate_page_elements(context):
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.validate_page_elements()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('"{user_type}" user enters first name')
def enter_first_name(context, user_type):
    first_name = registration[user_type]['first_name']
    if 'android' in context.config.userdata.get('platform'):
        context.first_name = context.create_account.set_first_name(first_name)
        print(first_name)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('"{user_type}" user enters last name')
def enter_last_name(context, user_type):
    last_name = registration[user_type]['last_name']
    if 'android' in context.config.userdata.get('platform'):
        context.last_name = context.create_account.set_last_name(last_name)
        print(context.last_name)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('"{user_type}" user enters email address')
def enter_email(context, user_type):
    email = registration[user_type]['email']
    print("Email address" + email)
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.set_email(email)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('user enters birth date')
def enter_birth_date(context):
    if 'android' in context.config.userdata.get('platform'):
        year = str(randint(1960, 2000))
        month = faker.month_name()
        day = str(randint(1, 28))
        print("YY: "+year)
        print("MM: " + month)
        print("DD: " + day)
        context.create_account.set_birth_date(year, month, day)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('user selects gender')
def select_gender(context):
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.set_gender()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('"{user_type}" user enters Zip Code')
def enter_zip_code(context, user_type):
    zip_code = registration[user_type]['zip_code']
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.set_zip_code(zip_code)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('"{user_type}" user enters new password')
def enter_password(context, user_type):
    password = registration[user_type]['password']
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.set_password(password)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('"{user_type}" user enters matching new password')
def enter_confirm_password(context, user_type):
    password = registration[user_type]['confirm_password']
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.set_confirm_password(password)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given('"{user_type}" user clicks agree to Sharecare\'s Terms and conditions')
def accept_terms_conditions(context, user_type):
    tnc = registration[user_type]['terms_conditions']
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.check_terms_and_conditions(tnc)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@when('user clicks create account')
def click_create(context):
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.click_create()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then('"{user_type}" user should be able to see the welcome screen')
def validate_welcome_screen(context, user_type):
    if 'android' in context.config.userdata.get('platform'):
        if 'Br' in registration[user_type]['country']:
            assert context.helper_functions.find(welcome_screen['_MORE_INFO_REQUIRED_BR_']).text
        else:
            assert context.helper_functions.validate_element_presence(welcome_screen['_WELCOME_GET_STARTED_'])
            assert context.helper_functions.validate_element_presence(welcome_screen['_NOT_NOW_'])

    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user clicks not now")
def tap_not_now(context):
    """
    user clicks not now
    """
    #time.sleep(10)
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(you_screen['_RAT_NOT_NOW_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("user should see home guided tooltips")
def validate_tool_tips(context):
    """
    Validate tooltips journey
    """
    if 'android' in context.config.userdata.get('platform'):
        context.guided_tooltips.validate_tool_tips()
        assert True
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
        context.guided_tooltips.validate_ios_tool_tips()
        assert True

    else:
        print('platform unavailable')


@then("entered passwords should be validated")
def validate_password_configs(context):
    # Validate passwords
    if 'android' in context.config.userdata.get('platform'):
        context.create_account.validate_passwords()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


