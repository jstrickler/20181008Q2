#!/usr/bin/env python

d1 = dict()
d2 = {'red': 5, 'purple': 8, 'pink': 9}
#  s = {'red', 'purple', 'pink'}   SET!
d3 = {}
d4 = dict(red=5, purple=8, pink=9)

print(d2 == d4)
pairs = [('red', 5), ('purple', 8), ('green', 9)]
d77 = dict(pairs)

keys = 'red purple green'.split()
values = 5, 8, 9
d5 = dict(zip(keys, values))
print(d5)

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

print(airports['RDU'])
print(airports.get('RDU'))
print(airports.get('GSO'))
print(airports.get('GSO', "not found"))

print(airports.setdefault('GSO', 'Greensboro'))
print(airports)

del airports['ABQ']

if 'MSN' in airports:
    del airports['MSN']

airports['ELM'] = 'Elmira/Corning'

more_airports = {'ELM': 'Elmira', 'CLE': 'Cleveland'}

airports.update(more_airports)
print(airports)

airports.setdefault('GSO', 'G2')
print(airports)

print(airports.items())

for abbr, airport in sorted(airports.items()):
    print(abbr, airport)


