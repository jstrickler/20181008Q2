#!/usr/bin/env python
"""
A wonderful example for my excellent klass.

Blah blah and more blah
"""
import sys  # standard library imports
# non-standard-library imports
# local imports

# "CONSTANTS"

MAX_VALUE = 25

def main():
    """
    Program entry point.

    :return:
    """
    doit()
    do_more()

def doit():
    """
    Do something bold!

    :return: None
    """
    print("Doing something")

def do_more():
    """
    Do even more

    :return:
    """
    print("doing some more")

if __name__ == '__main__':  # if I am called as a script
    main()

# else I am called as a module
