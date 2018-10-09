#!/usr/bin/env python

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
print(people[0][0])
for person in people:
    print(person[0])

x = ['a', 'b', 'c']
r = reversed(x)

print(r)
for i in r:
    print(i)

x = ['a', 'b', 'c']

y = [10, 20, 30]

m = zip(x, y)
print(m)
print(list(m))
print(list(m))


cities = ['Durham', 'Cary', 'Morrisville', 'Apex',
          'Carrboro', 'Chapel Hill']

for i, city in enumerate(cities):
    print(i, city)
print()

print(list(enumerate(cities)))

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

for i, (first_name, last_name, product) in enumerate(people, 1):
    print(i, first_name, last_name)
print()

for i, city in reversed(list(enumerate(sorted(cities)))):
    print(i, city)

flags = [False] * 10
print(flags)

x = ['foo'] + ['bar']
print(x)

for i in range(10):  # range(start, stop, step)
    print("Go Python! Represent!")

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')
