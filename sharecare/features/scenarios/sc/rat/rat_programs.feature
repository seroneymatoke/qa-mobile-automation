@sanity-sc @rat-programs
Feature: RAT Programs
  # Enter feature description here

  Scenario: Already created user logs in
    Given existing user logs in with "seroney.us@ftqa.com", and "@@Com/12/07@@"

  Scenario: Skip
    Given user taps "Skip"

    @testrail-C4402
  Scenario: Possible to Enroll to programs
    Given user taps "You"
    And user taps "Your RealAge"
    And user taps "Programmes"
    Then user should see "Participating"


  @testrail-C4403 @testrail-C4404
  Scenario: Possible to Submit progress/Enroll to programs
    Given user scrolls "2" times direction "down"
    And user taps "Track my steps"
    And user sets "Steps" to "4000"
    And user taps "Save"
    And user taps "Participating"
    Then user should see "Leave"
    # Given user taps "Leave"
