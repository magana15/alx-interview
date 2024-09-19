#!/usr/bin/python3
"""
makeChange module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.
    Optimized to handle larger input sizes efficiently.

    :param coins: List of coin denominations
    :param total: Target amount
    :return: Fewest number of coins, or -1 if the total cannot be met
    """
    if total <= 0:
        return 0

    # Sort coins to start with larger values for more efficient reduction
    coins.sort(reverse=True)

    # Initialize DP array for dynamic programming
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over every amount from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we cannot reach the total
    return dp[total] if dp[total] != float('inf') else -1
