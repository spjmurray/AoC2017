#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# For added security, yet another system policy has been put in place. Now, a
# valid passphrase must contain no two words that are anagrams of each other -
# that is, a passphrase is invalid if any word's letters can be rearranged to
# form any other word in the passphrase.
#
# For example:
#
#   * abcde fghij is a valid passphrase.
#   * abcde xyz ecdab is not valid - the letters from the third word can be
#     rearranged to form the first word.
#   * a ab abc abd abf abj is a valid passphrase, because all letters need to
#     be used when forming another word.
#   * iiii oiii ooii oooi oooo is valid.
#   * oiii ioii iioi iiio is not valid - any of these words can be rearranged
#     to form any other word.
#
# Under this new system policy, how many passphrases are valid?

import collections
import itertools


def anagram(a, b):
    return collections.Counter(a) == collections.Counter(b)


def valid(phrase):
    return not any(anagram(x, y) for x, y in itertools.permutations(phrase, 2))


def main():
    inp = [x.split() for x in open('4.in').read().strip().split("\n")]
    print len([x for x in inp if valid(x)])


if __name__ == '__main__':
    main()

# vi: ts=4 et:
