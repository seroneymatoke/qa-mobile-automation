from behave import *
from faker import Faker

faker = Faker()

@given(u'A User taps forgot password')
def step_impl(context):
    if 'android' in context.config.userdata.get('platform'):
        context.forgot_password.tap_forgot_password()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@given(u'A user enters a valid email')
def step_impl(context):
    if 'android' in context.config.userdata.get('platform'):
        context.forgot_password.enter_email(faker.email())
        context.forgot_password.tap_send()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')


@then(u'A user should get a successful alert upon tapping send button')
def step_impl(context):
    if 'android' in context.config.userdata.get('platform'):
        assert 'sent' in context.forgot_password.return_msg()
    elif 'ios' in context.config.userdata.get('platform'):
        print('ios')
    else:
        print('platform unavailable')
