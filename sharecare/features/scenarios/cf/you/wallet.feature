# Created by seroneymatoke at 18.04.22
  @sanity @you- @sanity-cf @wallet
Feature: You

  @stage @prod @android
  Scenario: User logs in
    Given user logs in
    And user taps "Skip"

  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

    @testrail-C44791 @financial-health @stage @prod @android @testrail-C4413
  Scenario: Financial Health as a Webview
    Given user taps "You"
    And user taps "Take It Later"
    And user scrolls "1" times direction "up"
    And user taps "Financial Health"
    And user waits for "3" seconds
        #Cookie policies only shown on webviews
      # Saucelabs - GDPR - Won't show up but for Device in Europe Cookie policy will be shared
    # Then user should see "Sharecare Cookie Policy"
    Then user should see "Financial Health"

      @stage @prod @android
  Scenario: Navigate back to You Landing Page
    Given user goes back "1" times
    And user waits for "5" seconds
    Then user should see "Financial Health"
    Then user should see "Wallet"

       @stage @prod @android @testrail-C4414
  Scenario: Navigate to Wallet
    Given user taps "Wallet"

    @testrail-C44792 @stage @android @testrail-C4414
  Scenario: All available cards are show to the user
    Given user taps "Ok"  
    Then user should see "Prescription Discount Card"
    Then user should see "create_insurance_card"

    @testrail-C44792 @prod @android
  Scenario: All available cards are show to the user
    Then user should see "create_insurance_card"

     @testrail-C44793 @stage @testrail-C4415
  Scenario: It is possible to see the details of the card upon opening
    Given user taps "Prescription Discount Card"
    Then user should see "Member ID #"
    Then user should see "key"

       @testrail-C44794 @testrail-C4416
  Scenario: Wallet files can be downloaded
    Given user taps "Download PDF"
    Then user should see "Downloading"
       


