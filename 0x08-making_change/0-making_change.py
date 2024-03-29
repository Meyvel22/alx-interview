#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """This function will take a list of coins and use
       that to calculate how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        count = 0
        for x in coin:
            while(total >= x):
                count += 1
                total -= x
        if total == 0:
            return count
        return -1
