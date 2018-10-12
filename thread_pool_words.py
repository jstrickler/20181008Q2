#!/usr/bin/env python
import random
from multiprocessing import Pool

with open('DATA/words.txt') as words_in:
    all_words = [w.rstrip() for w in words_in]
    random.shuffle(all_words)

def doit(word):
    return word.upper()

if __name__ == '__main__':
    p = Pool(30)

    results = p.map(doit, all_words)
    print(results[:50])

