"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 21.12.21
Purpose:
Implementation: POM for all account in settings file
TestData: Username
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import account
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class Account(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_edit(self):
        # click edit button
        return self.tap_element(account['_EDIT_'])

    def tap_delete(self):
        # click delete button - Constrants - should only allow non us accounts
        self.swipe_direction_android("down", 2)
        return self.tap_element(account['_DELETE_ACCOUNT_'])

    def tap_change_password(self):
        # tap change password btn
        self.swipe_direction_android("down", 2)
        return self.tap_element(account['_CHANGE_PASSWORD_'])

    def set_current_password(self, current_password):
        self.logger.info("Set current Password: "  + current_password)
        return self.find(account['_CURRENT_PASSWORD_']).send_keys(current_password)

    def set_new_password(self, new_password):
        self.logger.info("Set new Password: " + new_password)
        return self.find(account['_NEW_PASSWORD_']).send_keys(new_password)

    def set_confirm_password(self, new_password):
        self.logger.info("Set confirm Password: " + new_password)
        return self.find(account['_CONFIRM_PASSWORD_']).send_keys(new_password)

    def tap_update_password(self):
        return self.tap_element(account['_UPDATE_PASSWORD_'])

    def validate_user_data(self):
        time.sleep(5)
        result = {}
        labels_list = self.find(account['_LABEL_TEXT_'])
        items = labels_list.find_elements_by_id('com.sharecare.realgreen:id/label')
        values = labels_list.find_elements_by_id('com.sharecare.realgreen:id/value')
        # Do ze magic of list comprehensions
        result = {items[i].text: values[i].text for i in range(len(items)-1)}
        self.logger.info("List: " + str(result))
        return result['Email']

    # take photo
    def tap_change_profile_photo(self):
        return self.tap_element(account['_CHANGE_PHOTO_'])

    def tap_take_photo(self):
        return self.tap_element(account['_TAKE_PHOTO_'])

    def tap_camera_btn(self):
        return self.tap_element(account['_CAMERA_PHOTO_'])

    def tap_ok(self):
        return self.tap_element(account['_OK_'])

    def tap_remove_photo(self):
        return self.tap_element(account['_REMOVE_PHOTO_'])




