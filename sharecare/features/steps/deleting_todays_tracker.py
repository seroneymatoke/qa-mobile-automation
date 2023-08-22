import random
import time
from behave import *
from sharecare.keywords.android.android_locator_keywords import home_screen, trackers
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sharecare.utilities.helper_functions import HelperFunctions
from appium.webdriver.common.mobileby import MobileBy

@when('user taps ... icon')
def tap_see_more(context):
     if 'android' in context.config.userdata.get('platform'):
         context.helper_functions.tap_element(trackers['_..._'])
     elif 'ios' in context.config.userdata.get('platform'):
       print('ios')
     else:
      print('Platform unavailable')