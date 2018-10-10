#!/usr/bin/env python
from dateutil import parser
from datetime import date, timedelta, datetime, time as Time

import time


today = date.today()

now = datetime.now()

print(today, now)

james_bd = date(2014, 8, 1)

print(james_bd)

elapsed_days = today - james_bd

print(elapsed_days)

years, days = divmod(elapsed_days.days, 365.25)

print(f"James is {years} years and {days} days old")


fortnight  = timedelta(14)

x = today + fortnight
print(x)

print(time.time())

