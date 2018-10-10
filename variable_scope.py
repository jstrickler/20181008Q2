#!/usr/bin/env python
import sys

x = 100 # GLOBAL
y = 42  # LOCAL

def foo():
    m = 5
    def bar():
        print("m is", m)

    return bar

x = foo()
x()

def spam():
    x = 'apocalypse'
    print("x is", x)
    print("y is", y)

spam()
print("main: x is", x)
# print("main: y is", y)
