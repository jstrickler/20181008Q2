#!/usr/bin/env python
import sys
import os

print(sys.prefix)

for mod, details in sorted(sys.modules.items()):
    print(mod, str(details)[:60])

import re


print(sys.modules['re'].search(r'^abc', 'abcdef'))


print(sys.modules['re'], '\n')

print(sys.version)
print(sys.version_info)
print()

for path in sys.path:
    print(path)

print(sys.platform)


print(dir(sys))
print()

# sys.stdin  sys.stdout  sys.stderr

os.system("netstat -an")

with os.popen("netstat -an") as netstat_in:
    for line in netstat_in:
        if "ESTAB" in line:
            print(line, end='')







