#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# There are more programs than just the ones in the group containing program ID
# 0. The rest of them have no way of reaching that group, and still might have
# no way of reaching each other.
#
# A group is a collection of programs that can all communicate via pipes either
# directly or indirectly. The programs you identified just a moment ago are all
# part of the same group. Now, they would like you to determine the total
# number of groups.
#
# In the example above, there were 2 groups: one consisting of programs
# 0,2,3,4,5,6, and the other consisting solely of program 1.
#
# How many groups are there in total?

import itertools


def group(inp, program):
    # Start with the selected program, and enqueue any peers
    queue = [program]

    # Maintain a cache of programs seen so we don't revisit or end in a loop
    seen = set()
    seen.add(program)

    # Iteratively expand the group
    while queue:
        # Dequeue a program for analysis
        t = queue.pop(0)

        # Case 1: peers in t (fast)
        for peer in inp[t]:
            if peer not in seen:
                queue.append(peer)
                seen.add(peer)

        # Case 2: t in peers (sloooow)
        for prog in inp:
            if t in inp[prog]:
                if prog not in seen:
                    queue.append(prog)
                    seen.add(prog)

    return seen


def main():
    # Map from input to a hash of program and peers
    inp = [x.strip().split(None, 2) for x in open('12.in').readlines()]
    inp = {x[0]: x[2].split(', ') for x in inp}

    # Count the number of groups we see
    for groups in itertools.count():
        # Break when there is no input left to consume
        if not inp:
            break

        # Get an abitrary group
        grp = group(inp, inp.keys()[0])

        # Remove seen programs in the group from the input
        for member in grp:
            del inp[member]

    # Answer is the number of groups seen
    print groups


if __name__ == '__main__':
    main()

# vi: ts=4 et:
