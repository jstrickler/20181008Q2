#!/usr/bin/env python


def make_dash_printer(num_dashes):

    def _():
        print('-' * num_dashes)

    return _


d1 = make_dash_printer(5)

d2 = make_dash_printer(10)

d1()
d2()

