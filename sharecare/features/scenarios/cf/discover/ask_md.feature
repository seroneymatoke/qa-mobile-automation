# Created by seroneymatoke at 22.04.22
  @sanity @ask_md @discover @sanity-sc
Feature: AsK MD
  All ask MD tests

  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    Given user taps "Skip"

  Scenario: Find a Doctor opens a WebView
    Given user taps "Discover"
    And user scrolls "5" times direction "down"
    Then user should see "AskMD"
    Given user taps "AskMD"

  @testrail-C44757 @testrail-C44759 @testrail-C4384 @testrail-C4386
  Scenario Outline: It is possible to start a survey via searching for symptoms/Able to quit survey midway
    Given user taps "Search"
    Given user sets "Search" to "<symptom>"
    Given user taps "<suggestion>"
    Then user should see "Symptom Consultations"
    Given user taps "<consultation>"
    Then user should see "0%"
    Then user should see "Me"
    Then user should see "Someone else"
    Then user should see "Next"
    Given user taps "Quit"
    Then user should see "Do you want to quit the Consultation?"
    Given user taps "Quit"
    Then user should see "Symptom Consultations"
    Given user goes back "1" times
      Examples:
      |symptom|suggestion|consultation|
      |Headache|headache |Headache    |
      |Migraine|migraine |Dizziness or Vertigo|


  @testrail-C44758 @testrail-C4385
  Scenario Outline: It is possible to start a survey via selecting a condition
    Given user taps "Want to manage a condition?"
    Given user taps "<condition>"
    Then user should see "0%"
    Then user should see "Me"
    Then user should see "Someone else"
    Then user should see "Next"
    Given user taps "Quit"
    Then user should see "Do you want to quit the Consultation?"
    Given user taps "Quit"
    Given user goes back "1" times
      Examples:
      |condition|
      |Asthma Management|
      |COPD Management  |
      |Chronic Pain Management|

    @testrail-C44760 @testrail-C4387
    Scenario: Upon finishing the survey, the results are being shown
      Given user taps "Want to manage a condition?"
      And user taps "Asthma Management"
      And user taps "Next"
      And user taps "Next"
      And user taps "Next"
      And user taps "Next"
      And user sets "Pounds:" to "value"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "daily"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "checkBox"
      And user taps "Next"
      And user taps "Next"
      And user taps "Next"
      # And user taps "Next"
      And user taps "Get Results"
      Then user should see "Recommendations"

      @testrail-C44761 @testrail-C4388
  Scenario: It is possible to view Previous Consultations
    Given user goes back "1" times
    Given user goes back "1" times
    And user taps "Previous Consultations"
    Then user should see "date"
    Then user should see "text"



