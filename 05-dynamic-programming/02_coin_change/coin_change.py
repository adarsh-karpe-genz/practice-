"""
Problem: Coin Change
LeetCode: #322 (Medium)

Time Complexity: O(Amount * N)
Space Complexity: O(Amount)
"""

from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    print("[Python] Coin Change Test")
    tests = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]
    for coins, amount, expected in tests:
        res = coin_change(coins, amount)
        print(f"coins: {coins}, amount: {amount} -> Min Coins: {res} | Expected: {expected}")
        assert res == expected
    print("Coin change tests passed!")
