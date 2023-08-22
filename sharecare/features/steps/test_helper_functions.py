import time
import random

from behave import *
from faker import Faker
from selenium.webdriver import Keys

from sharecare.configs.config import base_url
from sharecare.test_data.test_data import select_random_choice, find_doc_speciality, find_doc_city

faker = Faker()


@then('user should see "{text}"')
def get_element_xpath(context, text):
    if 'android' in context.config.userdata.get('platform'):
        assert context.helper_functions.find_by_xpath(text)
    elif 'ios' in context.config.userdata.get('platform'):
        assert context.helper_functions.find_by_ios_xpath(text)
    else:
        print("Platform not found")


@given('user taps "{text}"')
def get_element_xpath(context, text):
    if 'android' in context.config.userdata.get('platform'):
        if text == 'Gender' or text == 'gender':
            text = random.choice(['Male', 'Female'])
            context.helper_functions.find_by_xpath(text).click()
        elif text == 'value':
            text = random.randint(0, 8)
            context.helper_functions.find_by_xpath(str(text)).click()
        else:
            context.helper_functions.find_by_xpath(text).click()
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
        # To handle closing Notifications
        if text == 'Gender' or text == 'gender':
            text = random.choice(['Male', 'Female'])
            context.helper_functions.find_by_ios_xpath(str(text)).click()
        elif text == 'value':
            text = random.randint(0, 8)
            context.helper_functions.find_by_ios_xpath(str(text)).click()
        elif text == 'Close':
            text = 'OK'
            context.helper_functions.find_by_ios_xpath(str(text)).click()
        else:
            context.helper_functions.find_by_ios_xpath(str(text)).click()
    else:
        print("Platform not found")
    #time out nonsense for sl
    pass


@then('user should see "{text}" is selected')
def get_element_xpath(context, text):
    if 'android' in context.config.userdata.get('platform'):
        result = context.helper_functions.find_by_xpath(text).get_attribute("checked")
        if result == 'True' or 'true':
            assert True
        else:
            return False
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user scrolls "{times}" times direction "{direction}"')
def scroll(context, times, direction):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.swipe_direction_android(direction, times)
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user goes back "{times}" times')
def step_back(context, times):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.step_back_x_times(times)
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user taps coordinates "{x}" and "{y}"')
def tap_coordinates(context, x, y):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.touch_by_coordinates(x, y)
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user waits for "{seconds}" seconds')
def time_delay(context, seconds):
    time.sleep(int(seconds))


@given("user activates app")
def activate_app(context):
    if 'android' in context.config.userdata.get('platform'):
        context.driver.activate_app('com.sharecare.realgreen')
    elif 'ios' in context.config.userdata.get('platform'):
        context.driver.activate_app('com.sharecare.feingoldtech.realgreen.experimental')
    else:
        print("Platform not found")


@given('user taps "{key_code}" keycode')
def pass_key_code(context, key_code):
    if 'android' in context.config.userdata.get('platform'):
        context.driver.press_keycode(key_code)
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user sets "{text}" to "{value}"')
def set_text_value(context, text, value):
    if 'android' in context.config.userdata.get('platform'):
        if text == 'Email':
            if 'cf' in context.config.userdata.get('label').lower():
                value = 'stg1cf1@scqa.me'
                print("email: " + value)
                context.helper_functions.find_by_ios_xpath(text).clear()
                context.helper_functions.find_by_ios_xpath(text).send_keys(value)
            else:
                value = 'seroney.us@ftqa.com'
                print("email: " + value)
                context.helper_functions.find_by_xpath(text).clear()
                context.helper_functions.find_by_xpath(text).send_keys(value)
        elif text == 'what':
            value = select_random_choice(find_doc_speciality)
            context.helper_functions.find_by_xpath(text).clear()
            context.helper_functions.find_by_xpath(text).send_keys(value)
        elif text == 'where':
            value = select_random_choice(find_doc_city)
            context.helper_functions.find_by_xpath(text).clear()
            context.helper_functions.find_by_xpath(text).send_keys(value)
        elif text == 'Pounds:':
            value = random.randint(60, 300)
            context.helper_functions.find_by_xpath(text).clear()
            context.helper_functions.find_by_xpath(text).send_keys(value)
        elif text == 'Feet':
            value = random.randint(2, 8)
            context.helper_functions.find_by_xpath(text).clear()
            context.helper_functions.find_by_xpath(text).send_keys(value)

        elif text == 'Inches':
            value = random.randint(1, 11)
            context.helper_functions.find_by_xpath(text).clear()
            context.helper_functions.find_by_xpath(text).send_keys(value)
        else:
            context.helper_functions.find_by_xpath(text).clear()
            context.helper_functions.find_by_xpath(text).send_keys(value)
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
        if text == 'Email':
            if 'cf' in context.config.userdata.get('label').lower():
                value = 'stg1cf1@scqa.me'
                print("email: " + value)
                context.helper_functions.find_by_ios_xpath(text).clear()
                context.helper_functions.find_by_ios_xpath(text).send_keys(value)
            else:
                value = 'seroney.us@ftqa.com'
                print("email: " + value)
                context.helper_functions.find_by_ios_xpath(text).clear()
                context.helper_functions.find_by_ios_xpath(text).send_keys(value)
        elif text == 'what':
            value = select_random_choice(find_doc_speciality)
            context.helper_functions.find_by_ios_xpath(text).clear()
            context.helper_functions.find_by_ios_xpath(text).send_keys(value)
        elif text == 'where':
            value = select_random_choice(find_doc_city)
            context.helper_functions.find_by_ios_xpath(text).clear()
            context.helper_functions.find_by_ios_xpath(text).send_keys(value)
        elif text == 'Pounds:':
            value = random.randint(60, 300)
            context.helper_functions.find_by_ios_xpath(text).clear()
            context.helper_functions.find_by_ios_xpath(text).send_keys(value)
        elif text == 'Feet':
            value = random.randint(2, 8)
            context.helper_functions.find_by_ios_xpath(text).clear()
            context.helper_functions.find_by_ios_xpath(text).send_keys(value)

        elif text == 'Inches':
            value = random.randint(1, 11)
            context.helper_functions.find_by_ios_xpath(text).clear()
            context.helper_functions.find_by_ios_xpath(text).send_keys(value)
        else:
            context.helper_functions.find_by_ios_xpath(text).clear()
            context.helper_functions.find_by_ios_xpath(text).send_keys(value)

    else:
        print("Platform not found")
    pass


@given('user presses enter on "{text}"')
def step_impl(context, text):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.find_by_xpath(text).submit()
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user sets "{pin}" as PIN')
def set_pin(context, pin):
    if 'android' in context.config.userdata.get('platform'):
        for i in pin:
            context.helper_functions.find_by_xpath(i).click()
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user backgrounds app for "{timeout}" seconds')
def step_impl(context, timeout):
    if 'android' in context.config.userdata.get('platform'):
        context.driver.background_app(timeout)
    elif 'ios' in context.config.userdata.get('platform'):
        print("ios")
    else:
        print("Platform not found")


@given('user taps Enter on "{text}"')
def pass_key(context, text):
    context.helper_functions.find_by_xpath(text).submit()


@given('user taps "{button}" button')
def tap_ios_element(context, button):
    if 'ios' in context.config.userdata.get('platform'):
        context.helper_functions.find_by_ios_elem_xpath(button)


@given('user navigates to abs "{deeplink}"')
def open_deep_links(context, deeplink):
    if 'android' in context.config.userdata.get('platform'):
        context.driver.get(base_url + deeplink)


@given('user taps partial text "{text}"')
def some_fx(context, text):
    if 'android' in context.config.userdata.get('platform'):
        context.helper_functions.find_element_by_partial_text(text)

