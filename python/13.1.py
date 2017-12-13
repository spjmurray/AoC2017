#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# http://adventofcode.com/2017/day/13

# The scanner will be in position zero at time (depth * 2) - 2).  If we are
# there then we have been caught
def caught(time, depth):
    return time % ((depth * 2) - 2) == 0


def main():
    # Map of firewall level to scan depth
    inp = [[int(y) for y in x.split(': ')] for x in open('13.in')]

    # Answer is the sum of the product of index and depth if we are caught
    print sum(index * depth for index, depth in inp if caught(index, depth))


if __name__ == '__main__':
    main()

# vi: ts=4 et:
