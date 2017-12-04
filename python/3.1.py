#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# You come across an experimental new kind of memory stored on an infinite two-
# dimensional grid.
#
# Each square on the grid is allocated in a spiral pattern starting at a
# location marked 1 and then counting up while spiraling outward. For example,
# the first few squares are allocated like this:
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
#
# While this is very space-efficient (no squares are skipped), requested data
# must be carried back to square 1 (the location of the only access port for
# this memory system) by programs that can only move up, down, left, or right.
# They always take the shortest path: the Manhattan Distance between the
# location of the data and square 1.
#
# For example:
#
#   * Data from square 1 is carried 0 steps, since it's at the access port.
#   * Data from square 12 is carried 3 steps, such as: down, left, left.
#   * Data from square 23 is carried only 2 steps: up twice.
#   * Data from square 1024 must be carried 31 steps.
#
# How many steps are required to carry the data from the square identified in
# your puzzle input all the way to the access port?

INPUT=361527


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, vec):
        self.x += vec.x
        self.y += vec.y
        return self

    def __getitem__(self, index):
        if index == 0:
            return self.x
        return self.y

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)


def main():
    # Moves are right/up/left/down.  We also record the maximum extent seen in
    # that direction, when we pass this threshold we change direction
    moves = [
        {'move': Vector( 1,  0), 'extent': 0},
        {'move': Vector( 0,  1), 'extent': 0},
        {'move': Vector(-1,  0), 'extent': 0},
        {'move': Vector( 0, -1), 'extent': 0},
    ]

    # Where we are in the spiral
    position = Vector(0, 0)

    # Begin by moving right
    direction = 0

    for _ in range(2, INPUT+1):
        # Move in the specified direction
        position += moves[direction]['move']
        # Select the coordinate component in the direction of movement
        magnitude = abs(position[0 if moves[direction]['move'][0] else 1])
        # If we have passed the previous extent, update the extent and change direction
        if magnitude > moves[direction]['extent']:
            moves[direction]['extent'] = magnitude
            direction = (direction + 1) % 4
    # Answer is the manhattan distance for the INPUTth move
    print position.manhattan


if __name__ == '__main__':
    main()

# vi: ts=4 et:
