import inspect
import os
import time
from time import sleep
from appium import webdriver

# from sharecare.features.libs.pages.android.base_page import BasePage
from behave.model import Scenario
from behave_testrail_reporter import TestrailReporter, TestrailProject

from sharecare.features.libs.pages.android.discover.discover import Discover
from sharecare.features.libs.pages.android.environment.setup_env import SetupEnv
from sharecare.features.libs.pages.android.home.home_screen import HomeScreen
from sharecare.features.libs.pages.android.missing_fields.missing_field_screen import MissingFieldScreens
from sharecare.features.libs.pages.android.registration_login.create_account import CreateAccount
from sharecare.features.libs.pages.android.registration_login.forgot_password import ForgotPassword
from sharecare.features.libs.pages.android.registration_login.guided_tooltips import GuidedToolTips
from sharecare.features.libs.pages.android.registration_login.login_screen import LoginScreen
from sharecare.features.libs.pages.android.search.search import SearchScreen
from sharecare.features.libs.pages.android.settings.about_screen import About
from sharecare.features.libs.pages.android.settings.account import Account
from sharecare.features.libs.pages.android.settings.communication_screen import Communications
from sharecare.features.libs.pages.android.settings.legal_privacy import LegalPrivacy
from sharecare.features.libs.pages.android.settings.security_pin_screen import SecurityPIN
from sharecare.features.libs.pages.android.settings.settings_screen import Settings
from sharecare.features.libs.pages.android.registration_login.splash_screen import SplashScreen
from sharecare.features.libs.pages.android.you.you_screen import YouScreen
# from sharecare.features.steps.test_helper_functions import activate_app
from sharecare.keywords.android.android_locator_keywords import select_environment
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions
from sharecare.utilities.team_integration import push_to_teams
from sharecare.utilities.team_integration import webhooks

# setup Logger
logger = CustomLogger.custom_logger()
tok_env = {}


def get_market_env(context):
    market_env = context.config.userdata.get("env")
    logger.info("Envir " + market_env)
    return market_env


# @todo -set android cloud names
def set_app_build_device(context):
    if 'uat' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get('label').lower():
        return 'com.sharecare.carefirst.realgreen.uat'
    if 'stage' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get('label').lower():
        return 'com.sharecare.carefirst.realgreen.internal'
    if 'uat' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'sc' in context.config.userdata.get('label').lower():
        return 'com.sharecare.realgreen.uat'
    if 'stage' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'sc' in context.config.userdata.get('label').lower():
        return 'com.sharecare.realgreen.internal'
    if 'uat' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get('label').lower():
        return ''
    if 'stage' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get('label').lower():
        return 'com.sharecare.carefirst'


def set_app_cloud_name(context):
    if 'uat' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get('label').lower():
        return 'CF_iOS_UAT.ipa'
    if 'stage' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get(
        'label').lower():
        return 'CF_iOS_RCandi.ipa'
    if 'uat' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'sc' in context.config.userdata.get('label').lower():
        return 'SC_iOS_UAT.ipa'
    if 'stage' in context.config.userdata.get('env').lower() and 'ios' in context.config.userdata.get(
            'platform').lower() and 'sc' in context.config.userdata.get(
        'label').lower():
        return 'SC_iOS_RCandi.ipa'
    if 'stage' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'sc' in context.config.userdata.get('label').lower():
        return 'app-sharecare-rcandi-debug.apk'
    if 'stage' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get(
        'label').lower():
        return 'app-carefirst-rcandi-debug.apk'
    if 'uat' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'sc' in context.config.userdata.get('label').lower():
        return 'app-sharecare-alpha-debug.apk'
    if 'uat' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get('label').lower():
        return 'app-carefirst-alpha-debug.apk'
    if 'prod' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'sc' in context.config.userdata.get('label').lower():
        return 'app-sharecare-beta-release.apk'
    if 'prod' in context.config.userdata.get('env').lower() and 'android' in context.config.userdata.get(
            'platform').lower() and 'cf' in context.config.userdata.get('label').lower():
        return 'app-carefirst-beta-release.apk'


def set_appium_connection_url(context):
    # Teneary operator
    # parse creds
    url = 'https://{username}:{access_key}@ondemand.us-west-1.saucelabs.com:443/wd/hub'.format(
        username=os.environ.get('SAUCE_USERNAME'),
        access_key=os.environ.get('SAUCE_ACCESS_KEY'))
    return url if 'cloud' in context.config.userdata.get(
        'platform') else 'http://localhost:4723/wd/hub'


def sauce_options(context):
    options = {
        "job-name": context.config.userdata.get('label') + ' | ' + context.feature.filename,
        "job-build": context.config.userdata.get('label') + ' | ' + context.feature.filename,
        "name": context.config.userdata.get('label') + ' | ' + context.feature.name,
        "build": context.config.userdata.get('label') + ' | Berlin Sanity | Build ' + context.config.userdata.get(
            'build') + '| Env: ' + context.config.userdata.get('env')
    }



def android_device_setup(context):
    android_app_path = context.config.userdata.get('android_app_path')
    android_device_name = context.config.userdata.get("android_device_name")
    android_device_id = context.config.userdata.get("android_device_id")
    #
    desired_capabilities = {
        "platformName": "Android",
        "autoGrantPermissions": True,
        # "autoGrantPermissions": context.config.userdata.get("auto_grant_permissions"),
        "app": android_app_path,
        "deviceName": android_device_name,
        "deviceId": android_device_id,
        "automationName": "UIAutomator2",
        "noReset": False,
        "autoAcceptAlerts": True
    }
    return desired_capabilities


# android_emulator


def android_emulator_setup(context):
    app = context.config.userdata.get('android_app_path')
    #
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": app,
        "autoGrantPermissions": True,
        "noReset": context.config.userdata.get("no_reset")
    }
    return desired_capabilities


def cloud_android_setup(context):
    app = context.config.userdata.get('android_app_path')
    # |(Samsung Galaxy.*)|(Google Pixel.*)
    app_storage = "storage:filename={storage}".format(storage=set_app_cloud_name(context))
    desired_capabilities = {
        "platformName": "android",
        "deviceName": "(Samsung Galaxy S2.*)|(Samsung Galaxy A7.*)|(Samsung Galaxy A8.*)",
        # "app": "storage:c6f6f5ba-1f80-46fc-81db-276ceed4fce9",
        "app": "storage:71f42701-8086-4287-ba6c-e1e2fe86b3fc",
        # CF app-carefirst-uat-release.apk
        "app": app_storage,
        "username": context.config.userdata.get("SAUCE_USERNAME"),
        "accessKey": context.config.userdata.get("SAUCE_ACCESS_KEY"),
        "deviceOrientation": 'portrait',
        "platformVersion": "11",
        "autoGrantPermissions": True,
        "noReset": False,
        "autoAcceptAlerts": True,
        "extendedDebugging": True,
        "capturePerformance": True,
        "passed": True,
        "build": context.config.userdata.get('label') + ' | Berlin Sanity | Build ' + context.config.userdata.get(
            'build') + '| Env: ' + context.config.userdata.get('env'),
        "newCommandTimeout": 1800,
        "phoneOnly": True,
        "resigningEnabled": False,
        "allowTouchIdEnroll": False,
        "sauceLabsImageInjectionEnabled": False,
        "job-name": context.config.userdata.get('label') + ' | ' + context.feature.filename,
        "job-build": context.config.userdata.get('label') + ' | ' + context.feature.filename,
        "name": context.config.userdata.get('label') + ' | ' + context.feature.name
    }
    return desired_capabilities


def ios_simulator_setup(context):
    app = context.config.userdata.get('ios_app_path_simulator')
    ios_device_name = context.config.userdata.get("ios_device_name_simulator")
    ios_platform_version = context.config.userdata.get("ios_platform_version_simulator")
    ios_no_reset = context.config.userdata.get("no_reset")
    ios_sim_udid = context.config.userdata.get("sim_udid")
    #
    desired_capabilities = {
        "autoGrantPermissions": True,
        "appium:noReset": True,
        "platformName": "iOS",
        "appium:platformVersion": "16.2",
        "appium:automationName": "XCUITest",
        "appium:deviceName": "iPhone 14",
        "appium:app": app,
        "appium:bundleId": "com.sharecare.feingoldtech.realgreen",
        "appium:xcodeOrgId": "CN89264FDM",
        "appium:xcodeSigningId": "Sharecare Inc",
        "appium:autoAcceptAlerts": True,
        "appium:shouldTerminateApp": True,
        "udid": ios_sim_udid,

    }
    return desired_capabilities


def ios_simulator_setup_no_reset(context):
    app = context.config.userdata.get('ios_app_path')
    ios_device_name = context.config.userdata.get("ios_device_name_simulator")
    ios_platform_version = context.config.userdata.get("ios_platform_version_simulator")
    ios_no_reset = context.config.userdata.get("ios_no_reset")
    #
    desired_capabilities = {
        'platformName': 'iOS',
        'automationName': 'XCUITest',
        "autoGrantPermissions": True,
        'app': app,
        'platformVersion': ios_platform_version,
        'deviceName': ios_device_name,
        "noReset": True,
    }
    return desired_capabilities


# ios_device


def ios_real_device_setup(context):
    # app = context.config.userdata.get('ios_app_path')
    ios_device_name = context.config.userdata.get("ios_device_name")
    ios_platform_version = context.config.userdata.get("ios_platform_version")
    ios_no_reset = context.config.userdata.get("ios_no_reset")
    #
    desired_capabilities = {
        "app": context.config.userdata.get("ios_app_path_real_device"),
        "platformName": "iOS",
        "appium:platformVersion": "16.1.1",
        "appium:automationName": "XCUITest",
        "appium:deviceName": "iPhone 13",
        "appium:updatedWDABundleId": "io.seroneymatoke1.WebDriverAgentRunner.xctrunner",
        # "appium:bundleId": "com.sharecare.feingoldtech.realgreen.internal",
        "appium:bundleId": "com.sharecare.feingoldtech.realgreen.uat",
        "appium:xcodeOrgId": "CN89264FDM",
        "appium:xcodeSigningId": "Sharecare Inc",
        # Work iPhone "00008110-001A758821E9801E"
        "appium:udid": "00008110-001A758821E9801E",
        # Seroney - 00008110-001975CE34B8801E
        "appium:autoAcceptAlerts": True,
        # 'app': app,
        # 'bundleId':
        # 'platformName': 'iOS',
        # 'platformVersion': context.config.userdata.get("iOSplatformVersion"),
        # 'udid': 'auto',
        # "autoGrantPermissions": context.config.userdata.get("auto_grant_permissions"),
        # "noReset": context.config.userdata.get("no_reset"),
        # "autoAcceptAlerts": context.config.userdata.get("auto_accept_alerts"),
        # 'automationName': 'XCUITest',
        # 'deviceName': context.config.userdata.get("ios_device_name"),
        # "xcodeSigningId": "Sharecare Inc",
        # "xcodeOrgId": "CN89264FDM"

    }
    return desired_capabilities


def cloud_ios_setup(context):
    app = context.config.userdata.get('ios_app_path')
    ios_device_name = context.config.userdata.get("ios_device_name")
    ios_platform_version = context.config.userdata.get("ios_platform_version")
    ios_no_reset = context.config.userdata.get("ios_no_reset")
    #
    app_storage = "storage:filename={storage}".format(storage=set_app_cloud_name(context))
    desired_capabilities = {
        "platformName": "iOS",
        "deviceName": "(iPhone 11.*)|(iPhone 12.*)|(iPhone 13.*)|(iPhone 14.*)",
        # "deviceName": ios_device_name,
        "app": app_storage,
        # "username": context.config.userdata.get("SAUCE_USERNAME"),
        # "accessKey": context.config.userdata.get("SAUCE_ACCESS_KEY"),
        "deviceOrientation": 'portrait',
        "platformVersion": "16",
        "autoGrantPermissions": True,
        "noReset": False,
        "fullReset": True,
        "autoAcceptAlerts": True,
        "extendedDebugging": True,
        "capturePerformance": True,
        "passed": True,
        "build": context.config.userdata.get('label') + ' | Berlin Sanity | Build ' + context.config.userdata.get(
            'build') + '| Env: ' + context.config.userdata.get('env'),
        "appium:bundleId": set_app_build_device(context),
        # "appium:bundleId": set_cloud_device(context),
        "appium:xcodeOrgId": "CN89264FDM",
        "appium:xcodeSigningId": "Sharecare Inc",
        "appium:udid": "00008110-001A758821E9801E",
        "job-name": context.config.userdata.get('label') + ' | ' + context.feature.filename,
        "job-build": context.config.userdata.get('label') + ' | ' + context.feature.filename,
        "name": context.config.userdata.get('label') + ' | ' + context.feature.name,
        "sauce:options": sauce_options(context)
    }

    return desired_capabilities


def before_all(context):
    os.environ['TESTRAIL_USER'] = os.environ.get("TESTRAIL_USERNAME")
    os.environ['TESTRAIL_KEY'] = os.environ.get("TESTRAIL_PASSWORD")
    userdata = context.config.userdata
    ev = {'env': context.config.userdata.get('env'), 'market': context.config.userdata.get('market')}

    continue_after_failed = userdata.getbool("runner.continue_after_failed_step", True)
    Scenario.continue_after_failed_step = continue_after_failed
    # Change this to get the current build branch of your CI system
    # if 'ios' in context.config.userdata.get('platform'):


def before_feature(context, feature):
    # if 'android' in feature.tags:

    if 'android' in context.config.userdata.get('platform'):
        if context.config.userdata.get('platform') == 'android_device':
            desired_capabilities = android_device_setup(context)
            logger.info("Running on Android Physical Device")
            context.driver = webdriver.Remote(set_appium_connection_url(context), desired_capabilities)

        # env = context.config.userdata.get("env")
        # android_env_flow(context, env)
        elif context.config.userdata.get('platform') == 'android_emulator':
            desired_capabilities = android_emulator_setup(context)
            logger.info("Running on Android Emulator")
            context.driver = webdriver.Remote(set_appium_connection_url(context), desired_capabilities)
            # env = context.config.userdata.get("env")
            # android_env_flow(context, env)

        elif context.config.userdata.get('platform') == 'cloud_android':
            desired_capabilities = cloud_android_setup(context)
            logger.info("Running on Android Cloud Device")
            context.driver = webdriver.Remote(set_appium_connection_url(context),
                                              desired_capabilities)
            # context.driver = webdriver.Remote('https://ondemand.eu-central-1.saucelabs.com/wd/hub',desired_capabilities)
        elif context.config.userdata.get('platform') == 'android_ios_parallel':
            desired_capabilities1 = cloud_ios_setup(context)
            desired_capabilities2 = cloud_android_setup(context)
            logger.info("Running on Parallel Devices")
            context.driver = webdriver.Remote(set_appium_connection_url(context),
                                              desired_capabilities1)
            context.driver = webdriver.Remote(set_appium_connection_url(context),
                                              desired_capabilities2)

        else:
            logger.error("Devices not configured")
            # Trying nothing serious
        context.helper_functions = HelperFunctions(context.driver)
        context.splash_screen = SplashScreen(context)
        context.login_screen = LoginScreen(context)
        context.create_account = CreateAccount(context)
        context.you = YouScreen(context)
        context.settings = Settings(context)
        context.guided_tooltips = GuidedToolTips(context)
        context.home = HomeScreen(context)
        context.about = About(context)
        context.legal_privacy = LegalPrivacy(context)
        context.communications = Communications(context)
        context.missing_field_screen = MissingFieldScreens(context)
        context.security_pin = SecurityPIN(context)
        context.account = Account(context)
        context.search_screen = SearchScreen(context)
        context.discover = Discover(context)
        context.forgot_password = ForgotPassword(context)

        # Set environment on APP
        # @ToDo - Add catch block...
        context.set_env = SetupEnv(context)
        if 'STAGE' in context.config.userdata.get('env'):
            market = str(context.config.userdata.get('market'))
            env = str(context.config.userdata.get('env'))
            if 'SC' in context.config.userdata.get('label'):
                context.set_env.set_environment_market('sc', market.upper(), env.upper())
            if 'CF' in context.config.userdata.get('label'):
                context.set_env.set_environment_market('cf', market.upper(), env.upper())
        elif 'UAT' in context.config.userdata.get('env'):
            # market = str(context.config.userdata.get('market'))
            # env = str(context.config.userdata.get('env'))
            # if 'SC' in context.config.userdata.get('label'):
            #     context.set_env.set_environment_market('sc', market.upper(), env.upper())
            # if 'CF' in context.config.userdata.get('label'):
            #     context.set_env.set_environment_market('cf', market.upper(), env.upper())
            pass
        elif 'PROD' in context.config.userdata.get('env'):
            market = str(context.config.userdata.get('market'))
            env = str(context.config.userdata.get('env'))
            if 'SC' in context.config.userdata.get('label'):
                context.set_env.set_environment_market('sc', market.upper(), env.upper())
            if 'CF' in context.config.userdata.get('label'):
                context.set_env.set_environment_market('cf', market.upper(), env.upper())
        else:
            pass



    elif 'ios' in context.config.userdata.get('platform'):
        logger.info("Running on iOS")

        if context.config.userdata.get('platform') == 'ios_device':
            desired_capabilities = ios_real_device_setup(context)
            logger.info("Running on iOS Physical Device")
            context.driver = webdriver.Remote(set_appium_connection_url(context), desired_capabilities)

        elif context.config.userdata.get('platform') == 'ios_simulator':
            desired_capabilities = ios_simulator_setup(context)
            logger.info("Running on iOS Simulator Device")
            context.driver = webdriver.Remote(set_appium_connection_url(context), desired_capabilities)
        elif context.config.userdata.get('platform') == 'cloud_ios':
            desired_capabilities = cloud_ios_setup(context)
            logger.info("Running on iOS Cloud Device")
            context.driver = webdriver.Remote(set_appium_connection_url(context),
                                              desired_capabilities)
        else:
            print("Platform not found")
        context.helper_functions = HelperFunctions(context.driver)
        context.splash_screen = SplashScreen(context)
        context.login_screen = LoginScreen(context)
        context.create_account = CreateAccount(context)
        context.you = YouScreen(context)
        context.settings = Settings(context)
        context.guided_tooltips = GuidedToolTips(context)
        context.home = HomeScreen(context)
        context.about = About(context)
        context.legal_privacy = LegalPrivacy(context)
        context.communications = Communications(context)
        context.missing_field_screen = MissingFieldScreens(context)
        context.security_pin = SecurityPIN(context)
        context.account = Account(context)
        context.search_screen = SearchScreen(context)
        context.discover = Discover(context)
        context.forgot_password = ForgotPassword(context)
        context.set_env = SetupEnv(context)
        # market = str(context.config.userdata.get('market'))
        # env = str(context.config.userdata.get('env'))
        # context.set_env.set_env_market_ios(context, market.upper(), env.upper())
        # context.set_env.reactivate_app(context)

    else:
        logger.error("Device not Setup correctly")


# check update
def after_feature(context, feature):
    # time.sleep(1)
    # context.driver.save_screenshot("features/reports/screen_final.png")
    # + ' on ' + context.config.userdata.get(
    #     'platform') +

    if 'android' in context.config.userdata.get('platform'):
        platform = 'Android'
        # current_branch = platform + ' ' + context.config.userdata.get('cycle') + ' | ' + context.config.userdata.get(
        #     'release') + ' | ' + context.config.userdata.get(
        #     'app_type') + ' ' + context.config.userdata.get(
        #     'app_version') + ' (' + context.config.userdata.get(
        #     'build') + ') | ENV: ' + context.config.userdata.get(
        #     'env')

        if 'STAGE' in context.config.userdata.get('env'):
            app_type = 'R-CANDI'
            cycle = 'SANITY'
            if 'CF' in context.config.userdata.get('label'):
                label = 'CF | '
            else:
                label = 'SC | '
            current_branch = label + platform + ' ' + cycle + ' | ' + context.config.userdata.get(
                'release') + ' | ' + app_type + ' ' + context.config.userdata.get(
                'app_version') + ' (' + context.config.userdata.get(
                'build') + ')'

        if 'UAT' in context.config.userdata.get('env'):
            if 'CF' in context.config.userdata.get('label'):
                label = 'CF | '
            else:
                label = 'SC | '
            app_type = 'Beta-UAT'
            cycle = 'SANITY'
            current_branch = label + platform + ' ' + cycle + ' | ' + context.config.userdata.get(
                'release') + ' | ' + app_type + ' ' + context.config.userdata.get(
                'app_version') + ' (' + context.config.userdata.get(
                'build') + ')'

    elif 'ios' in context.config.userdata.get('platform'):
        platform = 'iOS'
        # current_branch = platform + ' ' + context.config.userdata.get('cycle') + ' | ' + context.config.userdata.get(
        #     'release') + ' | ' + context.config.userdata.get(
        #     'app_type') + ' ' + context.config.userdata.get(
        #     'app_version') + ' (' + context.config.userdata.get(
        #     'build') + ') | ENV: ' + context.config.userdata.get(
        #     'env')

        if 'STAGE' in context.config.userdata.get('env'):
            app_type = 'R-CANDI'
            cycle = 'SANITY'
            if 'CF' in context.config.userdata.get('label'):
                label = 'CF | '
            elif 'CF-ALPHA' in context.config.userdata.get('label'):
                label = 'CF-ALPHA | '
            elif 'SC-ALPHA' in context.config.userdata.get('label'):
                label = 'SC-ALPHA | '
            else:
                label = 'SC | '
            current_branch = label + platform + ' ' + cycle + ' | ' + context.config.userdata.get(
                'release') + ' | ' + app_type + ' ' + context.config.userdata.get(
                'app_version') + ' (' + context.config.userdata.get(
                'build') + ')'

        if 'UAT' in context.config.userdata.get('env'):
            if 'CF' in context.config.userdata.get('label'):
                label = 'CF | '
            else:
                label = 'SC | '
            app_type = 'Beta-UAT'
            cycle = 'SANITY'
            current_branch = label + platform + ' ' + cycle + ' | ' + context.config.userdata.get(
                'release') + ' | ' + app_type + ' ' + context.config.userdata.get(
                'app_version') + ' (' + context.config.userdata.get(
                'build') + ')'

    else:
        'Platform not found'
    # current_branch = platform + context.config.userdata.get('app_version') + '|Env: ' + context.config.userdata.get('env')
    testrail_reporter = TestrailReporter(current_branch)
    context.config.reporters.append(testrail_reporter)
    # Teams integration
    if "prod" in context.config.userdata.get("env").lower():
        webhook = webhooks['prod']
        push_to_teams(webhook, testrail_reporter, current_branch, testrail_reporter.testrail_run)
    elif "uat" in context.config.userdata.get("env").lower():
        webhook = webhooks['uat']
        push_to_teams(webhook, testrail_reporter, current_branch, testrail_reporter.testrail_run)
    elif "stage" in context.config.userdata.get("env").lower():
        webhook = webhooks['stage']
        push_to_teams(webhook, testrail_reporter, current_branch, testrail_reporter.testrail_run)
    else:
        logger.info("Failed to create a teams connection")
    context.driver.quit()
