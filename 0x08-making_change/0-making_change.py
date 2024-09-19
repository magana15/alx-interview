#!/usr/bin/python3
"""
makeChange module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.

    :param coins: List of coin denominations
    :param total: Target amount
    :return: Fewest number of coins, or -1 if the total cannot be met
    """
    if total <= 0:
        return 0

    # Initialize DP array for dynamic programming solution
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
