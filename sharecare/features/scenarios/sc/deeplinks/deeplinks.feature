# Created by seroneymatoke at 25.08.22
@deeplinks
Feature: Test Deeplinks
  Test for deeplinks

  Scenario: User sets deeplink
    Given user logs in
    And user taps "Skip"

  @testrail-C768 @testrail-C785 @testrail-C202145 @testrail-C781 @testrail-C778 @testrail-C794 @testrail-C779
    @testrail-C202147 @testrail-C202148 @testrail-C797 @testrail-C792 @testrail-C796 @testrail-C789 @testrail-C786
    @testrail-C202160
  Scenario Outline:
    Given user navigates to abs "<url>"

  # Enter Deeplinks stuff here


    And user taps "<tap>"



    Then user should see "<value_1>"

    Then user should see "<value_2>"


    #Given

    Examples:
      | url                 | tap                | value_1          | value_2                                                                                                                 |
#    |tracker|Not Now|Today|Add Today's Entries|
#    |you    |Take It Later|Wallet|Health Profile|
#    |discover|Skip        |Your Health|Your Physical Traits|
#    |account |Account        |First Name |Last Name           |
#    |account/delete|Decline  |Delete Account|Password(required)| @Todo - need to check doesn't work to be transferred to different page
#  |ask-md|AskMD|Search|Previous Consultations|
#  |achieve|Achieve|Rewards|Challenges        |
#  |challenges|Challenges|Active|Upcoming     |
#  |communications|Communications|Push Notifications|Email Subscriptions|
      | communications/push | Push Notifications | Health Data      | Rewards                                                                                                                 |
#  |/drug-price/discover|Medication Prices|Enter medication name...|Find the lowest prices for your medications.| @Todo - Push to individual page
      | email-subscriptions | Settings           | Receive emails   | Personalized Reminders                                                                                                  |
      | messages            | Messages           | Messages         | Choose a sponsor                                                                                                        |
      | notifications       | Notifications      | No notifications | You haven't received any notifications of yet                                                                           |
      | security-pin        | Security PIN       | Security PIN     | The Security PIN protects your data from unauthorized access by autolocking the Sharecare app when you're not using it. |
      |settings             |Settings            |Account           |Languages                                                                                                                |
      |settings/data        |Settings            |Data Download     |Download                                                                                                                 |

#  Scenario: End
#    Given user terminates session
#
#    Given user backgrounds app for "5" seconds
