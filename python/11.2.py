#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Crossing the bridge, you've barely reached the other side of the stream when
# a program comes up to you, clearly in distress. "It's my child process," she
# says, "he's gotten lost in an infinite grid!"
#
# Fortunately for her, you have plenty of experience with infinite grids.
#
# Unfortunately for you, it's a hex grid.
#
# The hexagons ("hexes") in this grid are aligned such that adjacent hexes can
# be found to the north, northeast, southeast, south, southwest, and northwest:
#
#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
#
# You have the path the child process took. Starting where he started, you need
# to determine the fewest number of steps required to reach him. (A "step"
# means to move from the hex you are in to any adjacent hex.)
#
# For example:
#
#   - ne,ne,ne is 3 steps away.
#   - ne,ne,sw,sw is 0 steps away (back where you started).
#   - ne,ne,s,s is 2 steps away (se,se).
#   - se,sw,se,sw,sw is 3 steps away (s,s,sw).


def manhattan(x, y, z):
    return (abs(x) + abs(y) + abs(z)) / 2


def main():

    # In a 3D coordinate system:
    #
    # -z  \ /  +x
    # -y --+-- +y
    # -x  / \  +z
    #
    # Each hexagon is 2 away e.g north is +x -z

    inp = open('11.in').read().strip().split(',')
    x = y = z = 0
    maximum = 0
    for direction in inp:
        if direction == 'n':
            x += 1
            z -= 1
        elif direction == 'ne':
            x += 1
            y += 1
        elif direction == 'nw':
            z -= 1
            y -= 1
        elif direction == 's':
            x -= 1
            z += 1
        elif direction == 'sw':
            x -= 1
            y -= 1
        elif direction == 'se':
            z += 1
            y += 1
        maximum = max(maximum, manhattan(x, y, z))

    print maximum


if __name__ == '__main__':
    main()

# vi: ts=4 et:
