#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Now, you're ready to remove the garbage.
#
# To prove you've removed it, you need to count all of the characters within
# the garbage. The leading and trailing < and > don't count, nor do any
# canceled characters or the ! doing the canceling.
#
#   - <>, 0 characters.
#   - <random characters>, 17 characters.
#   - <<<<>, 3 characters.
#   - <{!>}>, 2 characters.
#   - <!!>, 0 characters.
#   - <!!!>>, 0 characters.
#   - <{o"i!a,<{i<a>, 10 characters.
#
# How many non-canceled characters are within the garbage in your puzzle input?

def main():
    inp = open('9.in').read().strip()

    ip = 0
    count = 0
    garbage = False
    while ip < len(inp):
        inst = inp[ip]
        if not garbage:
            if inst == '{':
                pass
            elif inst == '}':
                pass
            elif inst == ',':
                pass
            elif inst == '<':
                garbage = True
            else:
                raise RuntimeError(inst)
        else:
            if inst == '>':
                garbage = False
            elif inst == '!':
                ip += 1
            else:
                count += 1
        ip += 1
    print count


if __name__ == '__main__':
    main()

# vi: ts=4 et:
