#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# To be safe, the CPU also needs to know the highest value held in any register
# during this process so that it can decide how much memory to allocate to
# these operations. For example, in the above instructions, the highest value
# ever held was 10 (in register c after the third instruction was evaluated).

import collections
import operator

# Map assembly operations to actual functions
OPERATORS = {
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    'inc': operator.add,
    'dec': operator.sub,
}


def main():
    # Load each instruction
    inp = open('8.in').readlines()
    # We don't know the register set, but they default to zero, defaultdict
    # is our friend
    registers = collections.defaultdict(int)
    # Record the maximum value seen ever
    highest = 0
    # For every instruction move onwards, no jumps :)
    for inst in inp:
        # Unpack the instruction and predicate
        reg, op, imm, _, pred_reg, pred_op, pred_imm = inst.split()
        # If the predicate fails move on
        if not OPERATORS[pred_op](registers[pred_reg], int(pred_imm)):
            continue
        # Perform the main operation
        registers[reg] = OPERATORS[op](registers[reg], int(imm))
        # Is this new value the largest?
        highest = max(highest, registers[reg])
    # Result is the largest ever seen
    print highest


if __name__ == '__main__':
    main()

# vi: ts=4 et:
