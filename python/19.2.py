#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# The packet is curious how many steps it needs to go.
#
# For example, using the same routing diagram from the example above...
#
#     |          
#     |  +--+    
#     A  |  C    
# F---|--|-E---+ 
#     |  |  |  D 
#     +B-+  +--+ 
#
# ...the packet would go:
#
#   - 6 steps down (including the first line at the top of the diagram).
#   - 3 steps right.
#   - 4 steps up.
#   - 3 steps right.
#   - 4 steps down.
#   - 3 steps right.
#   - 2 steps up.
#   - 13 steps left (including the F it stops on).
#
# This would result in a total of 38 steps.
#
# How many steps does the packet need to go?

import itertools

def main():
    # Load the input into a 2D grid, happily it already has sentinels
    grid = open('19.in').readlines()

    # Fin the entry coordinate
    for i in range(0, len(grid[0])):
        if grid[0][i] == '|':
            x = i
            y = 0
            break

    # Note the path taken
    path = []

    # Initial direction is down
    dx = 0
    dy = 1

    for count in itertools.count(0):
        # We terminate on an ASCII character, and assume the next step will
        # be blank
        if grid[y][x] == ' ':
            break

        # At a junction alter direction
        if grid[y][x] == '+':
            # We can go up, down, left or right, however we cannot jump onto a path
            # perpendicular to the direction of movement, we class these as illegal moves
            for ddx, ddy, ill in [(0, 1, '-'), (0, -1, '-'), (1, 0, '|'), (-1, 0, '|')]:
                # Don't go the way we came
                if ddx == -dx and ddy == -dy:
                    continue
                tx = x + ddx
                ty = y + ddy
                # Don't jump to another junction, an empty space or perpendicular path
                if grid[ty][tx] in ['+', ' ', ill]:
                    continue
                # Update the direction of travel and escape
                dx = ddx 
                dy = ddy 
                break

        x = x + dx
        y = y + dy

        # If we encounter an ASCII character append to our path
        if grid[y][x] in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
            path.append(grid[y][x])

    # Answer is the steps taken
    print count


if __name__ == '__main__':
    main()

# vi: ts=4 et:
