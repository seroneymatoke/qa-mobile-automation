# Created by seroneymatoke at 13.06.22
  @blocked-ios @sanity @xsas @testrail-C13895 @xx @sanity-sc-ios @slow @common
Feature: After 5 attempts to login with an invalid password the app present the account lock
  @testrail-C13895 @sanity-ios
  Scenario: User taps login
    Given blocking user logs in

  Scenario: User taps close
    #Given user taps "OK"
  

  Scenario Outline: A user enters incorrect password 5 times
    Given user sets "Password" to "<password>"
    And user taps "Sign In"
    #And user taps "OK"
    Examples: 
    |password|
    |QWWWEEETY|
    |QWWWEEETY|
    |QWWWEEETY|

    
  Scenario: Check for blocked screen
    Given user sets "Password" to "QWEEEE41255"
    And user taps "Sign In"

    # For UAT need to check if password is enabled
    Then user should see "OK"
    # Then user should see "Reset password"
    
    