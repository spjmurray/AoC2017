#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Now, the jumps are even stranger: after each jump, if the offset was three or
# more, instead decrease it by 1. Otherwise, increase it by 1 as before.
#
# Using this rule with the above example, the process now takes 10 steps, and
# the offset values after finding the exit are left as 2 3 2 3 -1.
#
# How many steps does it now take to reach the exit?

import itertools


def main():
    # Load the instruction stream as a list of integers
    inp = [int(x) for x in open('5.in').readlines()]
    # Start at instruction zero
    ip = 0
    try:
        # Remember the number of steps, this is our answer
        for steps in itertools.count():
            # Calculate the next IP
            nip = ip + inp[ip]
            # Increment/decrement the jump target
            inp[ip] += -1 if inp[ip] >= 3 else 1
            # And move
            ip = nip
    except IndexError:
        # Catch the exit condition and print the answer
        print steps


if __name__ == '__main__':
    main()

# vi: ts=4 et:
