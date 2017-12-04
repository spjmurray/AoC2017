#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# As a stress test on the system, the programs here clear the grid and then
# store the value 1 in square 1. Then, in the same allocation order as shown
# above, they store the sum of the values in all adjacent squares, including
# diagonals.
#
# So, the first few squares' values are chosen as follows:
#
#   * Square 1 starts with the value 1.
#   * Square 2 has only one adjacent filled square (with value 1), so it
#     also stores 1.
#   * Square 3 has both of the above squares as neighbors and stores the sum
#     of their values, 2.
#   * Square 4 has all three of the aforementioned squares as neighbors and
#     stores the sum of their values, 4.
#   * Square 5 only has the first and fourth squares as neighbors, so it gets
#     the value 5.
#
# Once a square is written, its value does not change. Therefore, the first
# few squares would receive the following values:
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
#
# What is the first value written that is larger than your puzzle input?

INPUT=361527


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def __iadd__(self, vec):
        self.x += vec.x
        self.y += vec.y
        return self

    def __getitem__(self, index):
        if index == 0:
            return self.x
        return self.y

    @property
    def key(self):
        return self.x, self.y

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)


def adjacent(position, cache):
    acc = 0
    movements = [
        Vector(-1,  1), Vector(0,  1), Vector(1,  1),
        Vector(-1,  0),                Vector(1,  0),
        Vector(-1, -1), Vector(0, -1), Vector(1, -1),
    ]
    for move in movements:
        temp = position + move
        if temp.key in cache:
            acc += cache[temp.key]
    return acc


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

    # Cache of visited nodes and their values
    cache = {Vector(0, 0).key: 1}

    # Find the first value greater than the input
    while cache[position.key] < INPUT:
        # Move in the specified direction
        position += moves[direction]['move']
        # Select the coordinate component in the direction of movement
        magnitude = abs(position[0 if moves[direction]['move'][0] else 1])
        # If we have passed the previous extent, update the extent and change direction
        if magnitude > moves[direction]['extent']:
            moves[direction]['extent'] = magnitude
            direction = (direction + 1) % 4
        # Cache the value for the position
        cache[position.key] = adjacent(position, cache)

    # Answer is the first value greater than the input
    print cache[position.key]


if __name__ == '__main__':
    main()

# vi: ts=4 et:
