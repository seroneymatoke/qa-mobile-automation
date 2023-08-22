# Created by seroneymatoke at 14.12.21
@sanity @common @forgot_password @sanity-cf
Feature: A user should be able to reset a forgot password

  @testrail-C44711 @testrail-C13896
  Scenario: A user should be able to reset a password using a valid email
    #Given user waits for "2" seconds
    Given user taps "Sign In"
    And user taps "Forgot Password?"
    # Todo - Consider parameterization
    And user sets "Email" to "seroney.us@ftqa.com"
    And user taps "Send"
    Then user should see "A link to reset your password will be sent to your email address."