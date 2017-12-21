#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# How many pixels stay on after 18 iterations?

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
    for _ in xrange(0, 18):
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
