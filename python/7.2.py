#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# The programs explain the situation: they can't get down. Rather, they could
# get down, if they weren't expending all of their energy trying to keep the
# tower balanced. Apparently, one program has the wrong weight, and until it's
# fixed, they're stuck here.
#
# For any program holding a disc, each program standing on that disc forms a
# sub-tower. Each of those sub-towers are supposed to be the same weight, or
# the disc itself isn't balanced. The weight of a tower is the sum of the
# weights of the programs in that tower.
#
# In the example above, this means that for ugml's disc to be balanced, gyxo,
# ebii, and jptl must all have the same weight, and they do: 61.
#
# However, for tknk to be balanced, each of the programs standing on its disc
# and all programs above it must each match. This means that the following sums
# must all be the same:
#
#    ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
#    padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
#    fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
#
# As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
# other two. Even though the nodes above ugml are balanced, ugml itself is too
# heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the
# towers balanced. If this change were made, its weight would be 60.
#
# Given that exactly one program is the wrong weight, what would its weight
# need to be to balance the entire tower?

import collections
import re
import sys


class Program(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = []
        self.total = weight


def solve(program):
    # Leaf node, ignore
    if not program.children:
        return

    # Descend depth-first into the children
    for c in program.children:
        solve(c)

    # Get all the children's total weights
    weights = [p.total for p in program.children]

    # Update my running total
    program.total += sum(weights)

    # If my children's weights aren't all the sane we have an inbalance
    counts = collections.Counter(weights)
    if len(counts) != 1:
        # Find the offending weight and delta
        bad = [x for x in counts if counts[x] == 1][0]
        good = [x for x in counts if counts[x] != 1][0]
        delta = good - bad
        # Find the offending child
        child = [x for x in program.children if x.total == bad][0]
        # Print out the new weight it should be and exit
        print child.weight + delta
        sys.exit()


def main():
    # Split input into name, weight and optional children
    inp = [[y for y in re.split(r'\W+', x) if y != ''] for x in open('7.in').readlines()]

    # Pass 1 create the programs
    programs = {}
    for line in inp:
        programs[line[0]] = Program(line[0], int(line[1]))

    # Pass 2 link them
    for line in inp:
        children = line[2:]
        if not len(children):
            continue
        for child in children:
            programs[line[0]].children.append(programs[child])
            programs[child].parent = programs[line[0]]

    # Our root is the tower with no parent
    root = programs[[x for x in programs if not programs[x].parent][0]]
    solve(root)

if __name__ == '__main__':
    main()

# vi: ts=4 et:
