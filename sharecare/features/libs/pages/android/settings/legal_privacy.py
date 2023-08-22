"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 30.11.21
Purpose: POM for Legal and Privacy
Implementation: None
TestData: None
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from selenium.common.exceptions import NoSuchElementException

from sharecare.keywords.android.android_locator_keywords import legal_privacy
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class LegalPrivacy(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def download_tracker_data(self):
        time.sleep(5)
        try:
            # Downloading data
            self.logger.info("Making tracker data request")
            return self.tap_element(legal_privacy['_TRACKER_DATA_'])
        except NoSuchElementException as e:
            self.logger.info("Tracker data already requested")
            return True

