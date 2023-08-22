# Created by seroneymatoke at 21.12.21
@sanity-cf @account

  # To be run locally since requires active access to the camera.
  # https://docs.saucelabs.com/mobile-apps/features/camera-image-injection/

Feature: A user should be able to edit account details

  # https://sharecare.testrail.io/index.php?/cases/view/4417
  Scenario: User logs in
    Given user logs in

  Scenario: Skip Step
   Given user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

  @testrail-C44795 @testrail-C44796 @testrail-C4417 @testrail-C4418
  Scenario: The fields are populated with data provided by the user
    Given user taps "You"
    And user taps "Take It Later"

    # Todo - Changed from Setting to Button
    # And user taps "Settings"
    And user taps " Button"
    And user taps "Account"
    # Then user validates page information

  @testrail-C44800 @testrail-C30842
  Scenario: Change Profile Photo Take Photo
    Given user taps "Change Profile Photo"
    Then user should see "Choose From Library"
    Given user taps "Take a Photo"
    # Location Tags
    And user taps "Cancel"
    And user taps "Take picture"
    And user taps "OK"
    And user waits for "10" seconds

  @testrail-C44801 @testrail-C44802 @testrail-C30843 @testrail-C30844
  Scenario: Change Profile photo remove
    Given user taps "Change Profile Photo"
    Then user should see "Remove Current Photo"
    Given user taps "Remove Current Photo"
    Then user should see "TT"
    # Given user taps coordinates "200" and "500"

    @testrail-C44797 @testrail-C4419 @testrail-C13898 @testrail-C13897
  Scenario: It is possible to change the password
    Given user scrolls "3" times direction "down"
    And user taps "Change Password"
    And user sets "Current Password" to "Qweasdzxc1!"
    And user taps "Continue"
    And user sets "New Password" to "@@Com/12/07@@"
    And user sets "Confirm New Password" to "@@Com/12/07@@"
    And user taps "Update Password"
    Then user should see "Your password has been updated."






