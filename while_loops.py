#!/usr/bin/env python

i = 0
while i < 3:
    print("Whooooo")
    i += 1

# for i in range(3):
#     print("Whoo")

while True:
    name = input("What is your name? ")
    if name == '':
        continue # next
    if name == 'q':
        break # last
    print("Welcome, {}".format(name))
