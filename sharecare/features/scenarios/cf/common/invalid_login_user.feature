# Created by seroneymatoke at 29.10.21
@invalid @sanity-sc

  # No longer needed
Feature: Invalid Login into Sharecare

  # https://sharecare.testrail.io/index.php?/cases/view/3366&group_by=cases:section_id&group_order=asc&group_id=734

  Scenario: Invalid Login
    Given "invalid" user clicks login
    And the "invalid" user tries to log in
    Then an error message should be displayed

  Scenario:
    Given "missing_password" user clicks login
    And the "missing_password" user tries to log in
    Then an error message should be displayed

    @invalid-email
  Scenario:
    Given "incomplete_email" user clicks login
    And the "incomplete_email" user tries to log in
    Then an error message should be displayed

    # behave -v sharecare/features/scenarios/common/invalid_login_user.feature -f html -o reports/test-report.html
