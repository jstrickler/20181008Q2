#!/usr/bin/env python


def plot_location(lat, lon):
    print("plotting", lat, lon)


plot_location(5, 10)

def mike(thing1, thing2, *things):
    print("things:", things)


places = [
    (5, 10),
    (4, 8),
    (9, 6),
]

for x, y in places:
    plot_location(x, y)
print()

for place in places:
    plot_location(*place)
    mike(*place, 'wombat')
print()



def spam(*, filename, username):
    print("filename:", filename)
    print("username:", username)

data = [tuple([{
    'filename': 'foo.txt',
    'username': 'ralph123',
}])]

print(data)

# spam(**data)

spam(filename='toast.txt', username='Mandrake the Magnificent')

#  $_->[bar]{blah}



