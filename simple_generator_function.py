#!/usr/bin/env python


def simple_generator():
    yield "a"
    yield "b"
    yield "c"



sg = simple_generator()

for x in sg:
    print(x)

print(sg)

for i in range(5):
    for x in simple_generator():
        print(x)
print()

sg = simple_generator()
print(next(sg))
print(next(sg))
print(next(sg))
print(next(sg))
# print(next(sg))
print(next(sg))

# for i in whatever:
#     pass
#
# while True:
#     try:
#         i = next(whatever)
#     except StopIteration:
#         break
#



