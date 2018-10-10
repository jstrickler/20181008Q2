#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]


f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

# [EXPR for VAR in ITERABLE ... if COND ...]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2= [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

#  A?B:C

#  B if A else C

suits = 'clubs diamonds hearts spades'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [(r, s) for s in suits for r in ranks if r > '9' if s != 'hearts']

print(cards, '\n')


f3 = [f for f in fruits if f.startswith('p')]
print('f3:', f3, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print(last_names, '\n')

with open('DATA/mary.txt') as mary_in:
    lines = (line.rstrip() for line in mary_in)
    short_lines = (line[:5] for line in lines)

    for line in short_lines:
        print(line)

# if 5 < x  < 10:
#     pass

















