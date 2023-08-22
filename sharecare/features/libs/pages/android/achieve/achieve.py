"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 12.01.22
Purpose:
Implementation:
TestData: User Data
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from sharecare.keywords.android.android_locator_keywords import home_screen
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions



class AchieveScreen(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_achieve(self):
        return self.tap_element(home_screen['_ACHIEVE_'])