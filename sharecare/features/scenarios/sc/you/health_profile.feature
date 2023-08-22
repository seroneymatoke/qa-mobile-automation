# Created by seroneymatoke at 07.04.22
@health-profile @sanity @you @sanity-sc
Feature: Test for Health Profile

  @testrail-C175474
  Scenario: User logs in
    Given user logs in
    Given user taps "Skip"


  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

  @testrail-C44779 @testrail-C4405
  Scenario: User navigates to Health Profile
    Given user taps "You"
    And user taps "Take It Later"
    And user taps "Health Profile"
    Then user should see "What is your Health Profile?"
    Given user taps "Got it!"

  @testrail-C44787 @testrail-C30839
  Scenario: Health Profile - Initials are shown (or default image) if there is no avatar set
    # currently test use a default username test test hence should see TT as avatar
    Then user should see "TT"

  @testrail-C44779 @testrail-C4405 @testrail-C4409 @testrail-C4408 @testrail-C4410 @testrail-C4406
  Scenario Outline: It is possible to open every available health indicator
    Given user taps "<item>"
    Given user waits for "1" seconds
    Then user should see "<results>"
    Given user waits for "1" seconds
    Given user goes back "1" times
    Given user activates app
    Given user taps "You"
    And user taps "Health Profile"

    # Add as pleased
    Examples:
      | item        | results     |
      | Care Team   | Care Team   |
      | Medications | Medications |
      | Allergies   | Allergies   |

  @testrail-C44788 @testrail-C44789 @testrail-C30840
  Scenario: Change Profile Photo Take Photo
    Given user taps "Change Profile Photo"
    Then user should see "Choose From Library"
    Given user taps "Choose From Library"
    # Then user should see "Gallery"
    # Then user should see "Photos"
    Given user goes back "1" times

  @testrail-C44790 @testrail-C30841 @testrail-C30845
  Scenario: Change Profile photo remove
    Given user taps "Change Profile Photo"
    And user taps "Take a Photo"

  #FLakiness
  Scenario: Location Popup
    Given user taps "Cancel"

  @testrail-C44790 @testrail-C30841 @testrail-C30845
  Scenario: Change Profile photo remove
    Given user taps "Take picture"
    And user taps "OK"
    And user waits for "10" seconds
    And user taps "Change Profile Photo"
    Then user should see "Remove Current Photo"
    Given user taps "Remove Current Photo"
    Then user should see "TT"

