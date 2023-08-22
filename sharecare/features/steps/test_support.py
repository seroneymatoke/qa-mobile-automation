"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 18.02.22
Purpose: Implementation of Support Page
Implementation:
TestData: None required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from behave import given, then

from sharecare.keywords.android.android_locator_keywords import support


@given("user taps support")
def tap_support(context):
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_support()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("support should open in webview")
def support_webview(context):
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.validate_element_presence(support['_SUPPORT_WEBVIEW_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')
