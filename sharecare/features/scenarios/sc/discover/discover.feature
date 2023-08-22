# Created by seroneymatoke at 26.01.22
@sanity @discover @talk @main @sanity-sc @discover-check
Feature: Discover open web views

#  Scenario: Registration
#    Given user clicks create account
#    And "valid_us_user" user selects country
#    And user clicks continue223.2
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
#    Then "valid_us_user" user should be able to see the welcome screen

    @login-dis
  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"
@testrail-C44840 @testrail-C44706 @testrail-C44839 @testrail-C30847 @testrail-C30848
 Scenario: User should be on discover
   Given user taps "Discover"
   Then user should see "Your Physical Traits"
   Then user should see "Your Health"

  # For Production This might not be available - Covid Care Center WV
  @testrail-C44840 @testrail-C44706 @testrail-C44839 @testrail-C30847 @testrail-C30848
  Scenario: Covid Care Center being opens a WebView
    Given user scrolls "4" times direction "down"
    And user taps "COVID-19 Care Center"
    Then user should see "COVID-19 Care Center"

    @testrail-C44841 @testrail-C4378
  Scenario: Inspiration opens in a WebView
    Given user goes back "1" times
    And user scrolls "2" times direction "down"
    Given user taps "Inspirations"
    Then user should see "Inspirations"

     @testrail-C44842 @testrail-C4377 @testrail-C4407 @testrail-C4408 @testrail-C4409 @testrail-C4407
  Scenario: Medication Prices opens in a WebView
    Given user goes back "1" times
    And user scrolls "2" times direction "down"
    Given user taps "Medication Prices"
    Then user should see "Medication Prices"
