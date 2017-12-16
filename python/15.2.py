#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#

def main():
    a = 277
    b = 349
    qa = []
    qb = []
    pairs = 5000000
    while True:
        a = (a * 16807) % 2147483647
        if a % 4 == 0:
            qa.append(a)
        b = (b * 48271) % 2147483647
        if b % 8 == 0:
            qb.append(b)
        if len(qa) >= pairs and len(qb) >= pairs:
            break
    c = 0
    for i in range(0, pairs):
        if (qa[i] ^ qb[i]) & 0xffff == 0:
            c += 1
    print c


if __name__ == '__main__':
    main()

# vi: ts=4 et:
