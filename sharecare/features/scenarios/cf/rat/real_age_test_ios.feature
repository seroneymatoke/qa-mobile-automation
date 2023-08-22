# Created by seroneymatoke at 11.03.22
  @rat-sc-ios @sanity @sanity-sc
Feature: Real Age Tests

#  Scenario: Registration
#    Given user clicks create account
#    And "valid_us_user" user selects country
#    And user clicks continue
#    # Validates screen loads successfully
#    # And user validates page elements
#    And "valid_us_user" user enters first name
#    And "valid_us_user" user enters last name
#    And "valid_us_user" user enters email address
#    And user enters birth date
#    And user selects gender
#    And "valid_us_user" user enters Zip Code
#    And "valid_us_user" user enters new password
#    And "valid_us_user" user enters matching new password
#    And "valid_us_user" user clicks agree to Sharecare's Terms and conditions
#    When user clicks create account

  Scenario: User logs in
    Given user logs in
    And user waits for "2" seconds

  Scenario: Skip Phone Setup
    Given  user taps "Skip"

    @slow #-Takes quite a bit to show up on iOS
#  Scenario: Skip tool tips
#    Given user waits for "2" seconds
#    Given  user taps "Skip"

  @testrail-C4393
  Scenario: It is possible to start a RealAge Test with a newly registered user

    Given user taps "Take the RealAge Test"
    Given user waits for "20" seconds
    # Camera disabled if using Simulator
#    And user taps "Take a Selfie"
#    And user taps "Take Picture"
#    And user taps "Looks Good"
    And user taps "Skip"
    And user taps "Male"
    And user taps "Next"
    And user taps "Next"
    And user taps "Next"
#
#    # Android -
#    And user taps "Show dropdown menu"
#    And user waits for "2" seconds
#    And user taps coordinates "560" and "2020"
#    And user taps "Next"
#    And user taps "Next"
#
#
#  @testrail-C4394 @testrail-C4398
#  Scenario: RealAge Test can be paused at any point of the survey
#    Given user taps "Pause"
#    Then user should see "Are you sure you want to pause?"
#    Given user taps "Yes"
#    And user waits for "5" seconds
#    Then user should see "Complete the RealAge Test"
#
#
#  # Go To You check status
#  @testrail-C4397
#  Scenario: State of RealAge Test (not started/started/completed) is reflected in the header on You screen
#    Given user taps "You"
#    Then user should see "Complete the RealAge Test"
#
#  @testrail-C4396
#  Scenario: Paused RealAge Test continues from where it was left off
#    Given user taps "Complete the RealAge Test"
#    Then user should see "2%"
#    Then user should see "Pause"
#
#  @testrail-C4395
#  Scenario: Once completed, the RealAge Test can be done again any time
#    #HS
#    Given user taps "Good"
#    And user taps "Next"
#    #BP
#    And user taps "No"
#    And user taps "Next"
#    #BP Estimate
#    And user taps "Average"
#    And user taps "Next"
#    #Cholestrol
#    And user taps "No"
#    And user taps "Next"
#    #Chol Estimate
#    And user taps "Average"
#    And user taps "Next"
#    #Good Chol
#    And user taps "No"
#    And user taps "Next"
#    #Good Chol Estimate
#    And user taps "Average"
#    And user taps "Next"
#    # Physical Health
#    And user taps "4"
#    And user taps "Next"
#    # Struggling doing agemate stuff
#    And user taps "No"
#    And user taps "Next"
#    # Asthma stuff
#    And user taps "No"
#    And user taps "Next"
#    # Diabetes stuff
#    And user taps "No"
#    And user taps "Next"
#    # Vape stuff
#    And user taps "No"
#    And user taps "Next"
#    # Secondhand Smoke
#    And user taps "Next"
#    # Drinking habits
#    And user taps "Next"
#    # Gender Id
#    And user taps "Next"
#    # Diag Conditions
#    And user taps "Next"
#    # Cancers Conditions
#    And user taps "Next"
#    # Surgeries
#    And user taps "Next"
#    # Counselling Depression
#    And user taps "Next"
#    # Chronic Pain
#    And user taps "Next"
#    # Dentist Visit
#    And user taps "Next"
#    # Flu Vaxx
#    And user taps "Next"
#    # Pneumonia Vaxx
#    And user taps "Next"
#    # Mood medication
#    And user taps "Next"
#    # Continuous medication
#    And user taps "Next"
#    # Any medication
#    And user taps "Next"
#    # Any medication appointments
#    And user taps "Next"
#    # Halfway Done
#    And user taps "Next"
#    # General Health
#    And user taps "Next"
#    # Marital Status
#    And user taps "Never married"
#    And user taps "Next"
#    # Living arrangement
#    And user taps "Next"
#    # Living arrangement hse people #
#    And user taps "Next"
#    # No of children < 18
#    And user taps "Next"
#    # Employment Status
#    And user taps "Next"
#    # Ed status
#    And user taps "Next"
#    # Family income
#    And user taps "Next"
#    # Sleep Cycle
#    And user taps "Next"
#    # Emotional Pain
#    And user taps "None"
#    And user taps "Next"
#    # Financial Stress
#    And user taps "Little or none"
#    And user taps "Next"
#    # Home/Work Stress
#    And user taps "Next"
#    # Group Activities
#    And user taps "Often"
#    And user taps "Next"
#    # Roundness check
#    And user taps "Next"
#    # Recognition check
#    And user taps "Next"
#    # Finances check
#    And user taps "Next"
#    # Statisfaction check
#    And user taps "Next"
#    # Social Wellness check
#    And user taps "Next"
#    # Problems check
#    And user taps "Next"
#    # Exercise check
#    And user taps "Next"
#    # Speed Walk check
#    And user taps "Slow (conversation is effortless)"
#    And user taps "Next"
#
#    # Speed DropDown
#    And user taps "times per week"
#    And user taps coordinates "560" and "2020"
#    And user taps "min(s) per time"
#    And user taps coordinates "560" and "800"
#    And user taps "Next"
#
#    # Aerobic
#    And user scrolls "1" times direction "down"
#    And user taps "I don't do aerobic exercise"
#    And user taps "Next"
#
#    # Strength Training
#    And user taps "None"
#    And user taps "Next"
#
#    # Sitting
#    And user taps "Almost no time"
#    And user taps "Next"
#
#    # servings per day
#    And user taps "0"
#    And user scrolls "1" times direction "down"
#    And user taps "2"
#    And user scrolls "2" times direction "down"
#    And user taps "0"
#    And user taps "Next"
#
#    # servings per day
#    And user taps "0"
#    And user scrolls "1" times direction "down"
#    And user taps "0"
#    And user scrolls "2" times direction "down"
#    And user taps "0"
#    And user taps "Next"
#
#    #Legumes
#    And user taps "none"
#    And user taps "Next"
#    #Soy
#    And user taps "none"
#    And user taps "Next"
#    #Sugar
#    And user taps "1 drink per day"
#    And user taps "Next"
#    #Chips
#    And user taps "0"
#    And user taps "Next"
#    #Nuts
#    And user taps "None"
#    And user taps "Next"
#    #Vegan?
#    And user taps "No"
#    And user taps "Next"
#    #Meat?
#    And user taps "Next"
#    #Fish?
#    And user taps "Next"
#    # Trips
#    And user taps "Show dropdown menu"
#    And user taps coordinates "560" and "2000"
#    And user taps "Next"
#
#    #Airbags
#    And user taps "Next"
#
#    #Changes
#    And user taps "Next"
#
#
#    #Languages
#    And user taps "Next"
#
#
#    #Race
#    And user taps "Next"
#
#    # Finished
#    And user taps "Next"
#
#    Then user should see "RealAge Score"
#    Then user should see "Done"
#
#
#  @testrail-C4399
#  Scenario: RealAge Tips are shown based on the state and results of RealAge Test
#    Given user taps "You"
#    And user taps "Your RealAge"
#    And user taps "Tips"
#    Then user should see "What's affecting your RealAge?"
#
#  #Logout User for ioS
#  #@To-Refactor user termination
#  Scenario: Kill Session
#    Given user taps "You"
#    And user taps "Take it Later"





