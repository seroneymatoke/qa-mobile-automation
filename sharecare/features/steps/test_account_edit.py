"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 21.12.21
Purpose: Implementing Settings -> Account
Implementation: Supporting iOS /Android
TestData: user object i.e. names, gender, password etc
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from behave import given, when, then


@given("the user taps account")
def tap_account(context):
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_account()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("user validates page information")
def validate_user_data(context):
    if 'android' in context.config.userdata.get('platform'):
        # assert False not in context.account.validate_user_data()
        context.account.validate_user_data()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps change profile photo")
def change_profile_photo(context):
    if 'android' in context.config.userdata.get('platform'):
        context.account.tap_change_profile_photo()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@when("user taps take photo")
def tap_take_photo(context):
    if 'android' in context.config.userdata.get('platform'):
        context.account.tap_take_photo()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("user should be able to take a new DP photo")
def save_photo(context):
    if 'android' in context.config.userdata.get('platform'):
        context.account.tap_camera_btn()
        context.account.tap_ok()
        time.sleep(30)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("user should be able to remove photo")
def remove_photo(context):
    if 'android' in context.config.userdata.get('platform'):
        context.account.tap_remove_photo()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')