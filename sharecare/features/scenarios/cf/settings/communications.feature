# Created by seroneymatoke at 02.12.21
@sanity @testrail-C44804 @comms @settings @sanity-sc
Feature: User can setup communications

    # https://sharecare.testrail.io/index.php?/cases/view/4421&group_by=cases:section_id&group_id=1024&group_order=asc&display_deleted_cases=0

#  Scenario: A user should be able to turn sms messaging
#    Given "valid" user clicks login
#    And the "valid" user tries to log in
#    And the user taps you
#    And the user taps settings
#    And the user taps communications
#    When the user taps on sms messaging
#    Then the user should be able to enable or disable sms messaging
#
#  Scenario: A user should be able to set and unset various email communications
#    When the user taps on email subscriptions
#    # @ToDo
#    # Then the user should be able to set and save their desired email preferences
#    Then Email Subscriptions should open in a Webview
#
#  # @Todo - Fix this defect in future
##  Scenario: A user should be able to set preferred push notifications
##    When the user taps on push notifications
##    Then the user should be able to set push notification preferences
#
#
#
#    # behave sharecare/features/scenarios/settings/communications.feature

  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

  @testrail-C44804 @testrail-C4423 @testrail-C4421
  Scenario: Login user
    Given user taps "You"
    And user taps "Take It Later"
    And user taps " Button"
    And user taps "Communications"
    Then user should see "Push Notifications"
    Then user should see "Email Subscriptions"
    Then user should see "Text Messages"
    Given user taps "Email Subscriptions"
    Then user should see "webView"
    Then user should see "Receive emails"
    Then user should see "Personalized Reminders"
