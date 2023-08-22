"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 08.11.21
Purpose: To validate successful new user registration
Implementation: used by the register user file
TestData: Requires users to be created successfully
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from sharecare.utilities.helper_functions import HelperFunctions


class WelcomeScreen(HelperFunctions):
    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)




