"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 09.11.21
Purpose: To implement setting screen 
Implementation: POM Model for You screen
TestData: None
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sharecare.keywords.android.android_locator_keywords import you_screen
from sharecare.utilities.helper_functions import HelperFunctions


class YouScreen(HelperFunctions):
    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_you(self):
        """
        Click You button
        """
        self.tap_element(you_screen['_YOU_'])
        try:
            e = you_screen['_RAT_NOT_NOW_']
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((e[0], e[1])))
            self.tap_element(you_screen['_RAT_NOT_NOW_'])
        except TimeoutException as e:
            self.logger.info("RAT NOT FOUND")

    def update_real_age(self):
        """
        Returns update real age button
        """
        # self.find()

    def take_real_age_test(self):
        """
        Click Real Age Test button
        """
        # self.tap_element()
