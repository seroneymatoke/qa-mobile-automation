"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 04.03.22
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

from appium import webdriver

from sharecare.keywords.android.android_locator_keywords import select_environment, envs, markets
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class SetupEnv(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    def set_environment_market(self, label, market, environments):
        if 'sc' in label.lower():
            # Deprecated
            self.tap_element(select_environment['_SHARECARE_LOGO_'])
            self.tap_element(markets['_US_'])
            if 'US' in market:
                self.tap_element(markets['_US_'])
            elif 'NZ' in market:
                self.tap_element(markets['_NZ_'])
            elif 'BR' in market:
                self.tap_element(markets['_BR_'])
            else:
                self.logger.error('Invalid Market: ')

            # @todo - Clean this up
            # match market:
            #     case 'US':
            #         self.tap_element(markets['_US_'])
            #     case 'NZ':
            #         self.tap_element(markets['_NZ_'])
            #     case 'BR':
            #         self.tap_element(markets['_BR_'])
            #     case _:
            #         self.logger.error('Invalid Market: ')

            self.tap_element(envs['_PRODUCTION_'])
            if 'STAGE' in environments:
                self.tap_element(envs['_STAGING_'])
            elif 'PROD' in environments:
                self.tap_element(envs['_PRODUCTION_'])
            elif 'UAT' in environments:
                self.tap_element(envs['_UAT_'])
            elif 'QA' in environments:
                self.tap_element(envs['_QA_'])
            else:
                self.logger.error('Invalid Environment: ')
            self.step_back()

        if 'cf' in label.lower():
            self.tap_element(select_environment['_CF_LOGO_'])
            self.tap_element(select_environment['_CF_SELECT_MARKET_'])
            if 'US' in market:
                self.tap_element(markets['_US_'])
            elif 'NZ' in market:
                self.tap_element(markets['_NZ_'])
            elif 'BR' in market:
                self.tap_element(markets['_BR_'])
            else:
                self.logger.error('Invalid Market: ')

            # @todo - Clean this up
            # match market:
            #     case 'US':
            #         self.tap_element(markets['_US_'])
            #     case 'NZ':
            #         self.tap_element(markets['_NZ_'])
            #     case 'BR':
            #         self.tap_element(markets['_BR_'])
            #     case _:
            #         self.logger.error('Invalid Market: ')

            self.tap_element(select_environment['_CF_SELECT_ENVIRONMENT_'])
            if 'STAGE' in environments:
                self.tap_element(envs['_STAGING_'])
            elif 'PROD' in environments:
                self.tap_element(envs['_PRODUCTION_'])
            elif 'UAT' in environments:
                self.tap_element(envs['_UAT_'])
            elif 'QA' in environments:
                self.tap_element(envs['_QA_'])
            else:
                self.logger.error('Invalid Environment: ')
            self.step_back()

        # if environment == 'STAGE':
        #     self.tap_element(envs['_STAGING_'])
        # elif environment == 'PROD':
        #     self.tap_element(envs['_PRODUCTION_'])
        # elif environment == 'QA':
        #     self.tap_element(envs['_UAT_'])
        # else:
        #     self.logger.info("Resetting to Prod")

    def set_env_market_ios(self, context, market, environments):

        # @Todo - Add CF environment switch
        app = 'Settings'
        ios_device_name = context.config.userdata.get("ios_device_name_simulator")
        ios_platform_version = context.config.userdata.get("ios_platform_version_simulator")
        ios_no_reset = context.config.userdata.get("ios_no_reset")
        ios_sim_udid = context.config.userdata.get("sim_udid")
        #
        desired_capabilities = {
            'platformName': 'iOS',
            'automationName': 'XCUITest',
            "autoGrantPermissions": True,
            'app': app,
            'platformVersion': ios_platform_version,
            'deviceName': ios_device_name,
            "noReset": ios_no_reset,
            "udid": ios_sim_udid
        }
        context.driver_settings = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        context.driver_settings.execute_script("mobile: scroll", {"direction": "down"})
        sharecare_settings = context.driver_settings.find_element_by_accessibility_id(
            "com.sharecare.feingoldtech.realgreen")
        sharecare_settings.click()

        element = context.driver_settings.find_element_by_accessibility_id("settings.bundle.environment")
        element.click()

        if environments == "STAGE":
            test_env = context.driver_settings.find_element_by_xpath('//XCUIElementTypeCell[@name="STG"]')
            test_env.click()

        if environments == "UAT":
            test_env = context.driver_settings.find_element_by_xpath('//XCUIElementTypeCell[@name="UAT"]')
            test_env.click()

        context.driver_settings.back()

        element = context.driver_settings.find_element_by_accessibility_id("settings.bundle.market")
        element.click()
        testMarket = context.driver_settings.find_element_by_xpath(
            "//XCUIElementTypeCell[@name=\"" + market + "\"]")
        testMarket.click()
        back = context.driver_settings.find_element_by_xpath('//XCUIElementTypeButton[@name="Sharecare"]')
        back.click()
        context.driver_settings.quit()
        # element = context.driver_settings.find_element_by_xpath('//XCUIElementTypeCell[@name="Environment, PRD"]')
        # element.click()
        # testEnvironment = context.driver_settings.find_element_by_xpath(
        #     "//XCUIElementTypeCell[@name=\"" + environments + "\"]")
        # testEnvironment.click()
        # back.click()

    def reactivate_app(self, context):
        app = context.config.userdata.get('ios_app_path_simulator')
        ios_device_name = context.config.userdata.get("ios_device_name_simulator")
        ios_platform_version = context.config.userdata.get("ios_platform_version_simulator")
        ios_no_reset = context.config.userdata.get("ios_no_reset")
        ios_sim_udid = context.config.userdata.get("sim_udid")
        #
        desired_capabilities = {
            "autoGrantPermissions": True,
            "platformName": "iOS",
            "appium:platformVersion": "15.5",
            "appium:automationName": "XCUITest",
            "appium:deviceName": "iPhone 13",
            "app": app,
            "appium:xcodeOrgId": "CN89264FDM",
            "appium:xcodeSigningId": "Sharecare Inc",
            "udid": ios_sim_udid
        }

        print("WOA")
        context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
