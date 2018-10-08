#!/usr/bin/env python

a = 5

person = 'Matt'

b = a

print(b)

a = 25
print(a, b)

x = 5
y = 5
z = 5
print(id(x), id(y), id(z), id(b))

m = 300
n = 300

print(id(m), id(n))


list1 = ['a', 'b', 'c']
list2 = list1
list3 = ['a', 'b', 'c']

print(list1 == list2)
print(list1 == list3)
print(list1 is list2)
print(list1 is list3)

_ = 10

print(_)

customer_id = '1234'

id = '1234'

# dir = 'North'

x = 5

x = 'Ralph Cramden'

print(dir(x))

print()

x = 5

y = 'wombat'

z = 27.9302

# print(x + z)
#
# print(y + x)

print(x * y)

print('-' * 60)












