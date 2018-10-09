#!/usr/bin/env python

# mary_in = open(...)
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n\r')
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        print(raw_line, end='')
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(repr(contents)) # raw string
    print('*' * 20)
    print(str(contents))  # cooked string
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)
