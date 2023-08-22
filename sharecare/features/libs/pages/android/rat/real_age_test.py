"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 11.03.22
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class RealAgeTest(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def rat_status(self):
        pass
