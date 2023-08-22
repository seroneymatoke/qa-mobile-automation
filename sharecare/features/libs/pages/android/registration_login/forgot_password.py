"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 14.12.21
Purpose:
Implementation:
TestData: email
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from sharecare.keywords.android.android_locator_keywords import login_onboarding_screen, forgot_password, splash_screen, \
    android_alert_buttons
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class ForgotPassword(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_forgot_password(self):
        self.tap_element(splash_screen['_SIGN_IN_BTN_'])
        return self.tap_element(forgot_password['_FORGOT_PASSWORD_'])

    def enter_email(self, email):
        self.find(forgot_password["_EMAIL_"]).clear()
        set_email = self.find(forgot_password["_EMAIL_"]).send_keys(email)
        self.logger.info(email)

    def tap_send(self):
        return self.tap_element(forgot_password['_SEND_'])

    def return_msg(self):
        return self.find(android_alert_buttons['_MESSAGE_']).text
