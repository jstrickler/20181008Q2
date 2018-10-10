#!/usr/bin/env python
import traceback
import sys

class Q2Exception(Exception): pass

try:
    m_value = 23.9

    test_values = [8.3, 5.3, 9.8, 12, 0, 15.4, 'abc', 9.7]

    for tv in test_values:
        try:
            result = m_value / tv
        except ZeroDivisionError as err:
            print("OOPS:", err)
    #        print(traceback.format_exc())
    #         traceback.print_exc()
        except (TypeError, ValueError) as err:
            print("Uh-oh:", err, file=sys.stderr)
            # exit()
        except Exception:
            print("We're doomed", file=sys.stderr)
        else:
            print(f"Result is {result}")
            # print(..., file=sys.stdout, flush=False, end='\n', sep=' ')
        finally:
            print("OK")

except Exception as err:
    print(err)  # and log it


try:
    raise TypeError("Dude -- it should be a float!", 5.2, 'wombat')
except TypeError as err:
    print(err)
    print(err.args[1])





