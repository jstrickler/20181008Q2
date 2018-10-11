#!/usr/bin/env python
# (c) 2015 John Strickler
#
import sys
from datetime import date
import yaml

george = [
    {
        'num': 1,
        'lname': 'Washington',
        'fname': 'George',
        'dstart': date(1789, 4, 30),
        'dend': date(1797, 3, 4),
        'birthplace': 'Westmoreland County',
        'birthstate': 'Virginia',
        'term': [ date(1732, 2, 22), date(1799, 12, 14) ],
        'assassinated': False,
        'party': None,
    }
]

with open('george.yaml', 'w') as george_out:
    yaml.dump(george, george_out)

yaml.dump(george, sys.stdout)
