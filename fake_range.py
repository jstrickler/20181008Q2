#!/usr/bin/env python


def main():
    fr = FakeRange(1, 10)

    # iterator = iter(fr)
    # print(iterator)
    # for n in iterator:
    #     print(n)


    for i in FakeRange(1, 11):
        print(i)


    fr = FakeRange(1, 4)
    print(next(fr))
    print(next(fr))


class FakeRange():

    def __init__(self, start, stop):
        self._start = start
        self._stop = stop

    def __iter__(self):
        return self # the iterator


    def __next__(self):
        return_val = self._start
        if self._start >= self._stop:
            raise StopIteration

        self._start += 1
        return return_val


if __name__ == '__main__':  # if running, not importing

    main()

