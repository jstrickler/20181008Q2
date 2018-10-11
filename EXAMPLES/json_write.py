#!/usr/bin/env python

import json

class Spam():
    pass

george = [{
    'num': 1,
    'lname': 'Washington',
    'fname': 'George',
    'dstart': [1789, 4, 30],
    'dend': [1797, 3, 4],
    'birthplace': 'Westmoreland County',
    'birthstate': 'Virginia',
    'dbirth': [1732, 2, 22],
    'ddeath': [1799, 12, 14],
    'assassinated': False,
    'party': None,
}, {'foo': 'bar'}, Spam()]  # <1>

js = json.dumps(george, indent=4)  # <2>
print(js)

with open('george.json', 'w') as george_out:  # <3>
    json.dump(george, george_out, indent=4)  # <4>
