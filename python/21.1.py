#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# You find a program trying to generate some art. It uses a strange process
# that involves repeatedly enhancing the detail of an image through a set of
# rules.
#
# The image consists of a two-dimensional square grid of pixels that are either
# on (#) or off (.). The program always begins with this pattern:
#
# .#.
# ..#
# ###
#
# Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to
# have a size of 3.
#
# Then, the program repeats the following process:
#
#   - If the size is evenly divisible by 2, break the pixels up into 2x2
#     squares, and convert each 2x2 square into a 3x3 square by following the
#     corresponding enhancement rule.
#   - Otherwise, the size is evenly divisible by 3; break the pixels up into
#     3x3 squares, and convert each 3x3 square into a 4x4 square by following
#     the corresponding enhancement rule.
#
# Because each square of pixels is replaced by a larger one, the image gains
# pixels and so its size increases.

# The artist's book of enhancement rules is nearby (your puzzle input);
# however, it seems to be missing rules. The artist explains that sometimes,
# one must rotate or flip the input pattern to find a match. (Never rotate or
# flip the output pattern, though.) Each pattern is written concisely: rows are
# listed as single units, ordered top-down, and separated by slashes. For
# example, the following rules correspond to the adjacent patterns:
#
# ../.#  =  ..
#           .#
#
#                 .#.
# .#./..#/###  =  ..#
#                 ###
#
#                         #..#
# #..#/..../#..#/.##.  =  ....
#                         #..#
#                         .##.
#
# When searching for a rule to use, rotate and flip the pattern as necessary.
# For example, all of the following patterns match the same rule:
#
# .#.   .#.   #..   ###
# ..#   #..   #.#   ..#
# ###   ###   ##.   .#.
#
# Suppose the book contained the following two rules:
#
# ../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#
#
# As before, the program begins with this pattern:
#
# .#.
# ..#
# ###
#
# The size of the grid (3) is not divisible by 2, but it is divisible by 3. It
# divides evenly into a single square; the square matches the second rule,
# which produces:
#
# #..#
# ....
# ....
# #..#
#
# The size of this enhanced grid (4) is evenly divisible by 2, so that rule is
# used. It divides evenly into four squares:
#
# #.|.#
# ..|..
# --+--
# ..|..
# #.|.#
#
# Each of these squares matches the same rule (../.# => ##./#../...), three of
# which require some flipping and rotation to line up with the rule. The output
# for the rule is the same in all four cases:
#
# ##.|##.
# #..|#..
# ...|...
# ---+---
# ##.|##.
# #..|#..
# ...|...
#
# Finally, the squares are joined into a new grid:
#
# ##.##.
# #..#..
# ......
# ##.##.
# #..#..
# ......
#
# Thus, after 2 iterations, the grid contains 12 pixels that are on.
#
# How many pixels stay on after 5 iterations?

import collections


class Transformer(object):
    """
    Takes the input and creates all possible orientations from the source
    to the destination.  Thus each transform in the main loop is a log(n)
    string compare to get the required result
    """

    def __init__(self):
        self.cache = {}
        for line in open('21.in'):
            inp, _, out = line.strip().split()
            src1 = inp.split('/')
            src2 = self.flip(src1)
            dest = out.split('/')
            self.cache[''.join(src1)] = dest
            self.cache[''.join(src2)] = dest
            for _ in xrange(0, 3):
                src1 = self.rotate(src1)
                src2 = self.rotate(src2)
                self.cache[''.join(src1)] = dest
                self.cache[''.join(src2)] = dest

    @staticmethod
    def rotate(block):
        n = len(block)
        out = []
        for x in xrange(n-1, -1, -1):
            row = []
            for y in xrange(0, n):
                row.append(block[y][x])
            out.append(''.join(row))
        return out

    @staticmethod
    def flip(block):
        out = []
        for i in xrange(0, len(block)):
            out.append(''.join(reversed(block[i])))
        return out

    def transform(self, inp):
        return self.cache[''.join(inp)]


def main():
    transformer = Transformer()

    image = [
        '.#.',
        '..#',
        '###',
    ]

    # For the required number of iterations ...
    for _ in xrange(0, 5):
        new_image = []
        # If the size if divisible by 2 process as 2x2 blocks, else 3x3
        step = 2 if len(image) % 2 == 0 else 3
        # Calculate the number of blocks to process in each axis
        blocks = len(image) / step
        # For each row of blocks...
        for y in xrange(0, len(image), step):
            # Add in a new blank string for each output e.g. one larger than the step
            for _ in xrange(0, step + 1):
                new_image.append('')
            # For each block in the row
            for x in xrange(0, len(image), step):
                # Extract the block
                block = []
                for i in xrange(0, step):
                    block.append(image[y+i][x:x+step])
                # Transform into its new configuration
                new_block = transformer.transform(block)
                # And commit it into the correct location in the new image
                dst_y = (y / step) * (step + 1)
                for i in xrange(0, step + 1):
                    new_image[dst_y + i] += new_block[i]
        # Update the image
        image = new_image

    # Answer is the number of coordinates which are 'on' e.g. a hash
    print collections.Counter(''.join(image))['#']


if __name__ == '__main__':
    main()

# vi: ts=4 et:
