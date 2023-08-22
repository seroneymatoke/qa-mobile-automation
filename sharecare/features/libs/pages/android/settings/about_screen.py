"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 23.11.21
Purpose: POM for about screen
Implementation:
TestData: None required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import about
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class About(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def about_page(self):
        time.sleep(5)
        self.swipe_direction_android("down", 10)
        time.sleep(2)
        self.swipe_direction_android("up", 9)

    # @Todo -add request demo stuff.






