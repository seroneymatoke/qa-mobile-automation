"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 26.10.21
Purpose: Houses all the helper functions used by zeus
Implementation: HelperFunctions.function_name
TestData: None require
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import configparser
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    InvalidElementStateException, InvalidSessionIdException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sharecare.keywords.android.android_locator_keywords import home_screen, android_alert_buttons
from sharecare.utilities.custom_logger import CustomLogger

config = configparser.RawConfigParser()
config.read("sharecare/configs/config.ini")


class HelperFunctions(object):
    logger = CustomLogger.custom_logger()

    def __init__(self, browser):
        """
        Initializing the helper function class
        """
        self.driver = browser

    # implement Liam's Logic
    def find_by_xpath(self, text, time_out=30):
        ignored_exceptions = (StaleElementReferenceException, InvalidElementStateException)
        elem = '//*[@text="' + text + '" or @content-desc="' + text + '" or @resource-id="com.sharecare.realgreen:id/' + text + '" or @resource-id="com.sharecare.realgreen.alpha:id/' + text + '" or @resource-id="com.sharecare.realgreen.experimental:id/' + text + '" or @resource-id="' + text + '"]'
        # elem = '//*[contains(text() or content-desc() or resource-id(), ' +text+ ')]'
        try:
            element = WebDriverWait(self.driver, time_out, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_element_located((MobileBy.XPATH, elem)))
            return element
        except TimeoutException as e:
            self.logger.info("Element not Found: " + text)

    def find_element_by_partial_text(self, text, time_out=30):
        ignored_exceptions = (StaleElementReferenceException, InvalidElementStateException)

        elem = '// *[text()[contains(.,"' + text + '")]] '
        try:
            element = WebDriverWait(self.driver, time_out, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_element_located((MobileBy.XPATH, elem)))
            return element

        except TimeoutException as e:
            self.logger.info("Element not Found: " + text)

    # @todo - To be changed to find by accessibility id for iOS.

    def find_by_ios_xpath(self, text, time_out=30):

        ignored_exceptions = (StaleElementReferenceException, InvalidElementStateException, InvalidSessionIdException)
        # elem = '//[@name="' + text + '" or //*[@text="' + text + '" or @label="' + text + '" or @name="' + text + '" or @resource-id="com' \
        #                                                                                                           '.sharecare.realgreen:id/' + \
        #        text + '" or @resource-id="' + text + '"] '
        e = '//XCUIElementTypeButton[@name="' + text + '" or @label="' + text + '"]'

        elem = '//*[@name="' + text + '" or @label="' + text + '" or @value="' + text + '"]'
        try:
            element = WebDriverWait(self.driver, time_out, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_element_located((MobileBy.XPATH, elem)))
            return element
        except TimeoutException as e:
            self.logger.info("Element not Found: " + text)

    # Funny iOS buttons
    def find_by_ios_elem_xpath(self):
        pass

    def find(self, selector, time_out=30):
        """
        Used to get all elements as defined by the locator strategy in the keywords folders
        """
        # time.sleep(3)
        # introducing polling
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.presence_of_element_located((selector[0], selector[1])))
            # return self.driver.find_element(selector[0], selector[1])
            return element
        except TimeoutException as e:
            self.logger.error("Element not found: " + str(selector))

    def set_text_box_value(self, selector, value):
        textbox = self.find(selector)
        textbox.clear()
        self.logger.info("Entered Values: " + value)
        return textbox.send_keys(value)

    def scroll_to_element(self, selector):
        # scroll to element
        actions = ActionChains(self.driver)
        return self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()).scrollIntoView(text(\"" + selector + "\"))")

    def find_elements(self, selector):
        # returns elements as a list
        return self.driver.find_elements(selector[0], selector[1])

    def get_page_title(self, title):
        page_title = self.driver.title
        self.logger.info(page_title)
        if title.lower() in page_title.lower():
            return True
        else:
            return False

    def touch_by_coordinates(self, x_coords, y_coords):
        return TouchAction(self.driver).tap(x=x_coords, y=y_coords).perform()

    def step_back(self):
        # Step Back on Step
        return self.driver.back()

    def step_back_x_times(self, times):
        self.logger.info("Going back: " + times + " steps")
        for i in times:
            self.driver.press_keycode(4)

    def push_app_to_background(self, time_in_seconds):
        # Pushes app to background - Currently used by the settings Set PIN screen.
        self.driver.background_app(time_in_seconds)

    def tap_by_accessibility_id(self, element):
        """
        When I click on the accessibility-id "element"
        Currently only used by the date Picker
        """
        selector = self.driver.find_element_by_accessibility_id(element)
        selector.click()

    def get_element_size_and_location(self, selector):
        """
        Get element size and location
        Returns dict that holds height, width, x and y values
        """
        return self.find(selector).rect

    def search(self, selector, text):
        """
        Returns searched text
        """
        self.logger.info("Searching for: " + text)
        element = WebDriverWait(self.driver, self.get_time_out('default_timeout')).until(
            EC.element_to_be_clickable(self.find(selector)))
        element.clear()
        return element.send_keys(text)

    def tap_element(self, selector, time_out=30):
        """
        Taps on element upon search and selection
        """
        # time.sleep(3)
        try:
            element = WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable((selector[0], selector[1])))
            # element = WebDriverWait(self.driver, self.get_timeout('default_timeout')).until(
            #     EC.element_to_be_clickable(self.find(selector)))
            # self.logger.info("Ongoing Stuff")
            # # element = self.driver.find_element(selector[0], selector[1])
            # # element = self.find(selector)
            self.logger.info("I clicked on: " + str(selector))
            element.click()
            # time.sleep(10)
        except NoSuchElementException:
            self.logger.error("exception thrown when tapping " + str(selector))

    def android_default_ok(self):
        # Click ok on android pop up ok
        element = self.find(android_alert_buttons['_MESSAGE_'])
        self.logger.info("pop up message: " + element.text)
        self.tap_element(android_alert_buttons['_OK_'])

    def android_default_cancel(self):
        # Click ok on android pop up cancel
        self.logger.info("clicked cancel on alert")
        self.tap_element(android_alert_buttons['_CANCEL_'])

    def scroll_to(self, start, finish):
        """
        Scroll from element to element
        """
        element1 = self.find(start)
        element2 = self.find(finish)
        action = TouchAction(self.driver)
        action.press(element1).move_to(element2).release().perform()

    def select_from_list(self, selector, value):
        self.tap_element(selector)
        self.driver.find_element(MobileBy.PARTIAL_LINK_TEXT, value).click()

    def contains_content(self, selector, text):
        """
        Validate if text is present
        """
        try:
            element = self.find(selector)
            self.logger.info("inside try: " + element.text)
            if element.text == text:
                print("Matching")
                return True
            else:
                self.logger.error("Not Matching")
                return False
        except NoSuchElementException as e:
            self.logger.error(e)
            return False

    # ToDo - Need to convert this to a for loop
    def validate_element_presence(self, selector):
        """
        Validate presence of elements on a page
        """
        self.logger.info("Trying to find element: " + str(selector))
        # time.sleep(10)
        try:
            element = self.find(selector)
            self.logger.info("Beginning presence of : " + str(element))
            if element.is_displayed():
                self.logger.info("Element is present: " + str(element))
                return True
            else:
                return False

        except NoSuchElementException as e:
            self.logger.error(e)
        return False

    # @todo - Check Screen Aggregation size and scroll percentage.
    def swipe_with_touch_action(self, direction, times):
        """
            This method is master method for all scroll or swipe gestures
                # Find size of mobile device screen
                # Calculate width and height upon screen size
                # Define start and stop point
                # Implement swipe action
                TODO: use swipe percentage
        """
        global start_x, start_y, duration, end_x, end_y
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        if direction == "down":
            start_x = width * 0.1
            start_y = round(height * 0.4)
            end_x = start_x
            end_y = round(height * 0.1)
            duration = 800
        elif direction == "up":
            start_x = width * 0.5
            start_y = round(height * 0.5)
            end_x = start_x
            end_y = round(height * 0.9)
            duration = 800
        elif direction == "right":
            start_x = width * 0.9
            start_y = round(height * 0.9)
            end_x = width * 0.5
            end_y = round(height * 0.5)
            duration = 800
        elif direction == "left":
            start_x = width * 0.9
            start_y = round(height * 0.9)
            end_x = width * 0.5
            end_y = round(height * 0.5)
            duration = 800
        for i in range(int(times)):
            touch = TouchAction(self.driver)
            touch.press(x=start_x, y=start_y).wait(ms=duration).move_to(x=end_x, y=end_y).release().perform()

    # def swipe_direction(self,context, direction, times):
    #     """
    #     phrase : I swipe "{direction}" direction "{times}" times
    #     Method has different logic for android and ios
    #     For android, method calls swipe_with_touchAction method
    #     """
    #     #    touch = TouchAction(self.driver)
    #     if 'android' in context.config.userdata.get('platform'):
    #         print("swipe android")
    #         self.swipe_with_touch_action(direction, times)
    #     elif 'ios' in config.userdata.get('platform'):
    #         print("swipe ios")
    #         for i in range(int(times)):
    #             self.driver.execute_script("mobile: scroll", {"direction": direction})

    def swipe_direction_android(self, direction, times):
        touch = TouchAction(self.driver)
        self.swipe_with_touch_action(direction, times)

    def swipe_direction_ios(self, direction, times):
        touch = TouchAction(self.driver)
        for i in range(int(times)):
            self.driver.execute_script("mobile: scroll", {"direction": direction})

    def swipe_with_coordinates(self, press_x, press_y, move_x, move_y):
        """
            phrase: Scroll with coordinates "{pressX}", "{pressY}","{moveX}","{moveY}"
            this method can be used only specific situation
            it might be deprecated soon
        """
        touch = TouchAction(self.driver)
        touch.press(x=press_x, y=press_y)
        touch.move_to(x=move_x, y=move_y)
        touch.release()
        touch.perform()

    def swipe_on_given_element(self, direction, selector):
        """
        phrase : I swipe to "{direction}" on "{element}" specific element
        Find max width and height of device
        Find location of given element
        Swipe given direction on element
        """

        info = self.get_element_size_and_location(selector)
        w = info['width']
        h = info['height']
        element_center_y = info['y'] + round(h * 0.5)
        duration = 500

        touch = TouchAction(self.driver)
        if direction == "left":
            touch.press(x=w, y=element_center_y). \
                wait(ms=duration).move_to(x=round(w * 0.1), y=element_center_y). \
                release().perform()
        elif direction == "right":
            touch.press(x=w + 5, y=element_center_y). \
                wait(ms=duration).move_to(x=round(w * 0.9), y=element_center_y). \
                release().perform()

    def swipe_android(self):
        """
            phrase : I swipe on Android
            Method measures screen width and height.
            Thus swipe action covers all android devices.
        """
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        print(width, height)
        start_x = width * 0.5
        start_y = height * 0.9
        end_x = start_x
        end_y = height * 0.4
        duration = 800
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def date_picker_android(self, year, month, day, selector_date, selector_year, selector_year_picker,
                            selector_next_month_picker, confirm_date_button):
        """
                phrase: I pick date "{year}" year, "{month}" month, "{day}" day
                Method sets given value to desired date picker element such as day, month and year
                Method is relevant to android
            """
        self.tap_element(selector_date)
        self.tap_element(selector_year)
        # locator = keywords.transform(context, "_ONBOARDING_YEAR_PICKER_")
        year_list = []
        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                      'August', 'September', 'October', 'November', 'December']
        index = month_list.index(month)
        self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()).scrollIntoView(text(\"" + year + "\"))")

        # if int(year) < 1980:
        #     while not (str(year)) in year_list:
        #         self.swipe_direction_android("down", 1)
        #         time.sleep(1)
        #
        #         shown_years = self.find(selector_year_picker)
        #         for years in shown_years:
        #             year_list.append(years.text)
        # else:
        #     while not (str(year)) in year_list:
        #         self.swipe_direction_android("up", 1)
        #         time.sleep(1)
        #
        #         shown_years = self.find(selector_year_picker)
        #         for years in shown_years:
        #             year_list.append(years.text)

        self.tap_by_accessibility_id(year)

        if month != "January":
            for i in range(int(index)):
                self.tap_element(selector_next_month_picker)

        print(day + " " + month + " " + year)
        self.tap_by_accessibility_id(day + " " + month + " " + year)
        self.tap_element(confirm_date_button)

    @staticmethod
    def get_screenshot_path(path):
        """
        Gets paths to screenshot folders if need
        """
        screenshot_path = config.get('common-info', path)
        return screenshot_path

    @staticmethod
    def get_time_out(timeout):
        """
        Gets timeout as set in the config.ini
        """
        timeout = config.get('timeouts', timeout)
        print(timeout)
        return timeout
