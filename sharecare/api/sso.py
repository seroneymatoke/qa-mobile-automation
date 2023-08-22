import requests
import json


import sharecare.configs.config as cfg


class User(object):
    def __init__(self, email, password, secureId=True):
        self.email = email
        self.password = password
        self.get_token()
        if secureId == True:
            self.get_secure_id()

    def get_token(self):
        payload = json.dumps({"username": self.email, "password": self.password})

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + cfg.basic_token,
            'accept-language': 'en-US-u-ms-ussystem'
        }

        response = requests.request("POST", cfg.sso_url + "/access/?grant_type=password", headers=headers, data=payload)
        self.status_code = response.status_code

        if response.status_code == 200:
            self.account_id = response.json()["account_id"]
            self.access_token = response.json()["access_token"]
            self.bearerToken = "Bearer {}_{}".format(self.account_id, self.access_token)
        else:
            self.account_id = None
            self.access_token = None
            self.bearerToken = None

    def get_secure_id(self):
        payload = json.dumps([{"owner": {"referenceType": "entity",
                                         "entityReference": cfg.sso_url + "/account/" + self.account_id},
                               "scope": {"action": "POST", "resource": cfg.sso_resource_scope}}])

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }

        response = requests.request("POST", cfg.sso_url + "/access/authorize", headers=headers, data=payload)

        self.secureId = response.json()[0]["resolvedOwner"]["entityReference"]

    def create_new(email, pwd="Qweasdzxc1", country="US") -> object:
        payload = json.dumps({
            "postalCode": "10001",
            "email": email,
            "password": pwd,
            "gender": "FEMALE",
            "lastName": "Test",
            "firstName": "Test",
            "rememberMe": False,
            "country": country,
            "dateOfBirth": 315532800000
        })

        headers = {
            'Authorization': 'Basic ' + cfg.basic_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", cfg.sso_url + "/account", headers=headers, data=payload)
        # UAT Debug
        print(str(response))
        return response

    def terminate_session(account_id, bearer) -> object:
        headers = {
            'Authorization': "Bearer "+bearer,
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "accountId": account_id,
            "currentGroupOnly": True

        })

        response = requests.request("POST", cfg.sso_url + "/access/terminate", headers=headers, data=payload)
        return response


    def create_missing_field_user(email, pwd="Qweasdzxc1") -> object:
        payload = json.dumps({
            "postalCode": "10001",
            "email": email,
            "password": pwd,
            "lastName": "Test",
            "firstName": "Test",
            "rememberMe": False,
            "country": "US",
        })

        headers = {
            'Authorization': 'Basic ' + cfg.basic_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", cfg.sso_url + "/account", headers=headers, data=payload)
        return response