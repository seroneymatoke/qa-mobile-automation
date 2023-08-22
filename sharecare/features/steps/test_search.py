"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 29.12.21
Purpose: 
Implementation: Random Faker Data
TestData: Random Faker Data
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from behave import given, when, then
from random_word import RandomWords

r = RandomWords()


@given("user taps search")
def tap_search(context):
    time.sleep(5)
    if 'android' in context.config.userdata.get('platform'):
        context.search_screen.tap_search()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@when("user enters search params")
def search_params(context):
    param = r.get_random_word()
    if 'android' in context.config.userdata.get('platform'):
        context.search_screen.do_search(str(param))
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then("search suggests the results for the query")
def search_not_null(context):
    if 'android' in context.config.userdata.get('platform'):
        context.search_screen.search_results()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')