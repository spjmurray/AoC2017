#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#

import itertools

def main():
    a = 277
    b = 349
    c = 0
    for _ in range(0, 40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if (a ^ b) & 0xffff == 0:
            c += 1
    print c
        


if __name__ == '__main__':
    main()

# vi: ts=4 et:
