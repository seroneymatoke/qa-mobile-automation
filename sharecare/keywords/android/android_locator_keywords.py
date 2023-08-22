# Houses all locators and access methods

from appium.webdriver.common.mobileby import MobileBy

select_environment = {
    # Enabled in debug mode to select Market and environment
    "_SHARECARE_LOGO_": (MobileBy.XPATH, '//android.widget.TextView[@text="PRODUCTION – US"]'),
    "_SELECT_MARKET_": (MobileBy.ID, 'com.sharecare.realgreen:id/selectMarket'),
    "_SELECT_ENVIRONMENT_": (MobileBy.ID, 'com.sharecare.realgreen:id/selectEnvironment'),

    "_CF_LOGO_": (MobileBy.ID, 'com.sharecare.carefirst:id/debug_subtitle'),
    "_CF_SELECT_MARKET_": (MobileBy.ID, 'com.sharecare.carefirst:id/selectMarket'),
    "_CF_SELECT_ENVIRONMENT_": (MobileBy.ID, 'com.sharecare.carefirst:id/selectEnvironment')

}

envs = {
    "_STAGING_": (MobileBy.XPATH, '//android.widget.TextView[@text="STAGE"]'),
    "_PRODUCTION_": (MobileBy.XPATH, '//android.widget.TextView[@text="PRODUCTION"]'),
    "_UAT_": (MobileBy.XPATH, '//android.widget.TextView[@text="UAT"]'),
    "_QA_": (MobileBy.XPATH, '//android.widget.TextView[@text="QA"]')
}

markets = {
    "_US_": (MobileBy.XPATH, '//android.widget.TextView[@text="United States"]'),
    "_NZ_": (MobileBy.XPATH, '//android.widget.TextView[@text="New Zealand"]'),
    "_BR_": (MobileBy.XPATH, '//android.widget.TextView[@text="Brazil"]'),
}


gender = ["Male", "Female", "Other", "Prefer no to answer"]

cookies_settings = {

}

discover = {
    '_COMM_WELL_BEING_': (MobileBy.XPATH, '//android.widget.TextView[@text="Community Well-Being"]'),
    '_COMM_WELL_WEBVIEW_': (MobileBy.XPATH, '//android.widget.TextView[@text="Community Well-Being Index"]'),
    '_INSPIRATION_': (MobileBy.XPATH, '//android.widget.TextView[@text="Inspirations"]'),
    '_MED_PRICES_': (MobileBy.XPATH, '//android.widget.TextView[@text="Medication Prices"]'),

    '_FIND_DOCTOR_': (MobileBy.XPATH, '//android.widget.TextView[@text="Find a Doctor"]'),
    '_MD_PRICES_WEBVIEW_': (MobileBy.ID, 'com.sharecare.realgreen:id/webView'),
    # Find a doctor
    '_FIND_DOC_WEBVIEW_': (MobileBy.ID, 'com.sharecare.realgreen:id/webView'),
    '_DOC_SPEC_TXT_': (MobileBy.ID, 'what'),
    '_DOC_LOCATION_TXT_': (MobileBy.ID, 'where'),
    '_SEARCH_BTN_': (MobileBy.XPATH, '//android.widget.Button[@text="Search"]'),
    '_SEARCH_RESULTS_': (MobileBy.XPATH, '//android.widget.TextView[1]'),
    '_DOC_PHONE_': (MobileBy.XPATH, '//android.view.View[@content-desc="Phone icon Call"]'),
    '_ABOUT_DOC_': (MobileBy.XPATH, '//android.widget.TextView[1][@text="About"]'),
    '_ADD_TO_CARE_': (MobileBy.XPATH, '//android.view.View[@content-desc="+ Add to care team"]/android.widget.TextView'),
    '_REMOVE_FROM_CARE_': (MobileBy.XPATH, '//android.view.View[@content-desc="− Remove from care team"]/android.widget.TextView'),

    # Health Topics
    '_HEALTH_TOPICS_': (MobileBy.XPATH, '//android.widget.TextView[@text="Health Topics"]'),
    '_TOPICS_WEBVIEW_': (MobileBy.ID, 'com.sharecare.realgreen:id/recyclerView'),
    '_TOPICS_FILTER_': (MobileBy.ID, 'com.sharecare.realgreen:id/menu_item_filter'),
    '_FOLLOW_BTN_': (MobileBy.ID, 'com.sharecare.realgreen:id/btn_follow'),
    '_FOLLOWING_BTN_': (MobileBy.ID, 'com.sharecare.realgreen:id/btn_following'),
    '_ALL_TOPICS_RD_BTN_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="All Topics"]'),
    '_FOLLOWING_RD_BTN_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Following"]'),
    '_IMG_HT_DTL_': (MobileBy.ID, 'com.sharecare.realgreen:id/im_topic_image'),
    '_DTL_VIEW_HT_': (MobileBy.ID, 'com.sharecare.realgreen:id/image_view'),

}
trackers = {
    '_ACTIVATE_': (MobileBy.ID, 'com.sharecare.realgreen:id/button_activate'),
    '_UPD_SETTINGS_':(MobileBy.ID, 'com.sharecare.com:id/update_settings'),
    '_NOT_NOW_': (MobileBy.ID, 'com.sharecare.realgreen:id/button_not_now'),
    '_NXT_BUTTON_': (MobileBy.ID, 'com.sharecare.realgreen:id/button_next'),
    '_SLEEP_': (MobileBy.ID, 'com.sharecare.realgreen:id/switch_sleep'),
    '_STEPS_': (MobileBy.ID, 'com.sharecare.realgreen:id/switch_steps'),
    '_GOOGLE_FIT_': (MobileBy.ID, 'com.sharecare.realgreen:id/google_fit_connect'),
    '_FITBIT_': (MobileBy.ID, 'com.sharecare.realgreen:id/fitbit_connect'),
    '_SAMSUNG_HEALTH_': (MobileBy.ID, 'com.sharecare.realgreen:id/samsungHealthConnect'),
    '_SKIP_TOOLTIP_': (MobileBy.ID, 'com.sharecare.realgreen:id/skip_button'),
    '_ADD_ENTRIES_': (MobileBy.ID, 'com.sharecare.realgreen:id/add_entries_button'),
    '_DONE_BUTTON_': (MobileBy.ID, 'com.sharecare.realgreen:id/button_done'),
    '_DRINK_YES_': (MobileBy.ID, 'com.sharecare.realgreen:id/radio_button_one'),
    '_DRINK_NO_': (MobileBy.ID, 'com.sharecare.realgreen:id/radio_button_two'),
    '_DRINK_DROP_DOWN_': (MobileBy.ID, 'com.sharecare.realgreen:id/filled_exposed_dropdown'),
    '_DIABETIC_YES_': (MobileBy.ID, 'com.sharecare.realgreen:id/radio_button_one'),
    '_DIABETIC_NO_': (MobileBy.ID, 'com.sharecare.realgreen:id/radio_button_two'),
    '_BLD_SGR_': (MobileBy.ID, 'com.sharecare.realgreen:id/text_input_layout'),
    '_SYST_': (MobileBy.ID, 'com.sharecare.realgreen:id/text_input_layout'),
    '_DYST_': (MobileBy.ID, 'com.sharecare.realgreen:id/text_input_layout'),
    '_CHOL_': (MobileBy.ID, 'com.sharecare.realgreen:id/text_input_layout'),
    '_SAVE_': (MobileBy.XPATH, '//android.widget.Button[@text="Save"]'),
    '_TOP_DONE_': (MobileBy.ID, 'com.sharecare.realgreen:id/menu_item_done'),
    '_OK_BTN_': (MobileBy.ID, 'com.sharecare.realgreen:id/button'),
    '_DRP_DWN_': (MobileBy.ID, 'com.sharecare.realgreen:id/text_input_end_icon'),
    '_..._': (MobileBy.ID, 'com.sharecare.realgreen:id/edit_button'),
    
}

rat = {
    '_REAL_AGE_': (MobileBy.ID, 'com.sharecare.realgreen:id/realAge'),
    '_YOU_TAKE_RAT_': (MobileBy.ID, 'com.sharecare.realgreen:id/button'),
    '_YOU_COMPLETE_RAT_': (MobileBy.ID, 'com.sharecare.realgreen:id/button'),
    '_TAKE_RAT_': (MobileBy.ID, 'com.sharecare.realgreen:id/takeRealAge'),
    '_GET_STARTED_': (MobileBy.ID, 'com.sharecare.realgreen:id/get_started'),
    '_NOT_NOW_': (MobileBy.ID, 'com.sharecare.realgreen:id/take_later'),
    '_TAKE_SELFIE_': (MobileBy.ID, 'com.sharecare.realgreen:id/selfieButton'),
    '_SKIP_': (MobileBy.ID, 'com.sharecare.realgreen:id/skipButton'),
    '_CAPTURE_IMAGE_': (MobileBy.ID, 'com.sharecare.realgreen:id/capture_image'),
    '_CANCEL_': (MobileBy.ID, 'com.sharecare.realgreen:id/cancel'),
    '_PAUSE_': (MobileBy.ID, 'com.sharecare.realgreen:id/saveBtn'),
    '_MALE_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Male"]'),
    '_FEMALE_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Female"]'),
    '_HT_FEET_': (MobileBy.XPATH, '//android.widget.LinearLayout[1]'),
    '_HT_INS_': (MobileBy.XPATH, '//android.widget.LinearLayout[2]'),
    '_NEXT_': (MobileBy.ID, 'com.sharecare.realgreen:id/actionButton'),
    '_WEIGHT_': (MobileBy.ID, 'com.sharecare.realgreen:id/dropdown'),
    '_WAIST_': (MobileBy.ID, 'com.sharecare.realgreen:id/dropdown'),
    '_PE_EX_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Excellent"]'),
    '_PE_VG_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Very good"]'),
    '_PE_GD_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Good"]'),
    '_PE_FR_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Fair"]'),
    '_PE_PR_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Poor"]'),
    '_BP_YES': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Yes"]'),
    '_BP_NO_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="No"]'),
    '_BP_HG_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="High"]'),
    '_BP_AV_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Average"]'),
    '_BP_LO_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Low"]'),
    '_CHOL_YES': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Yes"]'),
    '_CHOL_NO_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="No"]'),
    '_CHOL_HG_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="High (Unhealthy)"]'),
    '_CHOL_AV_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Average"]'),
    '_CHOL_LO_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Low (Healthy)"]'),
    '_HDL_YES': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Yes"]'),
    '_HDL_NO_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="No"]'),
    '_HDL_CHOL_HG_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="High (unhealthy)"]'),
    '_HDL_CHOL_AV_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Average"]'),
    '_HDL_CHOL_LO_': (MobileBy.XPATH, '//android.widget.RadioButton[@text="Low (healthy)"]'),
}

splash_screen = {
    "_SIGN_IN_BTN_": (MobileBy.XPATH, '//android.widget.Button[@text="Sign In"]'),
    "_CREATE_ACCOUNT_BTN_": (MobileBy.XPATH, '//android.widget.Button[@text="Create Account"]'),
    #IOS
    "_SIGN_IN_BTN_IOS_": (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Sign In"]'),
}

error_messages_screen = {
    "_INVALID_CREDENTIALS_": (MobileBy.ID, 'android:id/message'),
    "_INVALID_ERROR_": (MobileBy.ID, 'com.sharecare.realgreen:id/textinput_error'),
    "_CLOSE_BTN_": (MobileBy.ID, 'android:id/button2')
}

android_alert_buttons = {
    "_OK_": (MobileBy.ID, 'android:id/button1'),
    "_CANCEL_": (MobileBy.ID, 'android:id/button2'),
    "_MESSAGE_": (MobileBy.ID, 'android:id/message')
}

# ToDo - Get Translations - Spanish
error_messages = {
    "_INVALID_CREDENTIALS_": 'The email or password you entered is invalid. Please try again.',
    "_INVALID_EMAIL_": 'Please enter a valid email',
    "_MISSING_PASSWORD_": 'Please enter a password'
}

language = {
    "_EN_": (MobileBy.XPATH, '//android.widget.RadioButton[@text="English (US)"]'),
    "_DE_": (MobileBy.XPATH, '//android.widget.RadioButton[@text="German (DE)"]')
}

achieve = {
    "_TITLE_": (MobileBy.ID, 'com.sharecare.realgreen:id/toolbarTextView'),
    "_CHALLENGES_": (MobileBy.XPATH, '//android.widget.TextView[@text="Challenges"]'),
    "_REWARDS_": (MobileBy.XPATH, '//android.widget.TextView[@text="Rewards"]'),
    "_PROGRAMS_": (MobileBy.XPATH, '//android.widget.TextView[@text="Programs"]'),
    # Webviews
    "_ACTIVE_": (MobileBy.ID, 'tabgroup-active-content'),

}

guided_tooltips_messages = {
    "_MESSAGE_1_": 'See your latest alerts and messages in the Notification Center. (1/4)',
    "_MESSAGE_2_": 'Take a moment and breathe with a relaxing scene. (2/4)',
    "_MESSAGE_3_": 'Here you can enter data for your tracked health factors. (3/4)',
    # "_MESSAGE_4_": 'Daily content personalized to lower your RealAge. (4/4)',
}

guided_tooltips = {
    "_NOTIFICATION_SKIP_": (MobileBy.ID, 'com.sharecare.realgreen:id/skip_button'),
    "_NOTIFICATION_NEXT_": (MobileBy.ID, 'com.sharecare.realgreen:id/action_button'),
    "_TOOLTIPS_MESSAGE_TXT_": (MobileBy.ID, 'com.sharecare.realgreen:id/bodyTxt'),
    "_DONE_": 'Done'
}

guided_ios_tooltips = {
    "_NOTIFICATION_SKIP_": (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Skip"]'),
    "_NOTIFICATION_NEXT_": (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Next"]'),
    "_TOOLTIPS_MESSAGE_TXT_": (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="See your latest alerts and messages in the Notification Center. (1/3)"]'),
    "_DONE_": (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Done"]')
}

about = {
    "_ABOUT_": (MobileBy.XPATH, '//android.widget.TextView[@text="About Sharecare"]'),
    "_ABOUT_TITLE_": (MobileBy.XPATH, '//android.widget.TextView[@text="About Our Digital Health and Wellness Company '
                                      '- Sharecare"]'),
}

support = {
    "_SUPPORT_WEBVIEW_": (MobileBy.ID, 'com.sharecare.realgreen:id/webView')
}

account = {
    "_EDIT_": (MobileBy.ID, 'com.sharecare.realgreen:id/rightTextBtn'),
    "_DELETE_ACCOUNT_": (MobileBy.ID, 'com.sharecare.realgreen:id/delete_account'),
    "_CHANGE_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/resetPw'),
    "_CURRENT_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_password'),
    "_NEW_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_password'),
    "_CONFIRM_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_confirm_password'),
    "_UPDATE_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/actionButton'),
    "_FIRST_NAME_": (MobileBy.ID, 'com.sharecare.realgreen:id/firstname'),
    "_LASTNAME_": (MobileBy.ID, 'com.sharecare.realgreen:id/lastname'),
    "_GENDER_": (MobileBy.ID, 'com.sharecare.realgreen:id/gender'),
    "_BIRTHDATE_": (MobileBy.ID, 'com.sharecare.realgreen:id/birthdate'),
    "_COUNTRY_": (MobileBy.ID, 'com.sharecare.realgreen:id/country'),
    "_POSTCODE_": (MobileBy.ID, 'com.sharecare.realgreen:id/zipcode'),
    "_PHONE_NUMBER_": (MobileBy.ID, 'com.sharecare.realgreen:id/phone'),
    "_DATA_TEXT_": (MobileBy.XPATH, '//android.widget.TextView[2]'),
    "_LABEL_TEXT_": (MobileBy.ID, 'com.sharecare.realgreen:id/content'),
    "_CHANGE_PHOTO_": (MobileBy.ID, 'com.sharecare.realgreen:id/change_profile_photo'),
    "_CHOOSE_FROM_LIB_": (MobileBy.XPATH, '//android.widget.TextView[@text="Choose From Library"]'),
    "_TAKE_PHOTO_": (MobileBy.XPATH, '//android.widget.TextView[@text="Take Photo"]'),
    "_CAMERA_PHOTO_": (MobileBy.ID, 'com.sec.android.app.camera:id/normal_center_button'),
    "_OK_": (MobileBy.ID, 'com.sec.android.app.camera:id/okay'),
    "_CANCEL_": (MobileBy.XPATH, '//android.widget.TextView[@text="Cancel"]'),
    "_REMOVE_PHOTO_": (MobileBy.XPATH, '//android.widget.TextView[@text="Remove Current Photo"]'),

}

legal_privacy = {
    "_DATA_DOWNLOAD_": (MobileBy.XPATH, '//android.widget.TextView[@text="Data download"]'),
    "_LICENSES_": (MobileBy.XPATH, '//android.widget.TextView[@text="Licenses"]'),
    "_PRIVACY_POLICY_": (MobileBy.XPATH, '//android.widget.TextView[@text="Privacy Policy"]'),
    "_TERMS_OF_USE_": (MobileBy.XPATH, '//android.widget.TextView[@text="Terms of Use"]'),
    "_LEGAL_PRIVACY_": (MobileBy.ID, 'com.sharecare.realgreen:id/webView'),
    "_RA_DOWNLOAD_": (MobileBy.XPATH, '(//android.view.View[@content-desc="Download"])[1]/android.widget.TextView[2]'),
    "_PROGRAMS_DATA_": (MobileBy.XPATH, '(//android.view.View[@content-desc="Download"])[2]/android.widget.TextView[2]'),
    "_TRACKER_DATA_": (MobileBy.XPATH, '//android.widget.Button[@text="Request"]'),
    "_TRACKER_DATA_REQUESTED_": (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                 '.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                                 '.ViewGroup/android.webkit.WebView/android.webkit.WebView/android'
                                                 '.view.View/android.view.View['
                                                 '1]/android.view.View/android.view.View[2]/android.view.View['
                                                 '4]/android.widget.Button')
}

communication = {
    "_RECEIVE_SMS_": (MobileBy.ID, 'com.sharecare.realgreen:id/sms_permission_switch'),
    "_SMS_MESSAGING_": (MobileBy.XPATH, '//android.widget.TextView[@text="SMS Messaging"]'),
    # Email subscriptions
    "_EMAIL_SUBSCRIPTIONS_": (MobileBy.XPATH, '//android.widget.TextView[@text="Email Subscriptions"]'),
    "_EMAIL_SUBSCRIPTIONS_WEBVIEW_": (MobileBy.ID, 'com.sharecare.realgreen:id/webView'),
    "_RECEIVE_EMAIL_NOTIFICATIONS_": (MobileBy.ID, 'input.subscriptions.emailGlobalOptOut.value'),
    "_ACTIVITY_DIGEST_": (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.CheckBox'),
    # "_ACTIVITY_DIGEST_": (MobileBy.ID, 'input.subscriptions.digests.teamDigests'),
    "_PROGRAM_UPDATES_": (MobileBy.ID, 'input.subscriptions.updates.emailWithProgramUpdates'),
    "_PRODUCT_UPDATES_": (MobileBy.ID, 'input.subscriptions.updates.emailWithProductUpdates'),
    "_PULSE_": (MobileBy.ID, 'input.subscriptions.newsletters.emailWithNewsletter'),
    # Health Tips
    "_HEALTH_TIPS_": (MobileBy.ID, 'input.subscriptions.newsletters.tips.value'),
    "_ONCE_A_WEEK_": (MobileBy.ID, 'input.subscriptions.newsletters.tips.frequency0'),
    "_TWICE_A_WEEK_": (MobileBy.ID, 'input.subscriptions.newsletters.tips.frequency1'),
    # Video Tips
    "_VIDEO_TIPS_": (MobileBy.ID, 'input.subscriptions.newsletters.emailWatchYourHealthVideoTips'),
    "_MY_CONDITIONS_": (MobileBy.ID, 'input.subscriptions.newsletters.emailWithConditionUpdates'),
    "_PERSONALIZED_EMAILS_": (MobileBy.ID, 'input.subscriptions.newsletters.emailPersonalizedRealAgeNewsletters'),
    "_NOTIFY_ME_WHEN_TRACKER_UPDATED_": (MobileBy.ID, 'input.subscriptions.notifyWhen.emailWhenTrackerUpdated'),
    "_NOTIFY_INSURANCE_REMINDERS_": (MobileBy.ID, 'input.subscriptions.notifyWhen.emailWhenInsuranceReminder'),
    "_SAVE_CHANGES_BTN_": (MobileBy.XPATH, '//android.widget.Button[@text="Save Changes"]'),
    # Push Notifications
    "_PUSH_NOTIFICATIONS_MENU_": (MobileBy.XPATH, '//android.widget.Button[@text="Push Notifications"]'),
    "_HEALTH_DATA_UPDATES_": (MobileBy.XPATH, 'android.widget.Switch[@text="Health Data Updates"]]'),
    "_REWARDS_": (MobileBy.XPATH, 'android.widget.Switch[@text="Rewards"]]'),
    "_INSIGHTS_": (MobileBy.XPATH, 'android.widget.Switch[@text="Insights"]]'),
    "_CHALLENGES_": (MobileBy.XPATH, 'android.widget.Switch[@text="Challenges"]]'),
    "_CHALLENGES_ENDING_": (MobileBy.XPATH, 'android.widget.Switch[@text="Challenge Ending"]]'),
    "_DAILY_REMINDER_": (MobileBy.XPATH, 'android.widget.Switch[@text="Daily Reminder"]]'),

}

home_screen = {
    # HOME_LOWER
    "_HOME_": (MobileBy.ID, 'com.sharecare.realgreen:id/navigation_home'),
    "_HOME_TRACKER_": (MobileBy.ID, 'com.sharecare.realgreen:id/navigation_track'),
    "_DISCOVER_": (MobileBy.ID, 'com.sharecare.realgreen:id/navigation_discover'),
    "_ACHIEVE_": (MobileBy.ID, 'com.sharecare.realgreen:id/navigation_achieve'),
    "_YOU_": (MobileBy.ID, 'com.sharecare.realgreen:id/navigation_you'),
    # HOME_TOP
    "_NOTIFICATION_ICON_": (MobileBy.ID, 'com.sharecare.realgreen:id/notificationCenterImageView'),
    "_SEARCH_ICON_": (MobileBy.ID, 'com.sharecare.realgreen:id/search'),
    "_HEART_": (MobileBy.ID, 'com.sharecare.realgreen:id/heart'),
    "_FILTER_": (MobileBy.ID, 'com.sharecare.realgreen:id/filter')
}

search = {
    "_SEARCH_FIELD_": (MobileBy.ID, 'com.sharecare.realgreen:id/input_field'),
    "_SEARCH_SUBTITLES_": (MobileBy.ID, 'com.sharecare.realgreen:id/exo_subtitles'),
    "_CONTENT_": (MobileBy.ID, 'com.sharecare.realgreen:id/exo_content_frame')
}

security_pin = {
    # Security PIN
    "_SECURITY_PIN_TOGGLE_": (MobileBy.ID, 'com.sharecare.realgreen:id/switch_security_pin'),
    "_PIN_CODE_TEXT_": (MobileBy.ID, 'com.sharecare.realgreen:id/pin_code_step_textview'),
    # AutoLock
    "_AUTO_LOCK_": (MobileBy.ID, 'com.sharecare.realgreen:id/timeout_container'),
    "_15_SECONDS_": (MobileBy.ID, 'com.sharecare.realgreen:id/fifteen_secondsrb'),
    "_30_SECONDS_": (MobileBy.ID, 'com.sharecare.realgreen:id/thiry_secondsrb'),
    "_1_MIN_": (MobileBy.ID, 'com.sharecare.realgreen:id/one_minuterb'),
    "_5_MIN_": (MobileBy.ID, 'com.sharecare.realgreen:id/five_minuterb'),
    "_10_MIN_": (MobileBy.ID, 'com.sharecare.realgreen:id/ten_minuterb'),
    #Change PIN
    "_CHANGE_PIN_": (MobileBy.ID, 'com.sharecare.realgreen:id/change_pin'),
    "_CANCEL_": (MobileBy.ID, 'com.sharecare.realgreen:id/textButton'),
    "_DELETE_KEY_": (MobileBy.ID, 'com.sharecare.realgreen:id/keyboard_button_imageview')
    
}

real_age_test = {

}

you_screen = {
    "_YOU_": (MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="You"]'),
    "_RAT_NOT_NOW_": (MobileBy.ID, 'com.sharecare.realgreen:id/take_later'),
    "_RAT_NOW_": (MobileBy.ID, 'com.sharecare.realgreen:id/take_now'),
    "_RAT_TITLE_": (MobileBy.ID, 'com.sharecare.realgreen:id/title'),
    "_RAT_ITEMS_": (MobileBy.ID, 'com.sharecare.realgreen:id/items'),
    "_UPDATE_RAT_": (MobileBy.ID, 'com.sharecare.realgreen:id/button')
}

settings_screen = {
    "_SETTINGS_": (MobileBy.ID, 'com.sharecare.realgreen:id/settings'),
    "_ACCOUNT_": (MobileBy.XPATH, '//android.widget.TextView[@text="Account"]'),
    "_APPEARANCE_": (MobileBy.XPATH, '//android.widget.TextView[@text="Appearance"]'),
    "_VIDEO_AUTOPLAY_": (MobileBy.XPATH, '//android.widget.TextView[@text="Video Autoplay"]'),
    "_SECURITY_PIN_": (MobileBy.XPATH, '//android.widget.TextView[@text="Security PIN"]'),
    "_COMMUNICATIONS_": (MobileBy.XPATH, '//android.widget.TextView[@text="Communications"]'),
    "_ABOUT_US_": (MobileBy.XPATH, '//android.widget.TextView[@text="About Us"]'),
    "_SUPPORT_": (MobileBy.XPATH, '//android.widget.TextView[@text="Support"]'),
    "_LEGAL_PRIVACY_": (MobileBy.XPATH, '//android.widget.TextView[@text="Legal & Privacy"]'),
    "_SIGN_OUT_": (MobileBy.XPATH, '//android.widget.TextView[@text="Sign Out"]'),
    "_LOGOUT_": (MobileBy.ID, 'android:id/button1'),
    '_LANGUAGE_': (MobileBy.XPATH, '//android.widget.TextView[@text="Languages"]')

}

welcome_screen = {
    "_WELCOME_GET_STARTED_": (MobileBy.ID, 'com.sharecare.realgreen:id/get_started'),
    "_NOT_NOW_": (MobileBy.ID, 'com.sharecare.realgreen:id/take_later'),
    "_GET_STARTED_BR_": (MobileBy.ID, 'com.sharecare.realgreen:id/fill_out'),
    "_MORE_INFO_REQUIRED_BR_": (MobileBy.ID, 'com.sharecare.realgreen:id/textView2'),
    "_SIGN_OUT_BR_": (MobileBy.ID, 'com.sharecare.realgreen:id/sign_out')
}

forgot_password = {
    "_SEND_": (MobileBy.ID, 'com.sharecare.realgreen:id/actionButton'),
    "_EMAIL_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_email_address'),
    "_FORGOT_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/forgot_text_view')
}

login_onboarding_screen = {
    "_SEARCH_": (MobileBy.ACCESSIBILITY_ID, 'Search'),
    "_EMAIL_": (MobileBy.XPATH, '//android.widget.EditText[@text="Email"]'),
    "_PASSWORD_": (MobileBy.XPATH, '//android.widget.EditText[@text="Password"]'),

    ###IOS

    "_EMAIL_IOS_": (MobileBy.XPATH, '//XCUIElementTypeTextField[@name="emailTextField"]'),
    "_PASSWORD_IOS_": (MobileBy.ID, 'passwordTextField'),



    "_CONTINUE_": (MobileBy.ID, 'com.sharecare.realgreen:id/confirmButton'),
    "_ONBOARDING_COUNTRY_SELECTION_OK_": (MobileBy.ID, 'android:id/button1'),
    "_ONBOARDING_FIRST_NAME_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_first_name'),
    "_ONBOARDING_LAST_NAME_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_last_name'),
    "_ONBOARDING_EMAIL_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_email_address'),
    "_ONBOARDING_BIRTH_DATE_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_birth_date'),
    "_ONBOARDING_YEAR_": (MobileBy.ID, 'com.sharecare.realgreen:id/mdtp_date_picker_year'),
    "_ONBOARDING_NEXT_MONTH_": (MobileBy.ID, 'com.sharecare.realgreen:id/mdtp_next_month_arrow'),
    "_ONBOARDING_BIRTH_DATE_OK_": (MobileBy.ID, 'com.sharecare.realgreen:id/mdtp_ok'),
    "_ONBOARDING_YEAR_PICKER_": (MobileBy.ID, 'com.sharecare.realgreen:id/mdtp_month_text_view'),

    # ToDo - Add list support.
    "_ONBOARDING_GENDER_": (MobileBy.ID, 'com.sharecare.realgreen:id/gender_dropdown'),

    "_ONBOARDING_GENDER_MALE_": (MobileBy.ID, 'com.sharecare.realgreen:id/radio_male'),
    "_ONBOARDING_GENDER_FEMALE_": (MobileBy.ID, 'com.sharecare.realgreen:id/radio_female'),

    "_ZIPCODE_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_zip_code'),
    "_ONBOARDING_NEW_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_password'),
    "_ONBOARDING_CONFIRM_NEW_PASSWORD_": (MobileBy.ID, 'com.sharecare.realgreen:id/edit_text_confirm_password'),
    "_ONBOARDING_TERMS_CONDITIONS_": (MobileBy.ID, 'com.sharecare.realgreen:id/accept_term_and_conditions'),
    "_PRIVACY_TERMS_CONDITIONS_": (MobileBy.ID, 'com.sharecare.realgreen:id/terms_and_conditions_text'),
    "_ONBOARDING_CREATE_": (MobileBy.ID, 'com.sharecare.realgreen:id/actionButton'),
    "_ONBOARDING_COUNTRY_SELECTION_": (MobileBy.XPATH, '//android.widget.TextView[@text="Country"]'),
    "_ONBOARDING_COUNTRY_": (MobileBy.XPATH, '//android.widget.RadioButton[@text="Germany"]'),
    "_ONBOARDING_SEARCH_": (MobileBy.ID, 'com.sharecare.realgreen:id/menu_item_search'),
    "_SEARCH_FIELD_": (MobileBy.ID, 'com.sharecare.realgreen:id/input_field'),
    "_ONBOARDING_SEARCH_COUNTRY_RESULT_": (MobileBy.ID, 'com.sharecare.realgreen:id/countryName'),
    "_ONBOARDING_COUNTRY_CONFIRM_": (MobileBy.ID, 'com.sharecare.realgreen:id/confirmButton'),
    "_INVALID_CREDENTIALS_ERROR_": (MobileBy.ID, 'com.sharecare.realgreen:id/title_template'),
    "_CLOSE_": (MobileBy.ID, 'android:id/button2'),
    "_COUNTRY_NAME_": (MobileBy.ID, 'com.sharecare.realgreen:id/countryName'),
    "_COUNTRY_SEARCH_": (MobileBy.ID, 'com.sharecare.realgreen:id/menu_item_search'),
    "_BR_CONFIRM_": (MobileBy.ID, 'com.sharecare.realgreen:id/fill_out'),
    "_CPF_INPUT_": (MobileBy.ID, 'com.sharecare.realgreen:id/text_input_edit_text'),
    "_CPF_CONFIRM_": (MobileBy.ID, 'com.sharecare.realgreen:id/actionButton'),

    # ToDo Checking on this
    "_8 character minimum_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[1]',
    "_1 upper case character_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[2]',
    "_1 lower case character_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[3]',
    "_1 number or special character_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[4]'

}

missing_field_screens = {
    "_MISSING_FIELD_INFO_TEXT_": (MobileBy.ID, 'com.sharecare.realgreen:id/textView2'),
    "_MISSING_CONTINUE_": (MobileBy.ID, 'com.sharecare.realgreen:id/fill_out'),
    "_MISSING_GENDER_DROPBOX_": (MobileBy.ID, 'com.sharecare.realgreen:id/text_input_end_icon'),
    "_MISSING_NEXT_": (MobileBy.ID, 'com.sharecare.realgreen:id/actionButton'),
    "_MISSING_GENDER_DOB_": (MobileBy.ID, 'com.sharecare.realgreen:id/dateEditText'),

}

android_keyswords = {
    # MARKET
    "_SHARECARELOGO_": 'com.sharecare.realgreen:id/debug_subtitle',
    "_SELECT_MARKET_": 'com.sharecare.realgreen:id/selectMarket',
    "_SELECT_ENVIRONMENT_": 'com.sharecare.realgreen:id/selectEnvironment',

    # ONBOARDING
    "_EMAIL_": 'com.sharecare.realgreen:id/text_input_edit_text_email',
    "_PASSWORD_": 'com.sharecare.realgreen:id/text_input_edit_text_password',

    "_CONTINUE_": 'com.sharecare.realgreen:id/confirmButton',
    "_ONBOARDING_COUNTRY_SELECTION_OK_": 'android:id/button1',
    "_ONBOARDING_FIRSTNAME_": 'com.sharecare.realgreen:id/edit_text_first_name',
    "_ONBOARDING_LASTNAME_": 'com.sharecare.realgreen:id/edit_text_last_name',
    "_ONBOARDING_EMAIL_": 'com.sharecare.realgreen:id/edit_text_email_address',
    "_ONBOARDING_BIRTHDATE_": 'com.sharecare.realgreen:id/edit_text_birth_date',
    "_ONBOARDING_YEAR_": 'com.sharecare.realgreen:id/mdtp_date_picker_year',
    "_ONBOARDING_NEXT_MONTH_": 'com.sharecare.realgreen:id/mdtp_next_month_arrow',
    "_ONBOARDING_BIRTHDATE_OK_": 'com.sharecare.realgreen:id/mdtp_ok',
    "_ONBOARDING_YEAR_PICKER_": 'com.sharecare.realgreen:id/mdtp_month_text_view',
    "_ONBOARDING_GENDER_MALE_": 'com.sharecare.realgreen:id/radio_male',
    "_ONBOARDING_GENDER_FEMALE_": 'com.sharecare.realgreen:id/radio_female',
    "_ZIPCODE_": 'com.sharecare.realgreen:id/edit_text_zip_code',
    "_ONBOARDING_NEWPASSWORD_": 'com.sharecare.realgreen:id/edit_text_password',
    "_ONBOARDING_CONFIRMNEWPASSWORD_": 'com.sharecare.realgreen:id/edit_text_confirm_password',
    "_ONBOARDING_TERMSCONDITIONS_": 'com.sharecare.realgreen:id/accept_term_and_conditions',
    "_ONBOARDING_CREATE_": 'com.sharecare.realgreen:id/actionButton',
    "_RAT_NOT_NOW_": 'com.sharecare.realgreen:id/take_later',
    "_RAT_NOW_": 'com.sharecare.realgreen:id/take_now',
    "_ONBOARDING_COUNTRY_SELECTION_": '//android.widget.TextView[@text="Country"]',
    "_ONBOARDING_COUNTRY_": '//android.widget.RadioButton[@text="Germany"]',
    "_ONBOARDING_SEARCH_": 'com.sharecare.realgreen:id/menu_item_search',
    "_SEARCH_FIELD_": 'com.sharecare.realgreen:id/input_field',
    "_ONBOARDING_SEARCH_COUNTRY_RESULT_": 'com.sharecare.realgreen:id/countryName',
    "_ONBOARDING_COUNTRY_CONFIRM_": 'com.sharecare.realgreen:id/confirmButton',
    "_INVALID_CREDENTIALS_ERROR_": 'com.sharecare.realgreen:id/title_template',
    "_CLOSE_": 'android:id/button2',
    "_COUNTRY_NAME_": 'com.sharecare.realgreen:id/countryName',
    "_COUNTRY_SEARCH_": 'com.sharecare.realgreen:id/menu_item_search',
    "_BR_CONFIRM_": 'com.sharecare.realgreen:id/fill_out',
    "_CPF_INPUT_": 'com.sharecare.realgreen:id/text_input_edit_text',
    "_CPF_CONFIRM_": 'com.sharecare.realgreen:id/actionButton',
    "_8 character minimum_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[1]',
    "_1 upper case character_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[2]',
    "_1 lower case character_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[3]',
    "_1 number or special character_": '(//*[@resource-id = "com.sharecare.realgreen:id/icon"])[4]',

    # HOME
    "HOME": '//android.widget.FrameLayout[@content-desc="Home"]/android.widget.ImageView',
    "_HOME_TRACKER_": '//android.widget.FrameLayout[@content-desc="Track"]/android.widget.ImageView',

    # FEED
    "_HERO_VIDEO_": 'com.sharecare.realgreen:id/exo_subtitles',
    "_TAKE_RAT_": 'com.sharecare.realgreen:id/takeRealAge',
    "_GDT_STACK_": '//android.widget.TextView[@text="Earn your first Green Day"]',
    # com.sharecare.realgreen:id/swipeContainer
    "_CARD_": 'com.sharecare.realgreen:id/card',

    # YOU
    "_YOU_": '//android.widget.FrameLayout[@content-desc="You"]',
    "_YOU_SETTING_": 'com.sharecare.realgreen:id/settings',
    "_YOU_SIGN_OUT_": '//android.widget.TextView[@text="Sign Out"]',
    "_YOU_LOGOUT_": 'android:id/button1',
    "_YOU_TAKE_IT_LATER_": '//android.widget.Button[@text="Take It Later"]',
    "_YOU_TAKE_RAT_": '//android.widget.Button[@text="Take the RealAge Test"]',

    # TRACKER
    "_TRACKER_GET_STARTED_": 'com.sharecare.realgreen:id/button_get_started',
    "_TRACKER_ALCOHOL_": '//android.widget.TextView[@text="Alcohol"]',
    "_TRACKER_BLOOD_GLUCOSE_": '//android.widget.TextView[@text="Blood Glucose"]',
    "_TRACKER_BLOOD_PRESSURE_": '//android.widget.TextView[@text="Blood Pressure"]',
    "_TRACKER_CHOLESTEROL_": '//android.widget.TextView[@text="Cholesterol"]',
    "_TRACKER_DIET_": '//android.widget.TextView[@text="Diet"]',
    "_TRACKER_FITNESS_": '//android.widget.TextView[@text="Fitness"]',
    "_TRACKER_MEDICATION_": '//android.widget.TextView[@text="Medication"]',
    "_TRACKER_RELATIONSHIP_": '//android.widget.TextView[@text="Relationship"]',
    "_TRACKER_SLEEP_": '//android.widget.TextView[@text="Sleep"]',
    "_TRACKER_SMOKE_": '//android.widget.TextView[@text="Smoke"]',
    "_TRACKER_STRESS_": '//android.widget.TextView[@text="Stress"]',
    "_TRACKER_WEIGHT_": '//android.widget.TextView[@text="Weight"]',
    "_TRACKER_SAVE_BUTTON_": 'com.sharecare.realgreen:id/textButton',
    "_TRACKER_INPUT_FIELD_": 'com.sharecare.realgreen:id/text_input_field',
    "_TRACKER_EDIT_": 'com.sharecare.realgreen:id/text_view_action',
    "_SYSTOLIC_": '(//android.widget.EditText)[1]',
    "_DIASTOLIC_": '(//android.widget.EditText)[2]',
    "_NOT_DIABETIC_": 'com.sharecare.realgreen:id/radio_button_negative',
    "_DIABETIC_": 'com.sharecare.realgreen:id/radio_button_positive',
    "_SEEK_BAR_": 'com.sharecare.realgreen:id/seek_bar',
    "_TRACKER_BACK_": '(//android.widget.ImageButton)[1]',

    # ALCOHOL
    "_ALCOHOL_NONDRINKER_": 'com.sharecare.realgreen:id/radio_button_negative',
    "_ALCOHOL_CONSUMER_": 'com.sharecare.realgreen:id/radio_button_positive',
    "_STATUS_SAVE_": 'com.sharecare.realgreen:id/menu_item_save',
    "_EXPOSED_DROPDOWN_": 'com.sharecare.realgreen:id/filled_exposed_dropdown',
    "_ALCOHOL_DRINK_SAVE_": 'com.sharecare.realgreen:id/textButton',
    "_ALCOHOL_KEY_1_": '//android.widget.Spinner[@text="1"]',
    "_ALCOHOL_DROPDOWN_MENU_": 'com.sharecare.realgreen:id/text_input_end_icon',

    # Smoke
    "_NON_SMOKER_": 'com.sharecare.realgreen:id/radio_button_negative',
    "_SMOKER_": 'com.sharecare.realgreen:id/radio_button_positive',

    # Weight
    "_HEIGHT_FEET_": 'com.sharecare.realgreen:id/label_feet',
    "_FEET_": 'com.sharecare.realgreen:id/row_spn_tv',
    "_HEIGHT_INCH_": 'com.sharecare.realgreen:id/label_inch',

    # Sleep
    "_BED_TIME_": '//android.widget.TextView[@text="Bed time"]',
    "_RISE_TIME_": '//android.widget.TextView[@text="Rise time"]',
    "_TIME_OK_": 'com.sharecare.realgreen:id/mdtp_ok',
    "_SLEEP_RATING_": 'com.sharecare.realgreen:id/rating_bar',
    "_RECORD_DELETED_": '//android.widget.TextView[@text="It’s a bit empty here…"]',

    # FEED
    "_WELCOME_CARD": '',

}
