#!/usr/bin/env python

cave_man = 'Fred Flintstone'
city = 'Bedrock'

x = 23.239023

print(cave_man, "lives in", city)
print("%s lives in %s" % (cave_man, city))
print(f"{cave_man:20} lives in {city:2.2s}, dude!")

#       0             1              0        1
print("{} lives in {{{}}}".format(cave_man, city))

print('{0:d} {0:x} {0:o}'.format(1234))

c2 = 'Barney Rubble'

print('{:^16s} lives in {}'.format(cave_man, city))
print('{:^16s} lives in {}'.format(c2, city))
print(f'{c2:^16s} lives in {city}')

result = 234.48034

print("result is {:.1f}".format(result))
print("result is {}".format(round(result, 1)))

huge_num = 2382093820398420398420398420
print('{:,d}'.format(huge_num))

