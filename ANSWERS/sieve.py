#!/usr/bin/env python

import sys
from time import time

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * (limit)

count = 0
start = time()
for num in range(2, limit):
    if flags[num]:
        print(num, end=' ')
        count += 1
        for multiple_of_num in range(2 * num, limit, num):
            flags[multiple_of_num] = False

print(f"\n{count} primes")
print(time() - start)
