# Created by seroneymatoke at 12.01.22
  @sanity @achieve @sanity-sc @testrail-C90954 @testrail-C90955
Feature: Achieve Tests

  @testrail-C44706 @login @slow @testrail-C30846
  Scenario: Login user
    Given user logs in
    # Then the user should be able to see the home screen
    Given user taps "Skip"

  @testrail-C44703
  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

    @testrail-C4400
  Scenario: Open Achieve
    Given user taps "Achieve"

    @testrail-C44773 @testrail-C4401
  Scenario: Rewards opens in a webview
    Given user taps "Rewards"
    Then user should see "Rewards"
    Then user should see "Rewards"

  @testrail-C44774
  Scenario: Rewards opens in a webview
    Given user goes back "1" times
    Given user taps "Challenges"
    Then user should see "Challenges"
