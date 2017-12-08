#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# You receive a signal directly from the CPU. Because of your recent assistance
# with jump instructions, it would like you to compute the result of a series
# of unusual register instructions.
#
# Each instruction consists of several parts: the register to modify, whether
# to increase or decrease that register's value, the amount by which to
# increase or decrease it, and a condition. If the condition fails, skip the
# instruction without modifying the register. The registers all start at 0. The
# instructions look like this:
#
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
#
# These instructions would be processed as follows:
#
#   * Because a starts at 0, it is not greater than 1, and so b is not
#     modified.
#   * a is increased by 1 (to 1) because b is less than 5 (it is 0).
#   * c is decreased by -10 (to 10) because a is now greater than or equal to 1
#     (it is 1).
#   * c is increased by -20 (to -10) because c is equal to 10.
#
# After this process, the largest value in any register is 1.
#
# You might also encounter <= (less than or equal to) or != (not equal to).
# However, the CPU doesn't have the bandwidth to tell you what all the
# registers are named, and leaves that to you to determine.
#
# What is the largest value in any register after completing the instructions
# in your puzzle input?

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
    # For every instruction move onwards, no jumps :)
    for inst in inp:
        # Unpack the instruction and predicate
        reg, op, imm, _, pred_reg, pred_op, pred_imm = inst.split()
        # If the predicate fails move on
        if not OPERATORS[pred_op](registers[pred_reg], int(pred_imm)):
            continue
        # Perform the main operation
        registers[reg] = OPERATORS[op](registers[reg], int(imm))
    # Result is the largest value
    print max(registers.values())


if __name__ == '__main__':
    main()

# vi: ts=4 et:
