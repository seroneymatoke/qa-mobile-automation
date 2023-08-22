import datetime
import os
import sys
import time
import re
import configparser
import json
from invoke import task
from testrail import APIClient
import tasks_testrail
import collections
from colorama import Fore, Back, Style
import traceback

# DEBUG = True
"""
invoke now
invoke ioslogin
invoke iosregister
invoke androidlogin
invoke androidregister

"""
# setup testrail configs and creds
config = configparser.ConfigParser()
config.read('behave.ini')
client = APIClient('https://sharecare.testrail.io/')
client.user = config['behave.userdata']['test_rail_username']
client.password = config['behave.userdata']['test_rail_password']
env = config['behave.userdata']['env']
# put functions from 'tasks_testrail.py' inside this list if you want them to run


nows = [
]

onboardings = [
    tasks_testrail.berlin_login(),
]


def testrun(c, suites):
    print(suites)
    num = len(suites)
    print(f"\n starting all {num} test suites")
    # Begin the loop of each of the suites
    for suite in suites:
        # We want to move on the the next suite if this script fails
        try:
            platform, suite_name, tr_features = suite
            # Setting up the Scaffolding
            hourly_reports_folder = f"reports/appium"
            if not os.path.exists(hourly_reports_folder):
                os.makedirs(hourly_reports_folder)
            #######################################
            print(f"Beginning {suite_name}")
            #######################################
            # Begin the loop of each test case for the suite
            for x in tr_features:
                try:
                    print(
                        f"behave {x[3]} -D platform={platform} -D no_reset={x[2]} -o {hourly_reports_folder}/{x[1]}_log.txt > {hourly_reports_folder}/{x[1]}_summary.txt")
                    c.run(
                        f"behave {x[3]} -D platform={platform} -D no_reset={x[2]} -o {hourly_reports_folder}/{x[1]}_log.txt > {hourly_reports_folder}/{x[1]}_summary.txt")
                    #
                except:
                    pass
                #
                print(f"Adding Results for {suite_name}\n")
                summary = f"{hourly_reports_folder}/{x[1]}_summary.txt"
                feature_log = f"{hourly_reports_folder}/{x[1]}_log.txt"
                with open(summary, 'r') as file:
                    summary_report = file.read()
                with open(feature_log, 'r') as file:
                    feature_report = file.read()
                #
                #
                timestamp = time.ctime(os.path.getctime(summary))
                # time format for test rail
                minutes = re.search(r"Took (\d+)m\d+", summary_report).group(1)
                seconds = re.search(r"Took \d+m(\d+)", summary_report).group(1)
                if summary_report.lstrip().startswith('Failing scenarios:'):
                    failure_log = f"{hourly_reports_folder}/{x[1]}_log.txt"
                    with open(failure_log, 'r') as file:
                        failure_log_report = file.read()
                    # if "Failing" in summary_report:
                    body = {
                        'status_id': 5,
                        'comment': f'{timestamp}\n{summary_report}\n{failure_log_report}',
                        'elapsed': f'{minutes}m {seconds}s'
                    }
                    # print(Fore.RED + str(body))
                else:
                    body = {
                        'status_id': 1,
                        'comment': f'{timestamp}\n{summary_report}\n{feature_report[0:200]}...',
                        'elapsed': f'{minutes}m {seconds}s'
                    }
                    # print(Fore.GREEN + str(body))
                #
                if 'DEBUG' in globals():
                    print(body)
                #
                client.send_post(f'add_result/{x[0]}', body)
                #
                if summary_report.lstrip().startswith('Failing scenarios:'):
                    print(Fore.RED)
                    # print(json.dumps(add_result, indent=4, sort_keys=True))
                    print(feature_report.replace('\\n', '\n'))
                    print('\n')
                    print(summary_report.replace('\\n', '\n'))
                else:
                    print(Fore.GREEN)
                    # print(json.dumps(add_result, indent=4, sort_keys=True))
                    print(feature_report[0:200].replace('\\n', '\n') + '...')
                    print('\n')
                    print(summary_report.replace('\\n', '\n'))
                #
                print(Style.RESET_ALL)
                #
        ######################################
        ######################################
        except Exception:
            cept = "There was an Exception...moving on to the next suite"
            print(Fore.RED + str(cept))
            print(Style.RESET_ALL)
            continue
        # traceback.print_exc()


#
# task cannot have underscores



@task
def now(c):
    testrun(c, nows)


@task
def onboarding(c):
    testrun(c, onboardings)


