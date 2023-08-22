"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 23.11.21
Purpose: Implementing tests for about page
Implementation:
TestData: None required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from behave import given, then


@given(u'user clicks about')
def tap_about(context):
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_about_us()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'about opens in a webview')
def validate_about_page(context):
    if 'android' in context.config.userdata.get('platform'):
        context.about.about_page()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')