#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in fruits:
        record = fruit + '\n'
        fruitlist_out.write(record)

with open('fruitlist.txt', 'w') as fruitlist_out:
    fruitlist_out.write('\n'.join(fruits) + '\n')



