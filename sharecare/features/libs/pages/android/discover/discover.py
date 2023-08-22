"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 12.01.22
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from sharecare.keywords.android.android_locator_keywords import home_screen, discover
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions
from selenium.webdriver.support import expected_conditions as EC


class Discover(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_discover(self):
        # Tap discover
        return self.tap_element(home_screen['_DISCOVER_'])

    def tap_community_well_being(self):
        # Tap community well being
        return self.tap_element(discover['_COMM_WELL_BEING_'])

    def tap_inspirations(self):
        # Tap inspiration
        return self.tap_element(discover['_INSPIRATION_'])

    def tap_med_prices(self):
        # Tap med prices
        return self.tap_element(discover['_MED_PRICES_'])

    def tap_health_topics(self):
        """
        Click You button
        """
        try:
            e = discover['_HEALTH_TOPICS_']
            element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((e[0], e[1])))
        except TimeoutException as e:
            self.logger.info("Health topic not found")




