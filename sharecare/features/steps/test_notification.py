import time

from behave import *

from sharecare.api.notification import *
from sharecare.features.steps.test_api_calls import *


@step('I send a {type} push notification')
def push_notification(context, type):
    """
    Now we have 'regular' and 'onScreen' type notification
    This method creates new user and gets user's bearer token,
    secureId.
    SecureId and bearer token are required for content creation and push notification
    """

    user = create_user()
    secure_id = user.secureId
    print(f"created user : {user.email} {user.password} {secure_id}")
    context.execute_steps(f'''
            Given existing user logs in with {user.email}, and {user.password}
            ''')
    # now we need to create content and this content will be use as payload
    # now we need to create content
    content_id = post_congratulation_content(secure_id)
    regular_id = post_notification(type, secure_id, content_id)
    print(regular_id)


@step('I send a {type} push notification for {email} and {password}')
def push_notification_existing_user(context, type, email, password):
    """
    Now we have 'regular' and 'onScreen' type notification
    This method requires existing user's credentials.
    SecureId and bearer token are required for content creation and push notification
    Additionally, method uses email and password to log in.
    """

    user = get_token_and_secure_id(email, password)
    print(f"created user : {email} {user.get_token()} {user.secureId}")
    # now we need to create content and this content will be use as payload
    # now we need to create content
    content_id = post_congratulation_content(user.secureId)
    notification_id = post_notification(type, user.secureId, content_id)
    print(notification_id)


@step('I will dismiss all notification for {email}, {password}')
def dismiss_all_notification(context, email, password):
    """
    Dismiss all notification
    """
    user = get_token_and_secure_id(email, password)
    print(user.bearerToken)
    r = get_regular_notifications(user.bearerToken)
    o = get_onscreen_notifications(user.bearerToken)
    if len(r) > 0:
        for i in range(len(r)):
            print(r[i])
            dismiss_notification(user.bearerToken, r[i])
    if o is not None:
        for i in range(len(o)):
            print(o[i])
            dismiss_notification(user.bearerToken, o[i])

    print("notifications are dismissed")
