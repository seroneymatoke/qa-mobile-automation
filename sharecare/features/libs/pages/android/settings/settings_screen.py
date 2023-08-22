"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 11.11.21
Purpose: Holds all page objects for the settings screen
Implementation: used by various pages e.g. login pages, settings pages
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from sharecare.keywords.android.android_locator_keywords import settings_screen
from sharecare.utilities.helper_functions import HelperFunctions


class Settings(HelperFunctions):

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def tap_settings(self):
        """
        Click settings button
        """
        self.tap_element(settings_screen['_SETTINGS_'])

    def tap_account(self):
        """
        Click Account button
        """
        self.tap_element(settings_screen['_ACCOUNT_'])

    def tap_appearance(self):
        """
        Click appearance button
        """
        self.tap_element(settings_screen['__APPEARANCE__'])

    def tap_video_autoplay(self):
        """
        Click video autoplay button
        """
        self.tap_element(settings_screen['_VIDEO_AUTOPLAY_'])

    def tap_communications(self):
        """
        Click communications button
        """
        self.tap_element(settings_screen['_COMMUNICATIONS_'])

    def tap_security_pin(self):
        """
        Click security_pin button
        """
        self.tap_element(settings_screen['_SECURITY_PIN_'])

    def tap_about_us(self):
        """
        Click about us button
        """
        self.tap_element(settings_screen['_ABOUT_US_'])

    def tap_support(self):
        """
        Click about us button
        """
        self.tap_element(settings_screen['_SUPPORT_'])

    def tap_legal_privacy(self):
        """
        Click legal and privacy button
        """
        self.tap_element(settings_screen['_LEGAL_PRIVACY_'])

    def tap_sign_out(self):
        """
        Click sign out button
        """
        self.tap_element(settings_screen['_SIGN_OUT_'])

