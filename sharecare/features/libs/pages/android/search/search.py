"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 29.12.21
Purpose: POM for search module
Implementation:
TestData: Random strings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import home_screen, search
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class SearchScreen(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_search(self):
        time.sleep(5)
        return self.tap_element(home_screen['_SEARCH_ICON_'])

    def do_search(self, param):
        self.logger.info("Searching for :" + param)
        self.find(search['_SEARCH_FIELD_']).clear()
        return self.find(search['_SEARCH_FIELD_']).send_keys(param)

    def search_results(self):
        content = self.find(search['_CONTENT_'])
        values = content.find_elements_by_id('com.sharecare.realgreen:id/content')
        results = [value.text for value in values]
        self.logger.info("Vals: " +str(values))
        self.logger.info("List : " + str(results))
        return results

