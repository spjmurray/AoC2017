#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# http://adventofcode.com/2017/day/22

import collections

# Node states
CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

def main():
    # Load the input and calulate its dimensions
    inp = [x.strip() for x in open('22.in')]
    height = len(inp)
    width = len(inp[0])

    # Load the input into a grid, modelled on a default dictionary
    # whose keys are x, y coordinates
    grid = collections.defaultdict(int)
    for y in xrange(0, height):
        for x in xrange(0, width):
            grid[(x-width/2, -(y-height/2))] = CLEAN if inp[y][x] == '.' else INFECTED

    # Set of directions, +1 clockwise (right), -1 anti-clockwise (left)
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    # Map from state to movement
    moves = [-1, 0, 1, 2]

    # Keep tab on the infections we make
    infections = 0

    # Start in the moddle of the grid facing up
    x = 0
    y = 0
    d = 0

    for _ in xrange(0, 10000000):
        # If the node is flagged turn around, infected turn right, clean left
        d = (d + moves[grid[(x, y)]]) % 4
        # Weaken, infect, flag or clean the node
        grid[(x, y)] = (grid[(x, y)] + 1) % 4
        # If infected increment our counter
        if grid[(x, y)] == INFECTED:
            infections += 1
        # Move in the direction we are facing
        x += directions[d][0]
        y += directions[d][1]

    # Answer is the number of infections
    print infections


if __name__ == '__main__':
    main()

# vi: ts=4 et:
