#!/usr/bin/python3
"""return fewest number of coins needed to meet total
"""


def makeChange(coins, total):
    """Create a list to store the minimum number
    of coins needed for each total value
    """
    if total <= 0:
        return 0
    # dp = [float('inf')] * (total + 1)
    # dp[0] = 0  # Base case: no coins needed for total of 0

    # for coin in coins:
    #     for i in range(coin, total + 1):
    #         dp[i] = min(dp[i], dp[i - coin] + 1)

    # if dp[total] == float('inf'):
    #     return -1  # Total cannot be met by any number of coins
    # else:
    #     return dp[total]  # Minimum number of coins needed for the total
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count