"""

TODO new TestRuns will need to be created each month so testrun_id will need updated

invoke now
invoke ioslogin
invoke iosregister
invoke androidlogin
invoke androidregister
"""


def berlin_login():
    # https://sharecare.testrail.io/index.php?/runs/view/
    platform = "android_device"
    suite_name = "Mobile_Automation_Zeus"
    # make sure ['testrun_id', 'test_case_id', ios_no_reset,'feature_file']
    # @ToDo - Autoget Testcase ID
    tr_features = [
        # ["106581", "45833", "False", "sharecare/features/scenarios/common/missing_field.feature"],
        # ["106581", "4421", "False", "sharecare/features/scenarios/settings/communications.feature"],
        ["106581", "3365", "False", "sharecare/features/scenarios/common/register_us_user.feature"]
        # ["106581", "32687", "False", "sharecare/features/scenarios/common/register_us_user.feature"],
        # ["106581", "4422", "False", "sharecare/features/scenarios/settings/about.feature"],
        # ["106581", "3385", "False", "sharecare/features/scenarios/common/valid_login.feature"],
        # ["106581", "3366", "False", "sharecare/features/scenarios/common/valid_login.feature"],
        # ["106581", "13893", "False", "sharecare/features/scenarios/common/password_validation.feature"],
        # ["106581", "44796", "False", "sharecare/features/scenarios/settings/account.feature"],
        # ["106581", "20576", "False", "sharecare/features/scenarios/settings/gdpr.feature"],


    ]

    return [platform, suite_name, tr_features]
