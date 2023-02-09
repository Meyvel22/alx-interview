#!/usr/bin/python3

"""
    Method that determines the minimum operations given n characters
"""


def minOperations(n):
    """
        A method that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of minimum operations
    """

    current = 1
    begin = 0
    tally = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            begin = current
            current += begin
            tally += 2
        else:
            current += begin
            tally += 1
    return tally
