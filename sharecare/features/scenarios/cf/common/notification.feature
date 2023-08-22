# Created by ismailkoembe at 01.07.22
  # @todo - Create verification steps.
  @testrail-C31495 @testrail-C8844 @testrail-C8845 @testrail-C8846 @testrail-C31496 @testrail-C31497 @sanity-sc @push_notifications
Feature: Push Notification
  # In order to test properly, we should start with dismissing all notifications
  # This feature file can be performed both new brand and existing users
  # For now, only api implementation is done - Closed

  #@Todo - Check Token - Sftqa

  @testrail-C31495 @testrail-C8844
  Scenario: Regular push notification for existing user
    Given I will dismiss all notification for <email>, <password>
    Given existing user logs in with <email>, and <password>
#    And user taps "Skip"
    When I send a regular push notification for <email> and <password>
#    Then I should see red dot on bell icon

    Scenario: OnScreen push notification for existing user
    Given I will dismiss all notification for <email>, <password>
    Given existing user logs in with <email>, and <password>
#    And user taps "Skip"
    When I send a onScreen push notification for ikstgus@ftqa.com and Qweasdzxc1!
#    Then I should see red dot on bell icon



  Scenario: Regular push notification for brand new user
    Given I send a regular push notification
    And user taps "Skip"
#    And user taps "_SKIP_TOOLTIP_"
#    Then I should see red dot on bell icon


  Scenario: Regular push notification for brand new user
    Given I send a onScreen push notification
    And user taps "Skip"
#    And user taps "_SKIP_TOOLTIP_"
    # Then I should see red dot on bell icon