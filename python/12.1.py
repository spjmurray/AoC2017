#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Walking along the memory banks of the stream, you find a small village that
# is experiencing a little confusion: some programs can't communicate with each
# other.
#
# Programs in this village communicate using a fixed system of pipes. Messages
# are passed between programs using these pipes, but most programs aren't
# connected to each other directly. Instead, programs pass messages between
# each other until the message reaches the intended recipient.
#
# For some reason, though, some of these messages aren't ever reaching their
# intended recipient, and the programs suspect that some pipes are missing.
# They would like you to investigate.
#
# You walk through the village and record the ID of each program and the IDs
# with which it can communicate directly (your puzzle input). Each program has
# one or more programs with which it can communicate, and these pipes are
# bidirectional; if 8 says it can communicate with 11, then 11 will say it can
# communicate with 8.
#
# You need to figure out how many programs are in the group that contains
# program ID 0.
#
# For example, suppose you go door-to-door like a travelling salesman and
# record the following list:
#
# 0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5
#
# In this example, the following programs are in the group that contains
# program ID 0:
#
#   - Program 0 by definition.
#   - Program 2, directly connected to program 0.
#   - Program 3 via program 2.
#   - Program 4 via program 2.
#   - Program 5 via programs 6, then 4, then 2.
#   - Program 6 via programs 4, then 2.
#
# Therefore, a total of 6 programs are in this group; all but program 1, which
# has a pipe that connects it to itself.
#
# How many programs are in the group that contains program ID 0?

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

    # Get the group containing program zero
    grp = group(inp, '0')

    # Answer is the number of programs in the seen set
    print len(grp)


if __name__ == '__main__':
    main()

# vi: ts=4 et:
