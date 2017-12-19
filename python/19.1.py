#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Somehow, a network packet got lost and ended up here. It's trying to follow a
# routing diagram (your puzzle input), but it's confused about where to go.
#
# Its starting point is just off the top of the diagram. Lines (drawn with |,
# -, and +) show the path it needs to take, starting by going down onto the
# only line connected to the top of the diagram. It needs to follow this path
# until it reaches the end (located somewhere within the diagram) and stop
# there.
#
# Sometimes, the lines cross over each other; in these cases, it needs to
# continue going the same direction, and only turn left or right when there's
# no other option. In addition, someone has left letters on the line; these
# also don't change its direction, but it can use them to keep track of where
# it's been. For example:
#
#     |          
#     |  +--+    
#     A  |  C    
# F---|----E|--+ 
#     |  |  |  D 
#     +B-+  +--+ 
#
# Given this diagram, the packet needs to take the following path:
#
#   - Starting at the only line touching the top of the diagram, it must go
#     down, pass through A, and continue onward to the first +.
#   - Travel right, up, and right, passing through B in the process.
#   - Continue down (collecting C), right, and up (collecting D).
#   - Finally, go all the way left through E and stopping at F.
#
# Following the path to the end, the letters it sees on its path are ABCDEF.
#
# The little packet looks up at you, hoping you can help it find the way. What
# letters will it see (in the order it would see them) if it follows the path?
# (The routing diagram is very wide; make sure you view it without line
# wrapping.)

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

    while True:
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

    # Answer is the path taken
    print ''.join(path)


if __name__ == '__main__':
    main()

# vi: ts=4 et:
