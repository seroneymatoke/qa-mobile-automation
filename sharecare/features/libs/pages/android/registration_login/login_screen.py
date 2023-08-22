"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 28.10.21
Purpose: Login Screen page object
Implementation: Class.Function
TestData: Username and Password required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import login_onboarding_screen, splash_screen, home_screen
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class LoginScreen(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_login(self):
        """
        Clicks login button
        """
        self.tap_element(splash_screen["_SIGN_IN_BTN_"])
        # time.sleep(10)

    def tap_login_ios(self):
        self.tap_element(splash_screen["_SIGN_IN_BTN_IOS_"])

    def enter_email_ios(self, email):
        self.find(login_onboarding_screen["_EMAIL_IOS_"]).clear()
        set_email = self.find(login_onboarding_screen["_EMAIL_IOS_"]).send_keys(email)
        self.logger.info(email)

    def enter_password_ios(self, password):
        self.find(login_onboarding_screen["_PASSWORD_IOS_"]).click()
        self.find(login_onboarding_screen["_PASSWORD_IOS_"]).clear()
        self.find(login_onboarding_screen["_PASSWORD_IOS_"]).send_keys(password)
        self.logger.info(password)

    def enter_email(self, email):
        self.find(login_onboarding_screen["_EMAIL_"]).clear()
        set_email = self.find(login_onboarding_screen["_EMAIL_"]).send_keys(email)
        self.logger.info(email)

    def enter_password(self, password):
        self.find(login_onboarding_screen["_PASSWORD_"]).clear()
        set_password = self.find(login_onboarding_screen["_PASSWORD_"]).set_value(password)
        self.logger.info(password)

    def validate_error_messages(self, selector, text):
        message = self.contains_content(selector, text)

    # Todo - Clean up
    def validate_login_page_elements(self):
        #     assert self.validate_element_presence(home_screen['_HOME_'])
        #     assert self.validate_element_presence(home_screen['_HOME_TRACKER_'])
        #     assert self.validate_element_presence(home_screen['_DISCOVER_'])
        #     assert self.validate_element_presence(home_screen['_ACHIEVE_'])
        #     assert self.validate_element_presence(home_screen['_YOU_'])
        pass
