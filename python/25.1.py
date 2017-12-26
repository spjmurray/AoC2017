#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# http://adventofcode.com/2017/day/25

import collections


LEFT = -1
RIGHT = 1


def main():
    # Infinite tape modelled with a dictionary defaulting to zero
    tape = collections.defaultdict(int)
    # We could parse the input, but who the hell would bother?
    states = {
        'A': [
            {'value': 1, 'move': RIGHT, 'state': 'B'},
            {'value': 0, 'move': LEFT, 'state': 'C'},
        ],
        'B': [
            {'value': 1, 'move':  LEFT, 'state': 'A'},
            {'value': 1, 'move':  RIGHT, 'state': 'D'},
        ],
        'C': [
            {'value': 1, 'move':  RIGHT, 'state': 'A'},
            {'value': 0, 'move':  LEFT, 'state': 'E'},
        ],
        'D': [
            {'value': 1, 'move':  RIGHT, 'state': 'A'},
            {'value': 0, 'move':  RIGHT, 'state': 'B'},
        ],
        'E': [
            {'value': 1, 'move':  LEFT, 'state': 'F'},
            {'value': 1, 'move':  LEFT, 'state': 'C'},
        ],
        'F': [
            {'value': 1, 'move':  RIGHT, 'state': 'D'},
            {'value': 1, 'move':  RIGHT, 'state': 'A'},
        ],
    }
    # Start in state A
    state = 'A'
    # At position 0
    position = 0
    # Then for the required number of steps...
    for _ in xrange(0, 12173597):
        # Select the rule
        rule = states[state][tape[position]]
        # Update the symbol
        tape[position] = rule['value']
        # Update the position
        position += rule['move']
        # Finally update the rule
        state = rule['state']

    # Our answer is the number of ones on the tape
    print collections.Counter(tape.values())[1]


if __name__ == '__main__':
    main()

# vi: ts=4 et:
