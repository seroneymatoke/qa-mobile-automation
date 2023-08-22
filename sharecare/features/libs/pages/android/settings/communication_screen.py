"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 25.11.21
Purpose: POs for communications screens
Implementation: features -> communication
TestData: None Required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from sharecare.keywords.android.android_locator_keywords import communication
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class Communications(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    # sms messaging
    def tap_sms_messaging(self):
        # Get attributes
        return self.tap_element(communication['_SMS_MESSAGING_'])

    def tap_enable_disable_sms_messaging(self, value):
        element = self.find(communication['_RECEIVE_SMS_'])
        self.logger.info("checking element attributes: " + element.get_attribute("checked"))
        if value == "on":
            if element.get_attribute("checked"):
                self.logger.info("SMS messaging is on")
                return True
            else:
                self.logger.info("SMS messaging is off turning it on")
                return element.click()
        elif value == "off":
            if element.get_attribute("checked"):
                self.logger.info("SMS messaging is on turning it off")
                return element.click()
            else:
                self.logger.info("SMS messaging is off")
                return True
        else:
            return False

    def enable_disable_sms_messaging(self):
        switches = ["on", "off"]
        for i in switches:
            self.tap_enable_disable_sms_messaging(i)
        time.sleep(5)

    # email subscriptions
    def tap_email_subscriptions(self):
        return self.tap_element(communication['_EMAIL_SUBSCRIPTIONS_'])

    def set_email_subscriptions_preferences(self, value):
        # Setting email preferences
        if value == "off":
            self.tap_element(communication['_RECEIVE_EMAIL_NOTIFICATIONS_'])
            assert self.find(communication['_ACTIVITY_DIGEST_']).is_enabled() is False
            self.logger.info("Disable Email Subscriptions")
        else:
            # Turn most notifications on
            self.tap_element(communication['_ACTIVITY_DIGEST_'])
            self.tap_element(communication['_PROGRAM_UPDATES_'])
            self.tap_element(communication['_PRODUCT_UPDATES_'])
            self.tap_element(communication['_PULSE_'])
            self.tap_element(communication['_HEALTH_TIPS_'])
            # scroll down
            self.swipe_direction_android("down", 2)
            if self.find(communication['_ONCE_A_WEEK_']).get_attributes('checked'):
                self.tap_element(communication['_TWICE_A_WEEK_'])
            else:
                self.tap_element(communication['_ONCE_A_WEEK_'])
            self.tap_element(communication['_VIDEO_TIPS_'])
            self.tap_element(communication['_MY_CONDITIONS_'])

            # No need to check personalized emails - always on
            # Notify When
            self.tap_element(communication['_NOTIFY_ME_WHEN_TRACKER_UPDATED_'])
            self.tap_element(communication['_NOTIFY_INSURANCE_REMINDERS_'])

    def submit_email_preferences(self):
        time.sleep(10)
        email_subscriptions = ["on", "off"]
        for i in email_subscriptions:
            self.logger.info("Email preferences being set to: " + i)
            self.set_email_subscriptions_preferences(i)
            time.sleep(10)
            self.tap_element(communication['_SAVE_CHANGES_BTN_'])

    def email_webview(self):
        return self.validate_element_presence(communication['_EMAIL_SUBSCRIPTIONS_WEBVIEW_'])

    # push notifications
    def tap_push_notifications(self):
        # tap the push notification button
        return self.tap_element(communication['_PUSH_NOTIFICATIONS_MENU_'])

    def set_push_notifications_preferences(self, value):
        if value == "on":
            if self.find(communication['_HEALTH_DATA_UPDATES_']).get_attributes('checked'):
                return True
            else:
                self.tap_element(communication['_HEALTH_DATA_UPDATES_'])
                self.logger.info("Turned on Health updates")
            if self.find(communication['_REWARDS_']).get_attributes('checked'):
                return True
            else:
                self.tap_element(communication['_REWARDS_'])
                self.logger.info("Turned on Reward updates")
            if self.find(communication['_INSIGHTS_']).get_attributes('checked'):
                return True
            else:
                self.tap_element(communication['_INSIGHTS_'])
                self.logger.info("Turned on Insights updates")
            if self.find(communication['_INSIGHTS_']).get_attributes('checked'):
                return True
            else:
                self.tap_element(communication['_INSIGHTS_'])
                self.logger.info("Turned on Insights updates")

            if self.find(communication['_CHALLENGES_']).get_attributes('checked'):
                return True
            else:
                self.tap_element(communication['_CHALLENGES_'])
                self.logger.info("Turned on Challenges updates")

            if self.find(communication['_CHALLENGES_ENDING_']).get_attributes('checked'):
                return True
            else:
                self.tap_element(communication['_CHALLENGES_ENDING_'])
                self.logger.info("Turned on Challenges Ending updates")

            if self.find(communication['_DAILY_REMINDER_']).get_attributes('checked'):
                return True
            else:
                self.tap_element(communication['_DAILY_REMINDER_'])
                self.logger.info("Turned on Daily reminder updates")
        else:
            if self.find(communication['_HEALTH_DATA_UPDATES_']).get_attributes('checked'):
                self.tap_element(communication['_HEALTH_DATA_UPDATES_'])
                self.logger.info("Turned off Health updates")
            else:
                return True

            if self.find(communication['_REWARDS_']).get_attributes('checked'):
                self.tap_element(communication['_REWARDS_'])
                self.logger.info("Turned on Reward updates")
            else:
                return True
            if self.find(communication['_INSIGHTS_']).get_attributes('checked'):
                self.tap_element(communication['_INSIGHTS_'])
                self.logger.info("Turned on Insights updates")
            else:
                return True
            if self.find(communication['_INSIGHTS_']).get_attributes('checked'):
                self.tap_element(communication['_INSIGHTS_'])
                self.logger.info("Turned on Insights updates")
            else:
                return True

            if self.find(communication['_CHALLENGES_']).get_attributes('checked'):
                self.tap_element(communication['_CHALLENGES_'])
                self.logger.info("Turned on Challenges updates")
            else:
                return True

            if self.find(communication['_CHALLENGES_ENDING_']).get_attributes('checked'):
                self.tap_element(communication['_CHALLENGES_ENDING_'])
                self.logger.info("Turned on Challenges Ending updates")
            else:
                return True

            if self.find(communication['_DAILY_REMINDER_']).get_attributes('checked'):
                self.tap_element(communication['_DAILY_REMINDER_'])
                self.logger.info("Turned on Daily reminder updates")
            else:
                return True

    def parametrize_push_notifications(self):
        push_notifications = ["on", "off"]
        for i in push_notifications:
            self.logger.info("Push Notification preferences being set to: " + i)
            time.sleep(10)
            self.set_push_notifications_preferences(i)
