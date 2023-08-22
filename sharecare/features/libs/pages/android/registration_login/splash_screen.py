# Landing page Screen Objects -Android
# No test data required - Just validating application is able to start successfully
import time

from sharecare.keywords.android.android_locator_keywords import splash_screen
from sharecare.utilities.custom_logger import CustomLogger
from sharecare.utilities.helper_functions import HelperFunctions


class SplashScreen(HelperFunctions):
    logger = CustomLogger.custom_logger()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)

    # Dummy implementation
    def check_splash_screen(self):
        """
        Verify elements on the splash screen
        """
        sign_in_btn = self.find(splash_screen["_SIGN_IN_BTN_"]).is_displayed()
        create_account_btn = self.find(splash_screen["_CREATE_ACCOUNT_BTN_"]).is_displayed()
        return sign_in_btn, create_account_btn
