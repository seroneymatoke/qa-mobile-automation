#!/usr/bin/env python
from sharecare.features.environment import tok_env
from argparse import ArgumentParser
from sharecare.configs import tokens
from sharecare.configs import users

# environment setup

# @todo - need to fix this
env = 'uat'
market ='us'


print("Dict:  "+str(tok_env))


try:
    env = env.lower()
    market = market.lower()
except:
    raise ValueError("missing configuration")

if env != 'stage' and env != 'qa' and env != 'uat' and env != "prod":
    raise ValueError("Invalid enviroment")

# URLs
sc3_urls = {"us": {"qa": "https://api-sc3.qa.sharecare.com", "stage": "https://api-sc3.stage.sharecare.com",
                   "uat": "https://api-sc3.uat.sharecare.com", "prod": "https://api-sc3.sharecare.com"}}
sso_urls = {"us": {"qa": "https://auth.qa.sharecare.com", "stage": "https://auth.stage.sharecare.com",
                   "uat": "https://auth.uat.sharecare.com", "prod": "https://auth.sharecare.com"}}
# @Todo - Ismail to Send new URLs
sso_resource_scopes = {
    "us": {"qa": "https://ue1-qa-api.feingoldtech.com", "stage": "https://ue1-stg-api.feingoldtech.com",
           "uat": "https://ue1-uat-api.feingoldtech.com", "prod": "https://ue1-prd-api.feingoldtech.com"}}
mongo_urls = {"us": {"qa": "mongodb.qa.ftech.sharecare.com", "stage": "mongodb.stg.ftech.sharecare.com", "uat": "",
                     "prod": ""}}
servicesapi_urls = {
    "us": {"qa": "https://servicesapi.mservices.sharecare.com", "stage": "https://servicesapi.stage.sharecare.com",
           "uat": "https://servicesapi.uat.sharecare.com", "prod": "https://servicesapi.sharecare.com"}}
api_urls = {"us": {"qa": "https://api.qa.sharecare.com", "stage": "https://api.stage.sharecare.com",
                   "uat": "https://api.uat.sharecare.com", "prod": "https://api.sharecare.com"}}

# Deeplinks
base_url = "https://you.sharecare.com/"
discover = "/discover"
you = "/you"
tracker = "/tracker"
achieve = "/achieve"


# tokens
basic_token = tokens.basic_tokens[market][env]
sc3_url = sc3_urls[market][env]
sso_url = sso_urls[market][env]
sso_resource_scope = sso_resource_scopes[market][env]
mongo_url = mongo_urls[market][env]
servicesapi_url = servicesapi_urls[market][env]
api_url = api_urls[market][env]
sc3_admin_users = users.sc3_admin_user[market][env]["email"]
sc3_admin_password = users.sc3_admin_user[market][env]["password"]