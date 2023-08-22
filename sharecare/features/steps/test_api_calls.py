"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by ismailkoembe
Date: 10.12.21
Purpose: Handles api calls for mobile automation
Implementation:
TestData: None required
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

from behave import given
from faker import Faker

from sharecare.api.sso import User
from sharecare.utilities.custom_logger import CustomLogger

faker = Faker()
email = faker.first_name().lower() + "." + faker.last_name().lower() + ".automation@scqa.me"
pwd = "Qweasdzxc1!"

logger = CustomLogger.custom_logger()
@given("Create SSO user")
def create_sso_user(context):
    response = User.create_new(email, pwd)
    if response.status_code == 403:
        print("VPN required")
        sys.exit(0)

    if response.status_code == 409:
        response = User.create_new(email, pwd)
        print("user already exist")

    if response.status_code == 200:
        user = User(email, pwd)
        print(user.email)
    return user


def create_user(country="US"):
    emails = faker.first_name().lower() + "." + faker.last_name().lower() + ".automation@scqa.me"
    pwds = "Qweasdzxc1!"
    print("EEE: ")
    response = User.create_new(emails, pwds, country)
    if response.status_code == 403:
        print("VPN is required")
        sys.exit(0)

    if response.status_code == 409:
        response = User.create_new(email, pwd)
        print("user already exist")

    if response.status_code == 200:
        user = User(emails, pwds)
        print(user.email)
        print(user.account_id)
    return user


def terminate_session(account_id, bearer_token):
    response = User.terminate_session(account_id, bearer_token)
    if response.status_code == 200:
        logger.info(account_id + ": Terminated successfully")

    logger.info("Stat code: "+str(response.status_code))
    logger.info(response.json())
    return response.status_code


@given("Create user that has missing fields")
def create_sso_user_missing_fields(context):
    response = User.create_missing_field_user(email, pwd)
    if response.status_code == 401:
        logger.info("Unauthorized")
        # sys.exit(0)

    if response.status_code == 403:
        logger.info("VPN required")
        sys.exit(0)

    if response.status_code == 409:
        logger.info("user already exist")

    if response.status_code == 200:
        user = User(email, pwd)
        logger.info(user.email)
    return user


def get_token_and_secure_id(email, password):
    user = User(email, password)
    print(user.email)
    print(str(user))
    return user
