#!/usr/bin/python3
"""Locating the minimum number of operations"""


def minOperations(n):
    """A function that finds minimum operations of copy all and paste
    required to product the n H characters"""
    if n <= 1:
        return 0
    op = 0
    div = 2
    while n > 1:
        while n % div == 0:
            op += div
            n /= div
        div += 1
    return op
