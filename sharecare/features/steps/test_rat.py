"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 01.03.22
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# TouchAction(driver).tap(x=268, y=915).perform()

from behave import *

from sharecare.keywords.android.android_locator_keywords import rat, android_alert_buttons, home_screen


@given(u'user taps on take real age test')
def tap_welcome_rat(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(rat['_GET_STARTED_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'user should be able to start the real age test')
def verify_start_rat(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(rat['_SKIP_'])
        assert context.helper_functions.find(rat['_MALE_'])
        assert context.helper_functions.find(rat['_FEMALE_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'User taps pause')
def tap_pause(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(rat['_PAUSE_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'user should be able to pause survey')
def pause_survey(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(android_alert_buttons['_OK_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'user taps complete RAT')
def complete_rat(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(android_alert_buttons['_OK_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'user should be able to continue from where it was left off')
def cont_rat(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(rat['_TAKE_RAT_'])
        assert context.helper_functions.find(rat['_MALE_'])
        assert context.helper_functions.find(rat['_FEMALE_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'user taps update real age')
def update_rat(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(android_alert_buttons['_OK_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'user should be able see rat status')
def rat_status(context):
    # create algo for this
    if 'android' in context.config.userdata.get('platform'):
        assert context.rat.rat_status()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'user taps home')
def tap_home(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(home_screen['_HOME_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')
