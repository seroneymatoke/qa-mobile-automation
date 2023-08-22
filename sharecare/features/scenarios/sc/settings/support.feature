# Created by seroneymatoke at 18.02.22
@sanity @settings @sanity-sc @support
Feature: Support opens in a Webview
  # Enter feature description here

  @stage @prod
  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

  @testrail-C44806 @stage @prod @testrail-C4423
  Scenario: Navigate to module
    Given user taps "You"
    And user taps "Take It Later"
    And user taps " Button"
    And user taps "Support"

  @prod @testrail-C4423
  Scenario: User should see support webview
    Then user should see "webView"

    @stage @testrail-C4423
  Scenario: User should see support webview
    Then user should see "webView"
    Then user should see "Log-in to your Sharecare account"


