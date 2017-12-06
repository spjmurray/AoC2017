#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Out of curiosity, the debugger would also like to know the size of the loop:
# starting from a state that has already been seen, how many block
# redistribution cycles must be performed before that same state is seen again?
#
# In the example above, 2 4 1 2 is seen again after four cycles, and so the
# answer in that example would be 4.
#
# How many cycles are in the infinite loop that arises from the configuration
# in your puzzle input?

import itertools

INPUT = '4    1   15  12  0   9   9   5   5   8   7   3   14  5   12  3'


def main():
    # Input is a list of integers
    inp = [int(x) for x in INPUT.split()]
    # Maintain a set of seen states, and when they were seen
    seen = dict()
    # And maintain the step count
    for count in itertools.count():
        # Break if we have seen this state before
        if tuple(inp) in seen:
            break
        seen[tuple(inp)] = count
        # Find the first largest bucket index
        index = inp.index(max(inp))
        # Note how big it is and zero it
        num = inp[index]
        inp[index] = 0
        # Redistribute the data starting with the next
        # index
        index += 1
        for i in range(0, num):
            inp[(index + i) % len(inp)] += 1
    # Answer is the difference in steps between first seeing
    # it and second seeing it
    print count - seen[tuple(inp)]


if __name__ == '__main__':
    main()

# vi: ts=4 et:
