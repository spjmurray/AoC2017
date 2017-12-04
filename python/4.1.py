#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# A new system policy has been put in place that requires all accounts to use a
# passphrase instead of simply a password. A passphrase consists of a series of
# words (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
#
#   * aa bb cc dd ee is valid.
#   * aa bb cc dd aa is not valid - the word aa appears more than once.
#   * aa bb cc dd aaa is valid - aa and aaa count as different words.
#
# The system's full passphrase list is available as your puzzle input. How many
# passphrases are valid?

def valid(phrase):
    dictionary = set()
    for word in phrase:
        if word in dictionary:
            return False
        dictionary.add(word)
    return True


def main():
    inp = [x.split() for x in open('4.in').read().strip().split("\n")]
    print len([x for x in inp if valid(x)])


if __name__ == '__main__':
    main()

# vi: ts=4 et:
