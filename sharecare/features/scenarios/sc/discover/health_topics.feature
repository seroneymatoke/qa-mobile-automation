# Created by seroneymatoke at 11.02.22
  @health_topics @sanity @discover @sanity-sc
Feature: Health Topics

  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    Given user taps "Skip"

  @testrail-C44706
  Scenario: Find a Doctor opens a WebView
    Given user taps "Discover"
    And user scrolls "4" times direction "down"
    And user taps "Health Topics"

  @testrail-C44762 @testrail-C44830 @testrail-C4389
  Scenario: Possible to follow and unfollow from main screen
    Given user is on the main screen
    And user taps "Follow"
    Then user should see "Following"
    Given user taps "Following"
    Then user should see "Follow"
#    Given user taps "Follow"
#    And user taps "Home"
#    Given user taps "Search"
#    Given user sets "input_field" to "ADHD"
#    And user waits for "5" seconds
#    Then user should see "topic"



  @testrail-C44763 @testrail-C4390
  Scenario: It is possible to Follow/Unfollow a topic from their details view
    Given user is on detailed view screen
    And user taps "Follow"
    Then user should see "Following"

  @testrail-C44764 @testrail-C4391
  Scenario: All filter options are available when tapping the filter
    Given user taps filter
    Then all filters should be available

  @testrail-C44765 @testrail-C44821 @testrail-C20577 @testrail-C8847 @testrail-C8848 @testrail-C20578
  Scenario: Health Topics are not displayed for language light (toggle "healthTopicsEnabled": false)
    Given user taps "You"
    And user taps "Take It Later"
    Given user taps " Button"
    Given user taps "Languages"
    And user taps "Dutch (NL)"
    Given user taps "Ontdekken"
    And user scrolls "3" times direction "down"
    Then user should see "Inspiraties"

