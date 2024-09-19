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

    # Initialize the coin count to zero
    coin_count = 0
    # Iterate through each coin in the coin list
    for coin in coins:
        # If the coin is > the remaining total, skip it
        if coin > total:
            continue
        # Calculate the number of times the coin can be used
        count = total // coin
        # Update the total by subtracting the value of coins used
        total -= count * coin
        # Update the coin count by adding the number of coins used
        coin_count += count
        # If the total is now zero, we're done
        if total == 0:
            break
    # If we couldn't make change for the total, return -1
    if total > 0:
        return -1
    # Otherwise, return the coin count
    return coin_count
