@trackers2
@testrail-C241322
# Precondition: User already submitted Relationship tracker for today

Feature: Tracker Tests

    Scenario: Existing User logged into the app
        Given existing user logging in with details kristin_wilson_genera_466448@scqa.me, and Aut0Mati0n_

    Scenario: User is on Track screen
        Given user taps tracker

    Scenario: User Tap on the 'See more' button of the Relationship card
        Given user scrolls "9" times direction "down"
        Given user taps "See more about Relationship"
        Then user should see "History"

    Scenario: User deletes today's entry in the Relationship card
        Given user scrolls "1" times direction "down"
        When user taps ... icon
        Given user taps "Delete"
        Then user should see "No data"