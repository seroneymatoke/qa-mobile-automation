# Created by seroneymatoke at 26.10.21

@sanity-sc @demo @common @talk @launch @smoke @ss
Feature: Launching the app
  # Launching app.
  @testrail-C44696 @testrail-C4428 @testrail-C44820 @testrail-C44697 @testrail-C44698 @testrail-C44699 @testrail-C3363 @testrail-C3364 @testrail-C4328 @testrail-C4353 @testrail-C43858 @testrail-C43859 @testrail-C43860 @testrail-C43858 @testrail-C20576 @testrail-C44701 @testrail-C3366 @testrail-C43861 @testrail-C44757 @testrail-C44759 @testrail-C4384 @testrail-C4386 @testrail-C44753 @testrail-C44754 @testrail-C4372 @testrail-C4373 @testrail-C4411
  Scenario: App launch from deployment
    Given That app is launched successfully
    Then user should see "Create Account"
    Then user should see "Sign In"

    # Then user should be able to see the splash screen
    # Given "valid" user clicks login

  # behave -v sharecare/features/scenarios/common/splash_screen.feature
  # https://discuss.appium.io/t/appium-always-reinstall-the-app-while-executing-the-script-how-to-resolve-the-issue/9960

   # behave -v -k sharecare/features --tags=launch -D platform=android_device -D env=STAGE -D market=US -D release=Poseidon -D build=R-Candi -D app_version=4.28.0.17925

  # behave -k sharecare/features --tags=rat -D platform=android_device -D env=STAGE -D market=US -D app_version=4.29.0 -D release=Quirinus -D build=17802 -D app_type=R-Candi