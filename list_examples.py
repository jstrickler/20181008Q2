#!/usr/bin/env python

list1 = list()
# list list1 = new list();

list2 = [5, 19, "wombat", None, False, 8.7]

list3 = []

list4 = 'wombat wallaby platypus'.split()
print(list4)

colors = ['red', 'purple', 'orange']
colors.append('blue')
print(colors, '\n')
colors.insert(0, 'black')
colors.insert(3, 'aquamarine')
print(colors)

more_colors = ['yellow', 'pink']

colors.extend(more_colors)

print(colors, '\n')

c2 = colors  # alias

c2.append("chartreuse")

print(colors)

c3 = list(colors)  # real copy

a = [1, 2, 3]
b = [4, 5, 6]

m = [a, b]
print('m:', m, '\n')
n = list(m)
print(id(m), id(n))
print('n:', n, '\n')
m[0].append('wombat')
print(n[0])

m.append('cheese')
print('m:', m, '\n')
print('n:', n, '\n')

from copy import deepcopy

p = deepcopy(m)
print(p)
p[0].append('rhubarb')
print(p)
print(m)

print(colors)

sorted_colors = sorted(colors)
print(sorted_colors)
#  sorted(iterable, key=key_func)

del colors[2]

x = colors.pop()  # x = colors.pop(-1)
print(colors)
x = colors.pop(5)
print(colors)
print(colors[-3])
print(colors[4])

print(colors[0:3])
print(colors[:3])
print(colors[2:5])

#  SEQ[START:STOP]
#  SEQ[:STOP]  SEQ[N:]  SEQ[:]  SEQ[::]
#  SEQ[START:STOP:SKIP]

print(colors[::2])

s = slice(None, None, 2)
print(colors[s])

goner = 'blue'
try:
    colors.remove('blue')
except Exception as err:
    print(f"{goner} not found")
















