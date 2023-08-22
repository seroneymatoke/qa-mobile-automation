"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 17.11.21
Purpose: Holds all POM models for Security PIN
Implementation: test_security_pin, security_pin_feature
TestData: Random 4 digit code - faker
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from appium.webdriver.common.mobileby import MobileBy

from sharecare.keywords.android.android_locator_keywords import security_pin
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions
from faker import Faker


class SecurityPIN(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def toggle_security_pin_btn(self):
        # Toggle Pin Switch on off
        return self.tap_element(security_pin['_SECURITY_PIN_TOGGLE_'])

    def enter_passcode(self, passcode):
        # Set Passcode
        # passcode as an iterable list
        self.logger.info("Passcode: " + str(passcode))

        for i in passcode:
            # Set Passcode
            # Create xpaths
            val = (MobileBy.XPATH, '//android.widget.TextView[@text="' + i + '"]')
            self.tap_element(val)

    def set_passcode(self, passcode, loop):
        self.logger.info("Setting passcode: ")
        for i in range(1, loop):
            if self.find(security_pin['_PIN_CODE_TEXT_']).text == 'Choose your 4-digit Security PIN':
                self.enter_passcode(passcode)
                self.logger.info("Set current PIN")
            elif self.find(security_pin['_PIN_CODE_TEXT_']).text == 'Re-enter your 4-digit Security PIN':
                self.enter_passcode(passcode)
                self.logger.info("Set current PIN")
            elif self.find(security_pin['_PIN_CODE_TEXT_']).text == 'Enter your current Security PIN':
                self.enter_passcode(passcode)
                self.logger.info("Set current PIN")
            else:
                self.logger.info("Missing Details")

    def tap_auto_clock(self):
        return self.tap_element(security_pin['_AUTO_LOCK_'])

    # ToDo - Best Selection
    def set_auto_lock(self, timeout):
        # Set auto lock settings
        self.logger.info("Timeout set to: "+str(timeout))
        if timeout == 15:
            self.tap_element(security_pin['_15_SECONDS_'])
            self.push_app_to_background(timeout)
        elif timeout == 30:
            self.tap_element(security_pin['_30_SECONDS_'])
            self.push_app_to_background(timeout)
        elif timeout == 60:
            self.tap_element(security_pin['_1_MIN_'])
            self.push_app_to_background(timeout)
        elif timeout == 300:
            self.tap_element(security_pin['_5_MIN_'])
            self.push_app_to_background(timeout)
        elif timeout == 600:
            self.tap_element(security_pin['_10_MIN_'])
            self.push_app_to_background(timeout)
        else:
            self.logger.info("Timeout Set incorrectly, setting default timeout")
            self.tap_element(security_pin['_15_SECONDS_'])
            self.push_app_to_background(15)

    def verify_app_background(self):
        seconds = [15]
        for i in seconds:
            self.push_app_to_background(i)
            self.logger.info("Testing pushing app to background and resurrecting")
