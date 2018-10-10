#!/usr/bin/env python
import typing

def get_message():
    return "Hello, Q2 World"

def say_hello():
    msg = get_message()
    print(msg)

say_hello()

def hello(whom: str='world') -> None:
    print("Hello,", whom)

hello('Earth')
hello('Mom')
hello()
print('***')

def hi(*whom):
    for who in whom:
        print("Hello,", who)

hi('Mom')
print('---')
hi('Mom', 'Dad', 'Sis', 'Bro', 'Bro')

def spam(p1, *p2):
    pass

def ham(*, filename, username, country='US'):
    pass


#  func(p, p, p, o, o, o, k, k, k, n, n, n, n)

def wacky(p1, p2=123, *p3, p4, p5='wombat', **p6):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)
    print('-' * 10)

wacky('a', p4='d', animal='wombat')

def barf():
    return 42

x = barf()
print("x is", x)






