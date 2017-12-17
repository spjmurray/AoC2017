#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# You come upon a very unusual sight; a group of programs here appear to be
# dancing.
#
# There are sixteen programs in total, named a through p. They start by
# standing in a line: a stands in position 0, b stands in position 1, and so on
# until p, which stands in position 15.
#
# The programs' dance consists of a sequence of dance moves:
#
#   - Spin, written sX, makes X programs move from the end to the front, but
#     maintain their order otherwise. (For example, s3 on abcde produces cdeab).
#   - Exchange, written xA/B, makes the programs at positions A and B swap
#     places.
#   - Partner, written pA/B, makes the programs named A and B swap places.
#
# For example, with only five programs standing in a line (abcde), they could
# do the following dance:
#
#   - s1, a spin of size 1: eabcd.
#   - x3/4, swapping the last two programs: eabdc.
#   - pe/b, swapping programs e and b: baedc.
#
# After finishing their dance, the programs end up in order baedc.
#
# You watch the dance for a while and record their dance moves (your puzzle
# input). In what order are the programs standing after their dance?

def swap(ary, a, b):
    t = ary[a]
    ary[a] = ary[b]
    ary[b] = t
   

def main():
    inp = open('16.in').read().strip().split(',')
    dancers = [chr(ord('a') + x) for x in range(0,  16)]
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
            
    print ''.join(dancers)


if __name__ == '__main__':
    main()

# vi: ts=4 et:
