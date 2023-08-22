import schedule
import time
import datetime
import os

"""
The following command will trigger the daily_invokes

python run_daily.py

invoke androidlogin

invoke now
invoke ioslogin
invoke iosregister
invoke androidregister

"""

daily_invokes = [
    "androidlogin",
]


def minutly():
    now = datetime.datetime.now()
    print(f"  Waiting for 18:05:00...{now.hour}:{now.minute}:{now.second}", end='\r')


def daily():
    for x in daily_invokes:
        now = datetime.datetime.now()
        # print(now.year, now.month, now.day, now.hour, now.minute, now.second)
        print(f"Invoking {x}...{now.hour}:{now.minute}:{now.second}")
        os.system(f'invoke {x}')


schedule.every(1).seconds.do(minutly)
schedule.every().day.at("18:05").do(daily)


while True:
    schedule.run_pending()
    time.sleep(1)
