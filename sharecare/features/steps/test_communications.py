"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 02.12.21
Purpose: Implement comms POM
Implementation: 
TestData: None required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from behave import given, when, then

from sharecare.keywords.android.android_locator_keywords import communication


@given("the user taps communications")
def tap_communications(context):
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_communications()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@when("the user taps on sms messaging")
def tap_sms(context):
    if 'android' in context.config.userdata.get('platform'):
        context.communications.tap_sms_messaging()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("the user should be able to enable or disable sms messaging")
def enable_disable_sms_messaging(context):
    if 'android' in context.config.userdata.get('platform'):
        context.communications.enable_disable_sms_messaging()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@when("the user taps on email subscriptions")
def tap_email_subscriptions(context):
    context.helper_functions.step_back()
    if 'android' in context.config.userdata.get('platform'):
        context.communications.tap_email_subscriptions()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("the user should be able to set and save their desired email preferences")
def set_submit_email_preferences(context):
    if 'android' in context.config.userdata.get('platform'):
        context.communications.submit_email_preferences()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@when("the user taps on push notifications")
def tap_push_notification(context):
    context.helper_functions.step_back()
    if 'android' in context.config.userdata.get('platform'):
        context.communications.tap_push_notifications()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("the user should be able to set push notification preferences")
def push_notifications_preferences(context):
    if 'android' in context.config.userdata.get('platform'):
        context.communications.parametrize_push_notifications()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("Email Subscriptions should open in a Webview")
def email_web_view(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.validate_element_presence(communication['_EMAIL_SUBSCRIPTIONS_WEBVIEW_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')