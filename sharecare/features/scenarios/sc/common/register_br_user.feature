# Created by seroneymatoke at 11.11.21
# PS: This is run separately as it requires a market change .... @Todo
@sanity @sl @common @brazil @registration @talk @smoke-android @XC @sanity-sc
Feature: User registration
  A User should be able to register self in BR production / STG

    @testrail-C44702 @testrail-C44705 @testrail-C3383 @testrail-C43862
  Scenario: A user should be able register successfully
    Given user taps "Create Account"
    And user taps "Country"
    And user taps "Search"
    And user sets "Search" to "Brazil"
    And user taps "Brazil"
    And user taps "countryName"
    And user taps "Continue"
    # Validates screen loads successfully
    # And user validates page elements
    And "valid_br_user" user enters first name
    And "valid_br_user" user enters last name
    And "valid_br_user" user enters email address
    And user enters birth date
    And user selects gender
    And "valid_br_user" user enters Zip Code
    And "valid_br_user" user enters new password
    And "valid_br_user" user enters matching new password
    And "valid_br_user" user clicks agree to Sharecare's Terms and conditions
    And user taps "Create"
    Then user should see "Skip"

    # behave -v sharecare/features/scenarios/common/register_br_user.feature
