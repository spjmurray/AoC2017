#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Now that you're starting to get a feel for the dance moves, you turn your
# attention to the dance as a whole.
#
# Keeping the positions they ended up in from their previous dance, the
# programs perform it again and again: including the first dance, a total of
# one billion (1000000000) times.
#
# In the example above, their second dance would begin with the order baedc,
# and use the same dance moves:
#
#   - s1, a spin of size 1: cbaed.
#   - x3/4, swapping the last two programs: cbade.
#   - pe/b, swapping programs e and b: ceadb.
#
# In what order are the programs standing after their billion dances?

import itertools
import copy

def swap(ary, a, b):
    t = ary[a]
    ary[a] = ary[b]
    ary[b] = t


def dance(dancers, inp):
    for i in inp:
        if i[0] == 's':
            t = int(i[1:])
            dancers = dancers[-t:] + dancers[:-t]
        elif i[0] == 'x':
            x, y = [int(t) for t in i[1:].split('/')]
            swap(dancers, x, y)
        else:
            x = dancers.index(i[1])
            y = dancers.index(i[3])
            swap(dancers, x, y)
    return dancers


def d2s(dancers):
    return ''.join(dancers)


def main():
    inp = open('16.in').read().strip().split(',')
    dancers = [chr(ord('a') + x) for x in range(0,  16)]
    start = d2s(copy.copy(dancers))

    # 1,000,000,000 you say, lets assume there is a cycle and
    # we can just do a fraction of the calculation
    rounds = [d2s(dancers)]
    for count in itertools.count(1):
        dancers = dance(dancers, inp)
        key = d2s(dancers)
        rounds.append(key)
        if key == start:
            break

    print rounds[1000000000 % count]


if __name__ == '__main__':
    main()

# vi: ts=4 et:
