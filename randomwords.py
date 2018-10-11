#!/usr/bin/env python
#
import random

class RandomWords():
    def __init__(self):
        with open('DATA/words.txt') as words_in:
            self._word_list = [w.rstrip() for w in words_in]

    def __call__(self, num_words=1):
        return random.choices(self._word_list, k=num_words)

if __name__ == '__main__':
    w = RandomWords()
    print(w()[0])
    print(w()[5])
