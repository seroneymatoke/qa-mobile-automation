 # Created by seroneymatoke at 27.01.22
@sanity @find_a_doc @discover @sanity-sc
Feature: Find a Doctor

  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    Given user taps "Skip"

  @testrail-C44706
  Scenario: Find a Doctor opens a WebView
    Given user taps "Discover"
    Given user scrolls "4" times direction "down"
    Given user taps "Find a Doctor"
    Then user should see "Find a Doctor in Your Area - Sharecare"

  @testrail-C44753 @testrail-C44754 @testrail-C4372 @testrail-C4373 @testrail-C4411
  Scenario: Search by Speciality and City
    Given user sets "what" to "specialty"
    Given user sets "where" to "city"
    And user taps "Search"
    Then user matching doctors should be displayed

    # Super Flaky - Test
  @testrail-C44755 @testrail-C4375
  Scenario: Detailed Information
    Given user taps coordinates "740" and "1800"
    # Given user taps partial text "Photo: "
    Then user should see "About"

  @testrail-C44756 @testrail-C44780 @testrail-C44781 @testrail-C44782 @testrail-C44783 @testrail-C44784 @testrail-C44785 @testrail-C44786 @testrail-C4376 @testrail-C4412
  Scenario: Possible to add doctor to care
    Given user taps "Add to care team"
    Then user should see "Remove from care team"

  # behave -v sharecare/features/scenarios/discover/find_doctor.feature -D platform=cloud_android -D env=STAGE -D market=US
