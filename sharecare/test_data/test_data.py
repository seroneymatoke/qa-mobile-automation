"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 29.10.21
Purpose: Holds test data used in the app
Implementation:
TestData: Resides Here
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import json
import random

import requests
from faker import Faker

faker = Faker()
first_name = faker.first_name()
last_name = faker.last_name()
password = faker.password()
email = first_name.lower() + "." + last_name.lower() + ".zeus.automation@ftqa.com"

countries = [
    # 'Kenya', 'Germany', 'Kiribati', 'korea', 'kuwait', 'Latvia', 'lesotho', 'lithuania', 'luxembourg', 'madagascar',
    # 'mali', 'mali', 'marshall islands', 'mexico', 'monaco', 'namibia', 'norway', 'poland', 'canada', 'serbia',
    # 'tunisia', 'uganda', 'united kingdom',
    'united states'
]


# Get countries list
def get_country():
    r = random.choice(countries)
    return r


users = {
    'invalid': {
        'email': 'seroney1@ftqa.com',
        'password': '@@Com/12/07@@101001'
    },
    'incomplete_email': {
        'email': 'seroney1',
        'password': '@@Com/12/07@@101001'
    },
    'missing_password': {
        'email': 'seroney1@ftqa.com',
        'password': ''
    },
    'valid': {
        'email': 'seroney@ftqa.com',
        'password': '@@Com/12/07@@',
        'passcode': '2145',
        'new_passcode': '0000'
    },
    'us': {
        'email': 'seroney.us@ftqa.com',
        'password': '@@Com/12/07@@',
        'passcode': '2145',
        'new_passcode': '0000'
    }

}

registration = {
    'valid_us_user': {
        'country': get_country(),
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'confirm_password': password,
        'zip_code': faker.postcode(),
        'terms_conditions': 'enabled'
    },
    'invalid': {
        'country': get_country(),
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'confirm_password': faker.password(),
        'zip_code': faker.postcode(),
        'terms_conditions': ''
    },
    'missing_details': {
        'country': get_country(),
        'first_name': "",
        'last_name': "",
        'email': "",
        'password': "",
        'confirm_password': "",
        'zip_code': "",
        'terms_conditions': 'enabled'
    },
    'valid_br_user': {
        'country': 'Brazil',
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'confirm_password': password,
        'zip_code': Faker("pt_BR").postcode(),
        'terms_conditions': 'enabled'
    }

}

password_configurations = {
    "incorrect_length": faker.password(length=7, special_chars=True, upper_case=True, lower_case=True, digits=True),
    "missing_digits": faker.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=False),
    "missing_upper_case": faker.password(length=8, special_chars=True, upper_case=False, lower_case=True, digits=True),
    "missing_lower_case": faker.password(length=8, special_chars=True, upper_case=True, lower_case=False, digits=True),
    "missing_special_characters": faker.password(length=8, special_chars=False, upper_case=False, lower_case=True,
                                                 digits=True)
}

# print(registration['valid_br_user']['email'])
#
# for i in password_configurations:
#      print(i)

find_doc_city = [
    # 'San Antonio, TX', 'San Andreas, CA',
    'Denver, CO'
]

find_doc_speciality = [
    'Allergy', 'Cardiology', 'Dentist', 'Family Medicine', 'Surgery', 'Pediatrics'
]

country_code = ["UK", "AF", "DE"]


def select_random_choice(choice):
    return random.choice(choice)

# print(select_random_choice(find_doc_city))
