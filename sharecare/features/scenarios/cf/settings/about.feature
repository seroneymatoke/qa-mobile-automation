# Created by seroneymatoke at 23.11.21
@sanity  @demo  @about @settings @sanity-sc
Feature: About opens in a Webview

  # https://sharecare.testrail.io/index.php?/cases/view/4422&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=1024
  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

  @testrail-C4422
  Scenario: Navigate to module
    Given user taps "You"
    And user taps "Take It Later"
    And user taps " Button"
    And user taps "About Us"
    Then user should see "webView"
    Then user should see "About Sharecare"

    # behave -v --tags=about sharecare/features/scenarios/settings/about.feature