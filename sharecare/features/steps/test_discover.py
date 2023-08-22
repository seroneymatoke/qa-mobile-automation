"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 12.01.22
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time
from _testcapi import raise_exception

from behave import then, given, when
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys

from sharecare.keywords.android.android_locator_keywords import discover, settings_screen, language
from sharecare.test_data.test_data import select_random_choice, find_doc_city, find_doc_speciality


@given("the user taps Discover")
def tap_discover(context):
    if 'android' in context.config.userdata.get('platform'):
        context.discover.tap_discover()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("the user taps community well being")
def tap_community_well_being(context):
    if 'android' in context.config.userdata.get('platform'):
        context.discover.tap_community_well_being()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


# @ToDo - Should I create a generic function that does all assertions?
@then("community well being should open in a webview")
def open_communication_webview(context):
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.validate_element_presence(discover['_COMM_WELL_WEBVIEW_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps Inspirations")
def tap_inspirations(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.step_back()
        context.helper_functions.swipe_direction_android("down", 2)
        context.discover.tap_inspirations()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("inspirations should open in a Webview")
def open_inspiration_webview(context):
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.validate_element_presence(discover['_INSPIRATION_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps medication prices")
def tap_medication_prices(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.step_back()
        context.helper_functions.swipe_direction_android("up", 1)
        context.discover.tap_med_prices()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("medication prices should open in a Webview")
def verify_web_view(context):
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.find(discover['_MD_PRICES_WEBVIEW_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("the user taps find a doctor")
def tap_find_a_doc(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.swipe_direction_android("down", 4)
        context.helper_functions.tap_element(discover['_FIND_DOCTOR_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user enters city")
def enter_city(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.set_text_box_value(discover['_DOC_LOCATION_TXT_'], select_random_choice(find_doc_city))
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps search doctor")
def tap_search_doc(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(discover['_SEARCH_BTN_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("user matching doctors should be displayed")
def display_docs(context):
    if 'android' in context.config.userdata.get('platform'):
        #Todo - fix this
        assert context.helper_functions.find(discover['_SEARCH_RESULTS_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user enters speciality")
def enter_speciality(context):
    if 'android' in context.config.userdata.get('platform'):
        elem = context.helper_functions.find(discover['_FIND_DOC_WEBVIEW_'])
        # context.helper_functions.set_text_box_value(discover['_DOC_LOCATION_TXT_'], select_random_choice(find_doc_city))
        context.helper_functions.set_text_box_value(discover['_DOC_SPEC_TXT_'],
                                                    select_random_choice(find_doc_speciality))

    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps detail information")
def tap_doc_dtl_info(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(discover['_SEARCH_RESULTS_'])
        assert True
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("doctor detailed information should be displayed")
def display_dtl_info(context):
    if 'android' in context.config.userdata.get('platform'):
        #context.helper_functions.swipe_direction_android("up", 1)
        assert context.helper_functions.find(discover['_DOC_PHONE_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps add doctor to care")
def add_doctor_to_care(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(discover['_ADD_TO_CARE_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("doctor should be added to care")
def validate_doc_added(context):
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.find(discover['_REMOVE_FROM_CARE_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps health topics")
def tap_health_topics(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.swipe_direction_android("down", 3)
        context.helper_functions.tap_element(discover['_HEALTH_TOPICS_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user is on the main screen")
def verify_main_screen(context):
    if 'android' in context.config.userdata['platform']:
        assert context.helper_functions.find(discover['_TOPICS_WEBVIEW_'])
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@given("user taps follow")
def tap_follow(context):
    if 'android' in context.config.userdata['platform']:
        context.helper_functions.tap_element(discover['_FOLLOW_BTN_'])
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@then("user should be able to tap unfollow")
def tap_unfollow(context):
    if 'android' in context.config.userdata['platform']:
        context.helper_functions.tap_element(discover['_FOLLOWING_BTN_'])
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@given("user is on detailed view screen")
def tap_detailed(context):
    if 'android' in context.config.userdata['platform']:
        context.helper_functions.tap_element(discover['_IMG_HT_DTL_'])
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@given("user taps filter")
def tap_filter(context):
    if 'android' in context.config.userdata['platform']:
        context.helper_functions.step_back()
        context.helper_functions.tap_element(discover['_TOPICS_FILTER_'])
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@then("all filters should be available")
def verify_filters(context):
    if 'android' in context.config.userdata['platform']:
        assert context.helper_functions.find(discover['_ALL_TOPICS_RD_BTN_'])
        assert context.helper_functions.find(discover['_FOLLOWING_RD_BTN_'])
        context.helper_functions.step_back()
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@given("user taps languages")
def tap_languages(context):
    if 'android' in context.config.userdata['platform']:
        context.helper_functions.tap_element(settings_screen['_LANGUAGE_'])
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@given("user selects language")
def select_language(context):
    if 'android' in context.config.userdata['platform']:
        #Todo - PArameterize
        context.helper_functions.tap_element(language['_DE_'])
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)


@then("health topics shouldn't be available")
def verify_raise_error(context):
    if 'android' in context.config.userdata['platform']:
        context.helper_functions.swipe_direction_android("down", 3)
        context.discover.tap_health_topics()
        assert raise_exception
    elif 'ios' in context.config.userdata['platform']:
        print('ios')
    else:
        print(404)