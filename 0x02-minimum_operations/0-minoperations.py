#!/usr/bin/python3
"""Module that determines minimum number of operations """


def minOperations(n):
    # init the varible ops
    ops = 0
    # init divisor starting with 2
    divisor = 2
    # ensure n is greater than 1
    while n > 1:
        # look for the divisor that divides completely
        while n % divisor == 0:
            # add the divisor to ops
            ops += divisor
            # divide n by the divisor to reduce it
            n //= divisor
        # otherwise try the next number
        divisor += 1
    # returns the nummber of ops once done
    return ops
