#!/usr/bin/env python


with open('foo.txt', 'w') as foo_out, open('bar.txt', 'w') as bar_out:
    pass

# vs.
with open('foo.txt', 'w') as foo_out:
    with open('bar.txt', 'w') as bar_out:
        pass

