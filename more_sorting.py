#!/usr/bin/env python

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

def by_value(e):
    abbr, name = e
    return name

for abbr, name in  sorted(airports.items(), key=by_value):
    print(abbr, name)
print('-' * 60)


for abbr, name in  sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)


#  lambda p1, ...; EXPR





