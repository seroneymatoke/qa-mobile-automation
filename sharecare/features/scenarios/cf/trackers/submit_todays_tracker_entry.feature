@today
@testrail-C241321

Feature: Tracker Tests

    Scenario: Existing User logged in to the app
        Given existing user logging in with details kristin_wilson_genera_466448@scqa.me, and Aut0Mati0n_
    #And user taps "Skip"
    # Given user clicks not now
    #Then user should see home guided tooltips


    Scenario: User is redirected on Track screen
        Given user taps tracker
    #Given user taps "Skip"

    Scenario: User should be able to tap + icon in Relationship card
        Given user scrolls "4" times direction "down"
        And user taps "Relationship Add Today's Entries Button"
        And user taps "Lots of meaningful interactions"
        And user taps "Save"

    Scenario: User should be able to see Today submitted icon is shown on Relationshipcard chart
        Given user scrolls "9" times direction "down"
        Then user should see "Many interactions"
        Then user should see "Previous 7 days · Last update: Today"
