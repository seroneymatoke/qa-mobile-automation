# Created by seroneymatoke at 05.11.21

  # https://sharecare.testrail.io/index.php?/cases/view/3365&group_by=cases:section_id&group_order=asc&group_id=734
  # https://sharecare.testrail.io/index.php?/cases/view/32687&group_by=cases:section_id&group_id=734&group_order=asc&display_deleted_cases=0
@sanity @demo @sl @common @registration @talk @regus @smoke-android @ios @sanity-sc
Feature: User registration
  A User should be able to register self in US production and user should see tooltips

   @testrail-C44701 @testrail-C3365 @testrail-C43861
  Scenario: A user should be able register successfully
#    Given user taps "Create Account"
#    And user taps "Country"
#    #And user taps "Search"
#    And user sets "Search" to "United States of America"
#    And user taps "United States of America"
#    #And user taps "countryName"
#    And user taps "Continue"
##    And user sets "First Name" to "valid_us_user"
##    And user waits for "20" seconds


    Given user clicks create account
    And "valid_us_user" user selects country
    And user clicks continue
    # Validates screen loads successfully
    # And user validates page elements
   And "valid_us_user" user enters first name
    And "valid_us_user" user enters last name
    And "valid_us_user" user enters email address
    And user enters birth date
    And user selects gender
    And "valid_us_user" user enters Zip Code
    And "valid_us_user" user enters new password
    And "valid_us_user" user enters matching new password
    And "valid_us_user" user clicks agree to Sharecare's Terms and conditions
    When user clicks create account
    #Then "valid_us_user" user should be able to see the welcome screen

    @testrail-C44712 @testrail-C41602 @testrail-C3384
  Scenario: Getting Started
    Given user taps "Skip"
    Given user taps "Get Started"
    Then user should see "Take a Selfie"


    # behave -v --tags=brazil sharecare/features/scenarios/common/register_br_user.feature
    # us behave -v --tags=us sharecare/features/scenarios/common/register_us_user.feature
    # behave -v sharecare/features/scenarios/common/register_user.feature

