# Created by seroneymatoke at 11.04.22
  @feed @sanity-sc @smoke-android @sanity-sc @testrail-C3373 @testrail-C3375 @testrail-C3379
Feature: Feed Tests
  # Enter feature description here

  @testrail-C44706 @login @slow @testrail-C4250
  Scenario: Login user
    Given user logs in
    And user taps "Skip"
    # Then the user should be able to see the home screen

  @testrail-C44703
  Scenario: Validate tool tips
    # Given user clicks not now
    Given user taps "Skip"

  @testrail-C44716 @testrail-C44715 @testrail-C43865 @testrail-C3374
  Scenario: Real Age test should be seen at the top
    Then user should see "Take the RealAge Test"

#  @testrail-C44715
#  Scenario: GDT stack item is shown on top of the feedf


  @testrail-C44732 @testrail-C3389 @testrail-C4420
  Scenario: Videos can be watched in a full screen mode
    Given user taps "exo_fullscreen_button"
    # Given user taps coordinates "570" and "400"
    # Then user should see "exo_fullscreen_layout"
    And user goes back "1" times
    Then user should see "exo_fullscreen_button"

  @testrail-C44713 @testrail-C3367
  Scenario: Newly registered user gets a welcome package injected in the Feed
    Given user scrolls "1" times direction "down"
    Then user should see "Welcome to Sharecare"

  @testrail-C44718 @testrail-C3368
  Scenario: Feed is re-fetched after pulling the header
    Given user scrolls "3" times direction "up"
    Then user should see "Take the RealAge Test"

  @testrail-C44720 @testrail-C43872 @testrail-C3369 @testrail-C3370 @testrail-C3379 @testrail-C3371 @testrail-C3372
  Scenario: Feed is defaulted to "All" filter
    Given user taps "filter"
    And user waits for "5" seconds
    Then user should see "All" is selected

  @testrail-C44724 @testrail-C43871 @testrail-C3381 @testrail-C3377
  Scenario: General content in the feed can be bookmarked via Feed view
     Given user taps coordinates "200" and "600"
     And user scrolls "3" times direction "down"
     And user taps "pin"   
     Then user should see "Added to Bookmarks"

  @testrail-C44725 @testrail-C3382 @testrail-C3387 @testrail-C3386 @testrail-C3378
  Scenario: General content in the feed can be shared via Feed view
    Given user taps "share_image_view"
    # To fix this in the near future
    Then user should see "No recommended people to share with"

  @testrail-C44726 @testrail-C3380 @testrail-C3386 @testrail-C3388 @testrail-C3389 @testrail-C31007 @testrail-C126861
  Scenario: General content opens its detailed view upon tap/click
    Given user taps coordinates "400" and "600"
    And user taps "content_type_image_view"
    Then user should see "items"




            

  




