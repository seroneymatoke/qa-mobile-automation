# Created by seroneymatoke at 17.11.21
  @security_pin @sanity @sanity-sc
Feature: Set Security PIN
  A user should be able to set a security pin successfully
 
 Scenario: User logs in
    Given user logs in
   And user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"


  Scenario: Navigate to module
    Given user taps "You"
    And user taps "Take It Later"
    And user taps " Button"
    And user taps "Security PIN"
    Then user should see "switch_security_pin"

    @testrail-C44807 @testrail-C4424 @testrail-C9274
  Scenario: Set Security PIN
    Given user taps "switch_security_pin"
    Then user should see "Choose your 4-digit Security PIN"
    Given user sets "2345" as PIN
    #Reenter PIN
    Then user should see "Re-enter your 4-digit Security PIN"
    Given user sets "2345" as PIN
    Then user should see "Your Security PIN has been enabled."
    Then user should see "switch_security_pin"
    Then user should see "Change PIN"
    Then user should see "Auto-Lock"

    @testrail-C44808 @testrail-C4425
  Scenario: User should be able to change pin
    Given user taps "Change PIN"
    Then user should see "Enter your current Security PIN"
    Given user sets "2345" as PIN
    Then user should see "Choose your 4-digit Security PIN"
    Given user sets "1778" as PIN
    #Reenter PIN
    Then user should see "Re-enter your 4-digit Security PIN"
    Given user sets "1778" as PIN
    Then user should see "Your security PIN has been updated."
    Then user should see "Change PIN"
    Then user should see "Auto-Lock"

    @testrail-C44809 @testrail-C4426
  Scenario: User should be able to set a time delay
    Given user taps "Auto-Lock"
    #ideally user can choose how long the app can be pushed to the back ground
    And user waits for "2" seconds  
    And user taps "15 Seconds"
    And user goes back "1" times
    Then user should see "15 Seconds"

  @testrail-C44810 @testrail-C44811 @testrail-C4427 @testrail-C35901
  Scenario: Security PIN is shown after minimising the app
    Given user backgrounds app for "15" seconds
    Then user should see "Enter your 4-digit Security PIN"

  @testrail-C44812 @testrail-C4260
  Scenario: Upon entering correct Security PIN, user can access the app
    Given user sets "1778" as PIN
    And user waits for "2" seconds
    Then user should see "switch_security_pin"
    Then user should see "Change PIN"
    Then user should see "Auto-Lock"

    @testrail-C44813 @testrail-C4371
  Scenario: It is possible to disable the Security PIN
    Given user taps "switch_security_pin"
    And user taps "Yes"
    And user sets "1778" as PIN
    Then user should see "Your Security PIN has been disabled."
