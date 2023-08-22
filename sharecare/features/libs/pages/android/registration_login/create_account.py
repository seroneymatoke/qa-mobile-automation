"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 29.10.21
Purpose: House all the create account objects
Implementation:
TestData: 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from sharecare.keywords.android.android_locator_keywords import splash_screen, login_onboarding_screen, gender
from sharecare.test_data.test_data import password_configurations, get_country
from sharecare.utilities.helper_functions import HelperFunctions
from faker import Faker


class CreateAccount(HelperFunctions):

    faker = Faker()
    password = faker.password()

    def __init__(self, context):
        """
        Initializing helper functions
        """
        HelperFunctions.__init__(self, context.driver)
        time.sleep(5)
    # faker password

    def click_create_account(self):
        """
        Click create account
        """
        self.tap_element(splash_screen["_CREATE_ACCOUNT_BTN_"])

    def confirm_country(self, country):
        """
        Select country
        """
        self.tap_element(login_onboarding_screen['_COUNTRY_NAME_'])
        self.tap_element(login_onboarding_screen['_SEARCH_'])
        try:
            self.search(login_onboarding_screen['_SEARCH_FIELD_'], country)
            print("Selected country" + country)
        except NoSuchElementException:
            selection = get_country()
            self.search(login_onboarding_screen['_SEARCH_FIELD_'], selection)
            print("Selected country" + selection)
        self.tap_element(login_onboarding_screen['_COUNTRY_NAME_'])

    def click_continue(self):
        """
        Click continue
        """
        self.tap_element(login_onboarding_screen['_CONTINUE_'])

    def set_first_name(self, first_name):
        """
        Set first name
        """
        self.find(login_onboarding_screen["_ONBOARDING_FIRST_NAME_"]).clear()
        self.find(login_onboarding_screen["_ONBOARDING_FIRST_NAME_"]).send_keys(first_name)

    def set_last_name(self, last_name):
        """
        Set last name
        """
        self.find(login_onboarding_screen["_ONBOARDING_LAST_NAME_"]).clear()
        self.find(login_onboarding_screen["_ONBOARDING_LAST_NAME_"]).send_keys(last_name)

    def set_email(self, email):
        """
        set email
        """
        self.find(login_onboarding_screen["_ONBOARDING_EMAIL_"]).clear()
        self.find(login_onboarding_screen["_ONBOARDING_EMAIL_"]).send_keys(email)

    def set_birth_date(self, year, month, day):
        """
        Caveat: I know it works. Not so sure how the date picker works. Inherited as is
        Set Birth date
        """
        print(year+" "+month+ " "+day)
        # ToDo - Fix swipe scroll functions
        # self.date_picker_android(year, month, day, login_onboarding_screen['_ONBOARDING_BIRTH_DATE_'],
        #                          login_onboarding_screen['_ONBOARDING_YEAR_'],
        #                          login_onboarding_screen['_ONBOARDING_YEAR_PICKER_'],
        #                          login_onboarding_screen['_ONBOARDING_NEXT_MONTH_'],
        #                          login_onboarding_screen['_ONBOARDING_BIRTH_DATE_OK_'])
        self.tap_element(login_onboarding_screen['_ONBOARDING_BIRTH_DATE_'])
        self.tap_element(login_onboarding_screen['_ONBOARDING_BIRTH_DATE_OK_'])

    # ToDo - To add list support to gender selection in Helper Functions
    def set_gender(self):
        """
        select gender

        """
        # self.select_from_list(login_onboarding_screen['_ONBOARDING_GENDER_'], random.choice(gender))
        # User selection need to raise an issue with @sebastian to ids to choice selections

        print("waiting for user input")
        self.tap_element(login_onboarding_screen['_ONBOARDING_GENDER_'])
        gender = [
                # TouchAction(self.driver).tap(x=142, y=1399).perform(),
                TouchAction(self.driver).tap(x=113, y=1516).perform(),
                TouchAction(self.driver).tap(x=117, y=1647).perform(),
                TouchAction(self.driver).tap(x=104, y=1774).perform()
        ]
        random.choice(gender)

    def set_zip_code(self, zip_code):
        """
        Set zip code
        """
        self.find(login_onboarding_screen["_ZIPCODE_"]).clear()
        self.find(login_onboarding_screen["_ZIPCODE_"]).send_keys(zip_code)
        self.driver.hide_keyboard()
        #time.sleep(5)

    def set_password(self, new_password):
        """
        Set zip code
        """
        self.swipe_direction_android("down", 2)
        self.find(login_onboarding_screen["_ONBOARDING_NEW_PASSWORD_"]).clear()
        self.find(login_onboarding_screen["_ONBOARDING_NEW_PASSWORD_"]).send_keys(new_password)
        self.driver.hide_keyboard()

    def set_confirm_password(self, new_password):
        """
        Set confirm password
        """
        self.find(login_onboarding_screen["_ONBOARDING_CONFIRM_NEW_PASSWORD_"]).clear()
        self.find(login_onboarding_screen["_ONBOARDING_CONFIRM_NEW_PASSWORD_"]).send_keys(new_password)
        self.driver.hide_keyboard()
        self.swipe_direction_android("down", 2)

    def check_terms_and_conditions(self, condition):
        """
        click terms and conditions
        """
        self.driver.hide_keyboard()
        if condition == "enabled":
            self.tap_element(login_onboarding_screen['_ONBOARDING_TERMS_CONDITIONS_'])
        else:
            print("Not clicked")
        time.sleep(3)

    def validate_page_elements(self):
        # time.sleep(10)
        self.validate_element_presence(login_onboarding_screen['_ONBOARDING_TERMS_CONDITIONS_'])
        self.validate_element_presence(login_onboarding_screen['_ONBOARDING_FIRST_NAME_'])
        self.validate_element_presence(login_onboarding_screen['_ONBOARDING_LAST_NAME_'])
        self.validate_element_presence(login_onboarding_screen["_ONBOARDING_NEW_PASSWORD_"])
        self.validate_element_presence(login_onboarding_screen["_ONBOARDING_CONFIRM_NEW_PASSWORD_"])
        self.validate_element_presence(login_onboarding_screen["_ZIPCODE_"])
        self.validate_element_presence(login_onboarding_screen["_EMAIL_"])
        self.validate_element_presence(login_onboarding_screen["_PRIVACY_TERMS_CONDITIONS_"])

    def click_create(self):
        self.tap_element(login_onboarding_screen['_ONBOARDING_CREATE_'])
        time.sleep(10)

    def validate_passwords(self):
        # validate various passwords configurations
        print("HERE: STUFF")
        for i in password_configurations:
            self.set_password(password_configurations[i])
            print(password_configurations[i])
            element = self.find(login_onboarding_screen["_ONBOARDING_CONFIRM_NEW_PASSWORD_"])
            assert element.is_enabled() == False




