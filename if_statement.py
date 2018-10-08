#!/usr/bin/env python
value = 56

if value > 75:
    print("wombat")
    print("kookaburra")
elif value > 50:
    print("wallaby")
    print("kangaroo")
else:
    print("platypus")
    print("aardwolf")
print("Done")

for i in range(10):
    print(i)

#  bool()
print(bool(0))
print(bool(1))
print(bool(1.00000000000000000000000001))
print(bool("False"))
print(bool(False))
print(bool(""))


class Foo():
    def __init__(self, value):
        self._value = value

    def __bool__(self):
        return bool(self._value % 2)

f1 = Foo(5)
print(bool(f1))

f2 = Foo(4)
print(bool(f2))

#  None  False True

x = 5

if x:
    pass

if bool(x):
    pass

if x == True:
    pass

if "m" in globals():
    print("m is defined")
else:
    print("m is not defined")

print(dir())

x = 0
if x is not None:
    print("Represent!")

#  == !=  >  <  >= <= is  is not

#  and   or   not

print(5 and 12)
print(5 or 12)
print((5 and 12) == 12)
print(None and 5)
print(0 and 12)

x = 0
limit = x or 50

print(5 == 5)
print(5 is 5)










