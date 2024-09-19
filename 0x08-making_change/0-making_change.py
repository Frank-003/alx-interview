#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
        coins: A list of integer coin values.
        total: The target amount to be met.

    Returns:
        The fewest number of coins needed to meet the total, or -1 if impossible.
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
