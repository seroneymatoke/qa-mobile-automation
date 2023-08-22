# Created by seroneymatoke at 29.12.21
  # Flaky Test.
  @sanity @search @smoke-android @sanity-sc
Feature: A user should be able to search

  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    Given user taps "Skip"

  Scenario: Tap Search
    Given user taps "Search"

    @testrail-C44824 @testrail-C44825 @testrail-C43868 @testrail-C43869 @testrail-C43870 @testrail-C28834 @testrail-C28840 @testrail-C28835 @testrail-C3372 @testrail-C28839 @testrail-C28836
  Scenario Outline: Search suggests the results for query
    Given user sets "input_field" to "<value>"
    And user waits for "5" seconds
    #And user presses enter on "input_field"

    Then user should see "<result>"

      Examples:
      |value|result|
      |settings  |Shortcut|
      |30   |slideshow|
      |sex  |topic |
    # Given user taps "article"
    # Then user should see "<string>"
      

    @testrail-C44830 @testrail-C28900
  Scenario: Follow topic, verify that it appears in followed topics
    Given user goes back "1" times
    Given user taps "Discover"
    And user scrolls "5" times direction "down"
    And user taps "Health Topics"
    And user taps "Follow"
    Then user should see "Following"
    Given user taps "Home"
    And user waits for "5" seconds
      # Flaky - Search
    # Given user taps "Search"
      # Flaky
    Given user sets "input_field" to "ADHD"
    And user waits for "5" seconds
    Then user should see "topic"