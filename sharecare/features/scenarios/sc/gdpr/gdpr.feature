# Created by seroneymatoke at 30.11.21
  # https://sharecare.testrail.io/index.php?/cases/view/20576&group_by=cases:section_id&group_id=3410&group_order=asc&display_deleted_cases=0
  # GDPR
@sanity @demo @gdpr @xx @sanity-sc
Feature: User can request and download tracker data

  Feature: Support opens in a Webview
  # Enter feature description here

  @stage @prod
  Scenario: A Non US User logs in
    Given A Non US user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

  @stage @prod @testrail-C20576
  Scenario: Navigate to module
    Given user taps "You"
    And user taps "Take It Later"
    And user taps " Button"
    And user taps "Legal & Privacy"
    And user taps "Data download"
    #And user taps "Decline"
    And user taps "Request"

    @testrail-C44823 @stage @prod @testrail-C20576
  Scenario: Validate test results
    Then user should see "Requested"

      @testrail-C44822 @stage @prod @testrail-C20575
  Scenario: A Non US country user should be able to delete account
    Given user goes back "1" times
    And user goes back "1" times
    And user taps "Account"
    And user waits for "5" seconds
    And user scrolls "3" times direction "down"
    And user taps "Delete Account"
    And user scrolls "2" times direction "down"
    And user sets "input.password" to "Qweasdzxc1!"
    And user taps "input.verification"
    And user scrolls "1" times direction "down"
    And user taps "Delete My Account"

    @stage @testrail-C44822 @testrail-C20575
  Scenario: Verify Delete Status
    Then user should see "We’re sad to see you go…"




