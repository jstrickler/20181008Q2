#!/usr/bin/env python
from pprint import pprint
import json

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, *fields = raw_line.rstrip().split(':')
        knight_data[name] = tuple(fields)

pprint(knight_data)

x = json.dumps(knight_data)

print(x)



