#!/usr/bin/env python
from typing import Iterable


def spam(a: float, b: float) -> float:
    return a + b


r1 = spam(1.2, 3.4)
r2 = spam(1, 5)
r3 = spam('a', 'b')


def greet(targets: Iterable[str]) -> None:
    for t in targets:
        print("Hello,", t)
    return 'wombat'


greet(['Mom', 'Dad'])
greet([1,2,3])
# greet(5)


print(greet.__annotations__)
