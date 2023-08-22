# Created by seroneymatoke at 02.11.21
@sanity @login @sanity @common @smoke-android @gk @login-ios @sanity-sc @test_uat @logout
Feature: Login with Valid Credentials for all markets
  User should be able to login to appropriate market with valid credentials

  # https://sharecare.testrail.io/index.php?/cases/view/3366&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=734

  @testrail-C44706 @login @slow @testrail-C3366 @testrail-C13892 @testrail-C13894 @set @testrail-C175474 @android @ios @testrail-C175472 @testrail-C175473
  Scenario: Login user
    Given user logs in
    And user taps "Skip"
    # Then the user should be able to see the home screen

  @testrail-C44703 @testrail-C32687 @testrail-C43873 @set @android @ios
  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

    @testrail-C44713 @testrail-C3367 @testrail-C43863 @set @android @ios
  Scenario: Newly registered user gets a welcome package injected in the Feed
    Given user scrolls "1" times direction "down"
    Then user should see "Welcome to Sharecare"


    # continuation from previous scenario
  @testrail-C44707 @login_logout @testrail-C3385 @lg @android @ios
  Scenario: Logout user
    Given user taps "You"
    And user taps "Take It Later"

    @android @testrail-C44707 @login_logout @testrail-C3385
  Scenario: User taps Settings
    Given user taps " Button"

  @ios @testrail-C44707 @login_logout @testrail-C3385
  Scenario: User clicks You Settings button
#    Given user taps "You"

  @login_logout @testrail-C3385
  Scenario: Logout
    Given user taps "Sign Out"
    And user taps "Logout"
    Then user should see "You are not logged in."

   # behave -v sharecare/features/scenarios/common/valid_login.feature



