#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# The bridge you've built isn't long enough; you can't jump the rest of the
# way.
#
# In the example above, there are two longest bridges:
#
#    0/2--2/2--2/3--3/4
#    0/2--2/2--2/3--3/5
#
# Of them, the one which uses the 3/5 component is stronger; its strength is
# 0+2 + 2+2 + 2+3 + 3+5 = 19.
#
# What is the strength of the longest bridge you can make? If you can make
# multiple bridges of the longest length, pick the strongest one.

import collections
import copy


def solve(edges, conn, strength, strengths):
    # For each edge in the list
    for a, b in edges:
        # Not a match fail fast
        if a != conn and b != conn:
            continue
        # Caclualte the new strength
        new_strength = strength + a + b
        # Calculate the next connector to look for
        next_conn = b if a == conn else a
        # Recursively descend
        new_edges = copy.copy(edges)
        new_edges.remove((a, b))
        solve(new_edges, next_conn, new_strength, strengths)
    # No new edges found, add the strength to the map
    else:
        strengths[len(edges)].append(strength)


def main():
    edges = []
    for line in open('24.in'):
        a, b = [int(x) for x in line.split('/')]
        edges.append((a, b))

    # This records the remaining edge length to strength
    strengths = collections.defaultdict(list)
    solve(edges, 0, 0, strengths)
    # Answer is the largest strength of the longest path
    # (or in this case the minimum path remainder)
    print max(strengths[min(strengths)])


if __name__ == '__main__':
    main()

# vi: ts=4 et:
