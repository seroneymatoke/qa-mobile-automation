"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 16.03.22
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
import time

from behave import *

from sharecare.keywords.android.android_locator_keywords import home_screen, trackers


@given("user taps tracker")
def tap_tracker(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(home_screen['_HOME_TRACKER_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("user should be able to enable automatic tracking")
def enable_auto_tracking(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(trackers['_ACTIVATE_'])
        assert context.helper_functions.find(trackers['_GOOGLE_FIT_'])
        assert context.helper_functions.find(trackers['_FITBIT_'])
        assert context.helper_functions.find(trackers['_SAMSUNG_HEALTH_'])
        context.helper_functions.tap_element(trackers['_NXT_BUTTON_'])
        assert context.helper_functions.find(trackers['_SLEEP_'])
        assert context.helper_functions.find(trackers['_STEPS_'])
        context.helper_functions.tap_element(trackers['_SLEEP_'])
        context.helper_functions.tap_element(trackers['_STEPS_'])
        context.helper_functions.tap_element(trackers['_DONE_BUTTON_'])
        context.helper_functions.tap_element(trackers['_SKIP_TOOLTIP_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps add today's entry")
def tap_add_tracker(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(trackers['_ADD_ENTRIES_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('Platform unavailable')


@then("user should be able to submit a tracker")
def submit_tracker(context):
    if 'android' in context.config.userdata.get('platform'):
        choices = ['Y']
        choice = random.choice(choices)
        match choice:
            case 'Y':
                context.helper_functions.tap_element(trackers['_DRINK_YES_'])
                unit = random.randint(1, 10)
                context.helper_functions.tap_element(trackers['_SAVE_'])
                context.helper_functions.tap_element(trackers['_DRP_DWN_'])
                context.helper_functions.set_text_box_value(trackers['_DRINK_DROP_DOWN_'], str(unit))
                context.helper_functions.touch_by_coordinates(268, 915)
            case _:
                context.helper_functions.tap_element(trackers['_DRINK_NO_'])
                context.helper_functions.tap_element(trackers['_SAVE_'])
        context.helper_functions.tap_element(trackers['_TOP_DONE_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('Platform unavailable')
