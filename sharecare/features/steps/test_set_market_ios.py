from behave import *


@given("A user sets market")
def set_market(context):
    if 'ios' in context.config.userdata.get('platform'):
        market = str(context.config.userdata.get('market'))
        env = str(context.config.userdata.get('env'))
        # if context.config.userdata.get(env) == "STAGE" or context.config.userdata.get(env) == "PRD" or context.config.userdata.get(market) == "BR" or context.config.userdata.get(market) == "US":
        context.set_env.set_env_market_ios(context, market.upper(), env.upper())
