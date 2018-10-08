#!/usr/bin/env python

i1 = 100
i2 = 0b100
i3 = 0x100
i4 = 0o100   # NOT 0100

big_int = 23985209358209385209835029385029385029385029385029850293850298350298350928350928305982039582039582093850298350298350

x = big_int + 1
print(x)

weird_num = '439HJ2493DG3'

print(int(weird_num, 31))

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.23432e18

c1 = 123j

print(c1, type(c1))

x = 23
y = 7
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)

x = 5
x += 10
x /= 3
print(x)

x = 2
x **= 5
print(x)

x = 45.689203
print(round(x, 2))
print(round(x, 0))


x = 5
y = '123'

print(x + int(y))
print(str(x) + y)

print(int('100'))
print(int('100', 16))
print(int('100', 2))
print(int('100', 8))
print(int('100', 36))

# print(str(obj1), ..., end='\n', sep=' ', file=stdout,
#   flush=False)

#  repr() str()

x = "Chad"

print(str(x))
print(repr(x))

class Foo():
    def __repr__(self):
        return 'Huzzah'

f = Foo()
print(f)

print(11 - 8.3)

a = 'Fred'
b = 'Mary'
c = 'Joe'

print(a, b, c)
print(a, b, c, sep='/')
print(a, end=':')
print(b, end='//wow//')
print(c)

print(a, end='\n' * 5)
print("Done.")




