"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 11.11.21
Purpose: Hold guided tooltips POM
Implementation: Used in Registration page
TestData: Valid account setup
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import guided_tooltips_messages, guided_tooltips, \
    guided_ios_tooltips
from sharecare.utilities.helper_functions import HelperFunctions


class GuidedToolTips(HelperFunctions):
    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def validate_tool_tips(self):
        # time.sleep(5)
        for i in guided_tooltips_messages:
            element = self.find(guided_tooltips['_TOOLTIPS_MESSAGE_TXT_'])
            self.tap_element(guided_tooltips['_NOTIFICATION_NEXT_'])
        assert True

    def validate_ios_tool_tips(self):
        self.tap_element(guided_ios_tooltips['_NOTIFICATION_NEXT_'])
        self.tap_element(guided_ios_tooltips['_NOTIFICATION_NEXT_'])
        self.tap_element(guided_ios_tooltips['_DONE_'])
