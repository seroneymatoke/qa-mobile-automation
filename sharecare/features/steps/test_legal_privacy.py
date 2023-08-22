"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 26.11.21
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from behave import given, then

from sharecare.keywords.android.android_locator_keywords import legal_privacy


@given(u'the user taps legal and privacy')
def tap_legal_privacy(context):
    if 'android' in context.config.userdata.get('platform'):
        context.settings.tap_legal_privacy()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'the user validates page elements on legal and privacy')
def verify_page_elements(context):
    time.sleep(10)
    if 'android' in context.config.userdata.get('platform'):
        assert False not in context.legal_privacy.validate_legal_prigvacy_page()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given("user taps on data download")
def tap_data_download(context):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.tap_element(legal_privacy['_DATA_DOWNLOAD_'])
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'the user should be able to download tracker data')
def download_tracker(context):
    if 'android' in context.config.userdata.get('platform'):
        context.legal_privacy.download_tracker_data()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')
