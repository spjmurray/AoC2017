#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# Now, it's time to fix the problem.
#
# The debug mode switch is wired directly to register a. You flip the switch,
# which makes register a now start at 1 when the program is executed.
#
# Immediately, the coprocessor begins to overheat. Whoever wrote this program
# obviously didn't choose a very efficient implementation. You'll need to
# optimize the program if it has any hope of completing before Santa needs that
# printer working.
#
# The coprocessor's ultimate goal is to determine the final value left in
# register h once the program completes. Technically, if it had that... it
# wouldn't even need to run the program.
#
# After setting register a to 1, if the program were to run to completion, what
# value would be left in register h?
#
# -----------------
#
# Decompiling the assembler into a HLL looks like the following
#
# b = c = 57
# if a != 0:
#     b = 105700
#     c = 122700
# while True:
#     f = True
#     for d in range(2, b):
#         for e in range(2, b):
#             if d * e == b:
#                 f = False
#     if not f:
#         h += 1
#     if b == c:
#         break
#     b += 17
#
# In essence we are looking for numbers between 105700 and 122700 wth a step of
# 17 which have some pair of factors which aren't one or itself e.g. are non-
# prime


def prime(x):
  if x <= 1:
    return False
  elif x <= 3:
    return True
  elif (x % 2) == 0 or (x % 3) == 0:
    return False
  i = 5
  while (i * i) <= x:
    if (x % i) == 0 or (x % (i + 2)) == 0:
      return False
    i += 6
  return True


def main():
    print len(list(x for x in xrange(105700, 122700 + 1, 17) if not prime(x)))


if __name__ == '__main__':
    main()

# vi: ts=4 et:
