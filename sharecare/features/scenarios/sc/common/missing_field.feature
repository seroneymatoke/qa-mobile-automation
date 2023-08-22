# Created by ismail.koembe at 12.12.21
  # @todo - And Testcase implementation
  @testrail-C175475 @sanity-sc @missing_fields @sanity-ios-cf
Feature: User that has missing field should be prompted to submit additional info
  # Enter feature description here

  Scenario: Missing fields screen shown
  Given I create and logged in with missing field user
  Then user should see "We need some more information to continue your experience."
  Then user should see "Continue"


   # behave -v sharecare/features/scenarios/common/missing_field.feature