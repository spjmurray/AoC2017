#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Suddenly, a scheduled job activates the system's disk defragmenter. Were the
# situation different, you might sit and watch it for a while, but today, you
# just don't have that kind of time. It's soaking up valuable system resources
# that are needed elsewhere, and so the only option is to help it finish its
# task as soon as possible.
#
# The disk in question consists of a 128x128 grid; each square of the grid is
# either free or used. On this disk, the state of the grid is tracked by the
# bits in a sequence of knot hashes.
#
# A total of 128 knot hashes are calculated, each corresponding to a single row
# in the grid; each hash contains 128 bits which correspond to individual grid
# squares. Each bit of a hash indicates whether that square is free (0) or used
# (1).
#
# The hash inputs are a key string (your puzzle input), a dash, and a number
# from 0 to 127 corresponding to the row. For example, if your key string were
# flqrgnkx, then the first row would be given by the bits of the knot hash of
# flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and
# so on until the last row, flqrgnkx-127.
#
# The output of a knot hash is traditionally represented by 32 hexadecimal
# digits; each of these digits correspond to 4 bits, for a total of 4 * 32 =
# 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent
# binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110,
# f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal
# would begin with 10100000110000100000000101110000... in binary.
#
# Continuing this process, the first 8 rows and columns for key flqrgnkx appear
# as follows, using # to denote used squares, and . to denote free ones:
#
# ##.#.#..-->
# .#.#.#.#   
# ....#.#.   
# #.#.##.#   
# .##.#...   
# ##..#..#   
# .#...#..   
# ##.#.##.-->
# |      |   
# V      V   
#
# In this example, 8108 squares are used across the entire 128x128 grid.
#
# Given your actual key string, how many squares are used?

import collections

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
    answer = 0
    for i in range(0, 128):
        binary = hex2bin(knot_hash('{}-{}'.format(INPUT, i)))
        answer += collections.Counter(binary)['1']
    print answer


if __name__ == '__main__':
    main()

# vi: ts=4 et:
