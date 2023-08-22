# Created by seroneymatoke at 14.12.21
@sanity @common @forgot_password_ios @sanity-sc-ios
Feature: A user should be able to reset a forgot password

  @testrail-C44711 @testrail-C13896
  Scenario: A user should be able to reset a password using a valid email
    #Given user waits for "2" seconds
    Given user taps "Sign In"
    Given user sets "Email" to "seroney.us@ftqa.com"

  Scenario: User taps Forgot Password
    Given user taps "Forgot Password?"
    # Todo - Consider parameterization

  Scenario: Flaky Test
    Given user sets "Email" to "seroney.us@ftqa.com"
    And user waits for "5" seconds
    And user taps "Send"
    Then user should see "A link to reset your password will be sent to your email address."