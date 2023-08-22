from typing import Type, List, Any

from sharecare.configs import config as cfg
import requests
import json
import time


def post_congratulation_content(secureId):
    payload = json.dumps(
        {
            "userId": secureId,
            "content": {
                "templateId": "nudge-feedback-congratulation",
                "localeTemplatePlaceholders": {
                    "en-US-u-ms-ussystem": {
                        "DISMISS_ACTION_TEXT": "Done",
                        "REWARD_TEXT": "2,000 Points",
                        "TITLE_TEXT_ONE": "Awesome!",
                        "TITLE_TEXT_TWO": "Look what you earned",
                        "HERO_ICON_URL": "https://res.cloudinary.com/sharecare/image/upload/v1618937941/sharecare-icons/rewards/points_reward.png",
                        "ACHIEVEMENT_LABEL": "Completed:",
                        "ACHIEVEMENT_TEXT": "21 of 30 Green Days",
                        "REWARD_BUTTON_LABEL": "View Rewards",
                        "REWARD_BUTTON_URL": "https://you.stage.sharecare.com/you"
                    }
                }
            }
        }
    )

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic ' + cfg.basic_token,
        'Application': 'RealGreen/1.1.1.1/Web',
        'Client': 'webTest'
    }
    response = requests.request("POST", cfg.sc3_url + "/feed/v1/notifications/content", headers=headers, data=payload)
    response_data = response.json()
    content_id = str(response_data['id'])
    print("ContentId: ", content_id)
    return content_id


def post_notification(type, secureId, content_id):
    payload = json.dumps(
        [
            {
                "userId": secureId,
                "type": type,
                "tags": [
                    "t1"
                ],
                "contentRequests": {
                    "en-US-u-ms-ussystem": {
                        "thumbnail": "https://res.cloudinary.com/sharecare/image/upload/v1618934684/sharecare-icons/rewards/reward_circle.png",
                        "title": "Congratulations!",
                        "body": "See what you just earned.",
                        "url": "https://you.stage.sharecare.com/notifications/content/" + content_id
                    }
                },
                "pushInfo": {
                    "category": "insights",
                    "localized": [
                        {
                            "locale": "en-US-u-ms-ussystem",
                            "title": "Congratulations!",
                            "body": "See what you just earned."
                        }
                    ]
                }
            }
        ]
    )

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic ' + cfg.basic_token,
        'Application': 'RealGreen/1.1.1.1/Web',
        'Client': 'webTest'
    }

    response = requests.request("POST", cfg.sc3_url + "/feed/v1/notifications/2", headers=headers, data=payload)
    response_data = response.json()
    onscreen_id = str(response_data[0]['id'])
    return onscreen_id


def get_regular_notifications(bearerToken) -> list[Any]:
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': bearerToken,
        'Application': 'RealGreen/1.1.1.1/Web',
        'Client': 'webTest',
        'client-date-time': '2019-01-24T10:20:00+01:00'
    }

    response = requests.request("GET", cfg.sc3_url + "/feed/v1/notifications?pageSize=50", headers=headers,
                                data=payload)
    notifications = response.json()
    regular_notifications = []
    for i in notifications["notifications"]:
        regular_notifications.append(i["id"])

    return regular_notifications


def get_onscreen_notifications(bearerToken) -> list[Any]:
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': bearerToken,
        'Application': 'RealGreen/1.1.1.1/Web',
        'Client': 'webTest',
        'client-date-time': '2021-06-24T10:20:00+01:00'
    }

    response = requests.request("GET", cfg.sc3_url + "/feed/v1/notifications/onScreen", headers=headers,
                                data=payload)
    if response.text:
        notifications = response.json()
    else:
        return None
    # response = requests.request("GET", cfg.sc3_url + "/feed/v1/notifications/onScreen", headers=headers, data=payload)
    # notifications = response.json()

    onScreen_notifications = []
    for i in notifications["notifications"]:
        onScreen_notifications.append(i["id"])

    return onScreen_notifications


def dismiss_notification(bearerToken, notification_id):
    payload = {}
    headers = {
        'accept': 'application/json',
        'authorization': bearerToken,
        'application': 'RealGreen/1.1.1.1/Web',
        'accept-language': 'en-US-u-ms-ussystem',
        'Client': 'webTest',
        'client-date-time': '2021-06-24T10:20:00+01:00'
    }

    response = requests.request("PUT", cfg.sc3_url + "/feed/v1/notifications/" + notification_id + "/dismiss",
                                headers=headers, data=payload)

    print(response.text)
