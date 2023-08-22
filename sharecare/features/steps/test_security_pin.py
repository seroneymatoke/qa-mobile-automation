"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 18.12.21
Purpose: Set PIN configs
Implementation:
TestData: Valid login details Security PIN
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from behave import given, then, when

from sharecare.test_data.test_data import users


@given("user taps security pin")
def tap_security_pin(context):
    # Open Security PIN Screen
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_security_pin()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@when("user taps Security PIN switch")
def tap_security_pin_switch(context):
    if 'android' in context.config.userdata.get('platform'):
        context.security_pin.toggle_security_pin_btn()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'the "{user_type}" user should be able to set PIN')
def set_pin(context, user_type):
    if 'android' in context.config.userdata.get('platform'):
        context.security_pin.set_passcode(users[user_type]['passcode'], 2)
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'user taps auto lock')
def tap_auto_lock(context):
    if 'android' in context.config.userdata.get('platform'):
        context.security_pin.tap_auto_clock()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'the user should be able to set a time delay')
def set_time_delay(context):
    if 'android' in context.config.userdata.get('platform'):
        context.security_pin.set_auto_lock()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'user taps change security PIN')
def change_pin(context):
    raise NotImplementedError(u'STEP: Given user taps change security PIN')


@given(u'"{user_type}" user enters current PIN')
def enter_current_pin(context, user_type):
    raise NotImplementedError(u'STEP: Given user enters current PIN')


@given(u'the "{user_type}" user sets new PIN')
def set_new_pin(context, user_type):
    raise NotImplementedError(u'STEP: Given the user sets new PIN')


@then(u'user should be able to successful set new PIN')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user should be able to successful set new PIN')


@then(u'user should be able to disable PIN')
def disable_pin(context):
    raise NotImplementedError(u'STEP: Then user should be able to disable PIN')
