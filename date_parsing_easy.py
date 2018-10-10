#!/usr/bin/env python
#
import sys
import dateutil
from dateutil import parser
print(sys.version)

date_strings = [  # <1>
    'April 1, 2015',
    '4/1/2015',
    'Apr 1, 2015',
    'Apr 1 2015',
    '04/01/2015',
    '1 Apr 2015',
    'April 1st, 2015',
    'April 1, 2015 8:09',
    '4/1/2015 8:09 PM',
    'Apr 1, 2015 5 AM',
    'Apricot 4, 341',
    'July 4',
    '4',
    '7/4',
    '32',
    '9/30/1980 10:00:04.293032',
    '1.12344',
]

for date_string in date_strings:
    try:
        dt = parser.parse(date_string)  # <2>
        print(dt)
    except ValueError as err:
        print("Can't parse", date_string)
