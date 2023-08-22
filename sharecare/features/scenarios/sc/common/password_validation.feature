# Created by seroneymatoke at 12.11.21
@sanity @demo @sl @common @sanity-sc @password_validation @common
#ToDo - Need to delete
Feature: Password validation
  Password should be validated according to market rules
  # https://sharecare.testrail.io/index.php?/cases/view/13893&group_by=cases:section_id&group_id=734&group_order=asc&display_deleted_cases=0

  @testrail-C44704 @testrail-C13893
  Scenario: User populates required data
    Given user clicks create account
    And "valid_us_user" user selects country
    And user clicks continue
    # Validates screen loads successfully
    # And user validates page elements
    And "valid_us_user" user enters first name
    And "valid_us_user" user enters last name
    And "valid_us_user" user enters email address
    And user enters birth date
    And user selects gender
    And "valid_us_user" user enters Zip Code
    Then entered passwords should be validated


# behave -v sharecare/features/scenarios/common/password_validation.feature