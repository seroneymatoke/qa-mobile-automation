# Test a simple test
import time

from behave import given, then


@given("That app is launched successfully")
def splash_screen(context):
    """
    Load splash screen
    """
    if 'android' in context.config.userdata.get('platform'):
        print('android')
    else:
        # Wait for IOS
        print("ios")


@then("user should be able to see the splash screen")
def verify_elements_splash_screen(context):
    # time.sleep(10)
    if 'android' in context.config.userdata.get('platform'):
        assert False not in context.splash_screen.check_splash_screen()
    else:
        print("ios pale")

