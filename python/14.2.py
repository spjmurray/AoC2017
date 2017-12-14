#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Now, all the defragmenter needs to know is the number of regions. A region is
# a group of used squares that are all adjacent, not including diagonals. Every
# used square is in exactly one region: lone used squares form their own
# isolated regions, while several adjacent squares all count as a single
# region.
#
# In the example above, the following nine regions are visible, each marked
# with a distinct digit:
#
# 11.2.3..-->
# .1.2.3.4   
# ....5.6.   
# 7.8.55.9   
# .88.5...   
# 88..5..8   
# .8...8..   
# 88.8.88.-->
# |      |   
# V      V   
#
# Of particular interest is the region marked 8; while it does not appear
# contiguous in this small view, all of the squares marked 8 are connected when
# considering the whole 128x128 grid. In total, in this example, 1242 regions
# are present.
#
# How many regions are present given your key string?

INPUT='amgozmfv'

def knot_hash_round(string, inp, position, skip):
    for length in inp:
        # Extract at most length elements from position
        subset = string[position:position+length]
        # If we've overflowed extract from the beginning
        if len(subset) < length:
            subset += string[0:length-len(subset)]
        # Reverse our subset
        subset = list(reversed(subset))
        # And finally overwrite the subset in the original string
        for i in range(0, length):
            ptr = (position + i) % len(string)
            string[ptr] = subset[i]
        # Update the position watching for overflow
        position = (position + length + skip) % len(string)
        # And increase the skip size
        skip += 1
    return position, skip


def dense_hash(string):
    # Split into groups for 16
    groups = [string[x:x+16] for x in range(0, len(string), 16)]
    # And XOR them together
    return [reduce(lambda a, b: a ^ b, x, 0) for x in groups]


def knot_hash(inp):
    inp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]

    string = range(0, 256)
    position = skip = 0
    for _ in range(0, 64):
        position, skip = knot_hash_round(string, inp, position, skip)
    dense = dense_hash(string)

    return ''.join('{:02x}'.format(x) for x in dense)


def hex2bin(value):
    conv = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111',
    }
    return ''.join(conv[x] for x in value)


def main():
    # Start with a grid X+2 x Y+2 (e.g. surrounded by sentinels)
    X = 128
    Y = 128
    grid = []
    for _ in range(0, Y+2):
        grid.append((X+2) * [0])

    for y in range(0, 128):
        # Calculate the row hash in binary
        binary = hex2bin(knot_hash('{}-{}'.format(INPUT, y)))
        # Update the grid, use -1 as unvisited as we will color based on group
        # number in a second...
        for x in range(0, 128):
            grid[y+1][x+1] = 0 if binary[x] == '0' else -1

    # The main problem, given the grid, how many blocks exist which consist of
    # contiguous nodes in a the vertical and horizonal planes.  We iterate over
    # the grid taking into account the sentinels...
    group = 0
    for y in range(1, Y+1):
        for x in range(1, X+1):
            # Ignore anything we haven't visited
            if grid[y][x] != -1:
                continue
            # The fun bit, based on Dijkstra/A* depth first searches we are going
            # to color contiguous blocks
            group += 1
            queue = [(x, y)]
            seen = set()
            while queue:
                # Pop the closest node to the source and colour it in
                node = queue.pop(0)
                grid[node[1]][node[0]] = group
                # Next move N,S,E,W pushing valid coordinates onto the queue
                for move in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    tx = node[0] + move[0]
                    ty = node[1] + move[1]
                    if grid[ty][tx] != -1:
                        continue
                    coord = (tx, ty)
                    if coord in seen:
                        continue
                    queue.append(coord)
                    seen.add(coord)

    print group


if __name__ == '__main__':
    main()

# vi: ts=4 et:
