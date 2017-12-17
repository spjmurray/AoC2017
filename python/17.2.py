#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# The spinlock does not short-circuit. Instead, it gets more angry. At least,
# you assume that's what happened; it's spinning significantly faster than it
# was a moment ago.
#
# You have good news and bad news.
#
# The good news is that you have improved calculations for how to stop the
# spinlock. They indicate that you actually need to identify the value after 0
# in the current state of the circular buffer.
#
# The bad news is that while you were determining this, the spinlock has just
# finished inserting its fifty millionth value (50000000).
#
# What is the value after 0 the moment 50000000 is inserted?

def main():
    inp = 303

    # Mother fucker... so 50,000,000 insertions is way too much. However
    # we know that the answer after zero will always be in position 1,
    # thus keep track of where the current position would be, when we hit
    # position 1 make a note of what value would be inserted

    pos = 0
    answer = 0
    for i in xrange(1, 50000000 + 1):
        pos = ((pos + inp) % i) + 1
        if pos == 1:
            answer = i

    print answer

if __name__ == '__main__':
    main()

# vi: ts=4 et:
