#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# http://adventofcode.com/2017/day/13

import itertools


# The scanner will be in position zero at time (depth * 2) - 2).  If we are
# there then we have been caught
def caught(time, depth):
    return time % ((depth * 2) - 2) == 0


def main():
    # Map of firewall level to scan depth
    inp = [[int(y) for y in x.split(': ')] for x in open('13.in')]

    # For each delay until infinity
    for delay in itertools.count():
        for index, depth in inp:
            if caught(index + delay, depth):
                break
        else:
            break

    # Answer is the delay where we don't get caught
    print delay


if __name__ == '__main__':
    main()

# vi: ts=4 et:
