#!/usr/bin/env python
import numpy as np

def spam(x):
    return x * 3

a = np.array(
    [
        [5, 10, 15],
        [2, 4, 6],
        [3, 6, 9, ],
])

b = spam(a)

print(b)
