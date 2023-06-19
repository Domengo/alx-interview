#!/usr/bin/python3
"""return fewest number of coins needed to meet total
"""


def makeChange(coins, total, memo=None):
    """make"""
    if total < 0:
        return -1  # Total cannot be met by any number of coins
    if total == 0:
        return 0  # Base case: no coins needed for total of 0

    if memo is None:
        memo = {}  # Memoization dictionary to store computed results

    if total in memo:
        return memo[total]

    min_coins = float("inf")
    for coin in coins:
        result = makeChange(coins, total - coin, memo)
        if result >= 0 and result < min_coins:
            min_coins = result + 1

    if min_coins == float("inf"):
        min_coins = -1  # Total cannot be met by any combination of coins

    memo[total] = min_coins
    return min_coins
