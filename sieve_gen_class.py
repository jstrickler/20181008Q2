#!/usr/bin/env python


class Primes():

    def __init__(self, limit):
        self._limit = limit
        self._curr = 2
        self._flags = set()

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(2, self._limit):
            if i in flags:
                continue
            for j in range(2 * i, self._limit + 1, i):
                flags.add(j)  # <2>
            yield i  # <3>
