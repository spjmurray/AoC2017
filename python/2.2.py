#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# "Great work; looks like we're on the right track after all. Here's a star for
# your effort." However, the program seems a little worried. Can programs be
# worried?
#
# "Based on what we're seeing, it looks like all the User wanted is some
# information about the evenly divisible values in the spreadsheet.
# Unfortunately, none of us are equipped for that kind of calculation - most of
# us specialize in bitwise operations."
#
# It sounds like the goal is to find the only two numbers in each row where one
# evenly divides the other - that is, where the result of the division
# operation is a whole number. They would like you to find those numbers on each
# line, divide them, and add up each line's result.
#
# For example, given the following spreadsheet:
#
# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
#
#  * In the first row, the only two numbers that evenly divide are 8 and 2; the
#    result of this division is 4.
#  * In the second row, the two numbers are 9 and 3; the result is 3.
#  * In the third row, the result is 2.
#
# In this example, the sum of the results would be 4 + 3 + 2 = 9.
#
# What is the sum of each row's result in your puzzle input?

INPUT="""1236   741 557 1029    144 101 1968    2159    1399    80  1139    1167    1695    82  90  2236
2134    106 107 1025    584 619 191 496 80  352 351 2267    1983    1973    97  1244
3227    179 691 3177    172 1636    3781    2020    3339    2337    189 3516    1500    176 159 3279
201 688 364 180 586 659 623 577 188 265 403 670 195 720 115 37
1892    1664    2737    2676    849 2514    923 171 311 218 255 2787    1271    188 1278    2834
150 3276    204 603 3130    587 3363    3306    2890    127 176 174 383 3309    213 1620
5903    3686    200 230 6040    4675    6266    179 5375    1069    283 82  6210    6626    6398    1954
942 2324    1901    213 125 2518    655 189 2499    160 2841    2646    198 173 1841    200
232 45  272 280 44  248 50  266 296 297 236 254 58  212 276 48
563 768 124 267 153 622 199 591 204 125 93  656 198 164 797 506
243 4746    1785    204 568 4228    2701    4303    188 4148    4831    1557    4692    166 4210    3656
72  514 1572    172 1197    750 1392    1647    1587    183 1484    213 1614    718 177 622
1117    97  2758    2484    941 1854    1074    264 2494    83  1434    96  2067    2825    2160    92
2610    1290    204 2265    1374    2581    185 852 207 175 3308    1500    2898    1120    1892    3074
2322    1434    301 2156    98  2194    587 1416    1521    94  1985    424 91  119 1869    1073
66  87  176 107 2791    109 21  92  3016    2239    1708    3175    3210    2842    446 484"""


import itertools


def even_divide(row):
    # Since our input is sorted we need to check if each element modulus
    # succeeding elements has a remainder of zero
    for x, y in itertools.permutations(row, 2):
        if x % y:
            continue
        return x / y


def main():
    # Convert to a list of sorted integers (in descending order)
    inp = [list(reversed(sorted(int(y) for y in x.split()))) for x in INPUT.split("\n")]
    # Answer is the sum of even divisions within a row (of which only one exists)
    print sum(even_divide(x) for x in inp)


if __name__ == '__main__':
    main()

# vi: ts=4 et:
