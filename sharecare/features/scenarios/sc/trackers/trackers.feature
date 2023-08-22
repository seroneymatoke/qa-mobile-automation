# Created by seroneymatoke at 16.03.22
@trackers @talk @sanity-sc
Feature: Tracker Tests

  @testrail-C44706
  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  @testrail-C44703
  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

    # Dependency of other apps negated - Need to install multiple apps and conform to the TCs - Can only check if the options are available. Recommend to test manual connection
  @testrail-C4251 @testrail-C44746 @testrail-C44747 @testrail-C44748 @testrail-C44749 @testrail-C44750 @testrail-C4366 @testrail-C4367 @testrail-C4368 @testrail-C4383 @testrail-C4369 @testrail-C13899 @testrail-C13900
  Scenario: It is possible to enable automatic tracking
      Given user taps "Track"
      Then user should be able to enable automatic tracking

  @testrail-C44743 @testrail-C4365
  Scenario: It is possible to submit a tracker
    Given user taps add today's entry
    Then user should be able to submit a tracker


