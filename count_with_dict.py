#!/usr/bin/env python

counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        counts[food] = counts.get(food, 0) + 1

print(counts)

from collections import Counter
with open('DATA/breakfast.txt') as breakfast_in:
    c = Counter(breakfast_in)
print(c)

print(c.most_common(3))
