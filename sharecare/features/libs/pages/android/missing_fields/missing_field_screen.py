"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by ismail.koembe
Date: 12.12.21
Purpose: Holds Missing Fields Screen Page Objects
Implementation: missing_field
TestData: User that has no DOB and gender attributes
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import missing_field_screens, gender
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class MissingFieldScreens(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_next(self):
        """
        Clicks Next button
        """
        self.tap_element(missing_field_screens["_MISSING_NEXT_"])
        time.sleep(2)

    def enter_gender(self, gender):
        self.tap_element(missing_field_screens["_MISSING_GENDER_DROPBOX_"])
        self.tap_element(missing_field_screens["_MISSING_NEXT_"])
        time.sleep(2)

    def enter_dob(self, dob):
        self.find(missing_field_screens["_MISSING_GENDER_DOB_"]).clear()
        set_password = self.find(missing_field_screens["_MISSING_GENDER_DOB_"]).send_keys(dob)
        self.logger.info(dob)

    def validate_missing_fields_page_elements(self):
        assert self.validate_element_presence(missing_field_screens['_MISSING_FIELD_INFO_TEXT_'])
        pass

