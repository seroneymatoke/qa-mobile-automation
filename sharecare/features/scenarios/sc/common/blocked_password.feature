# Created by seroneymatoke at 13.06.22
  @blocked @sanity @xsas @testrail-C13895 @xx @sanity-sc @slow @common
Feature: After 5 attempts to login with an invalid password the app present the account lock
  @testrail-C13895 @sanity-ios
  Scenario: User taps login
    Given blocking user logs in

    @android
  Scenario: User taps close
    Given user taps "Close"
  

  Scenario Outline: A user enters incorrect password 5 times
    Given user sets "Password" to "<password>"
    And user taps "Sign In"
    And user taps "Close"
    Examples: 
    |password|
    |QWWWEEETY|
    |QWWWEEETY|
    |QWWWEEETY|

    
  Scenario: Check for blocked screen
    Given user sets "Password" to "QWEEEE41255"
    And user taps "Sign In"
    Then user should see "Reset password"
    
    