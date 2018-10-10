#!/usr/bin/env python

person = 'Fred', 'Smith', 24

print(len(person), person[0])

first_name, last_name, age = person   # UNPACK!

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


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
    ('Linus', 'Torvalds', 'Linux', 'Git'),
    ('John', 'Strickler'),
]

for first_name, last_name, *_ in people:
    print(first_name, last_name)

for i, v in enumerate(values):
    print(i, v)



print(list(enumerate(values)))


stuff = [
    ('Bob', ('Fishing', 'Ice Fishing', 'Fly Fishing')),
    ('Martha', ('Whaling', 'phishing', 'crushing the corporate oligarchy')),
]

for person, (h1, *other) in stuff:
    print(person, h1, other)


stuffed = {
    'Bob' : ('Fishing', 'Ice Fishing', 'Fly Fishing'),
    'Martha' : ('Whaling', 'phishing', 'crushing the corporate oligarchy'),
}

for key, (h1, *_) in stuffed.items():
    print(key, h1)





