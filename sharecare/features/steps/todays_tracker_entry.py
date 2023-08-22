import random
import time

from behave import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sharecare.keywords.android.android_locator_keywords import you_screen
from sharecare.utilities.helper_functions import HelperFunctions
from sharecare.keywords.android.android_locator_keywords import home_screen, trackers
from appium.webdriver.common.mobileby import MobileBy
from datetime import date

@given("existing user logging in with details {email}, and {password}")
def login(context, email, password):
    """
        Without user creation, existing user can log in
    """
    if 'android' in context.config.userdata.get('platform'):
        context.login_screen.tap_login()
        context.login_screen.enter_email(email)
        context.login_screen.enter_password(password)
        context.login_screen.tap_login()
    elif 'ios' in context.config.userdata.get('platform'):
        context.login_screen.tap_login_ios()
        context.login_screen.enter_email_ios(email)
        context.login_screen.enter_password_ios(password)
        context.login_screen.tap_login_ios()
    else:
        print('not found')