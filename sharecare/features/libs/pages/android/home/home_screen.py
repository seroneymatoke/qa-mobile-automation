"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 02.11.21
Purpose: Holds Home Screen Page Objects
Implementation: test_login
TestData: Valid Username and Password
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import home_screen
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class HomeScreen(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    # list elements
    def validate_home_screen_element(self):
        time.sleep(10)
        assert self.validate_element_presence(home_screen['_NOTIFICATION_'])
        assert self.validate_element_presence(home_screen['_HOME_TRACKER_'])
        assert self.validate_element_presence(home_screen['_DISCOVER_'])
        assert self.validate_element_presence(home_screen['_ACHIEVE_'])
        assert self.validate_element_presence(home_screen['_YOU_'])




