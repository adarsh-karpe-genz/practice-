"""
Problem 77: Check Abundant Number
Difficulty: Beginner / Easy

Problem Statement:
An abundant number is a positive integer for which the sum of its proper
divisors is strictly greater than the number itself.
Examples:
  12 -> Proper divisors: 1, 2, 3, 4, 6 -> Sum: 16 > 12 -> True (Abundant)
  18 -> Proper divisors: 1, 2, 3, 6, 9 -> Sum: 21 > 18 -> True (Abundant)
  15 -> Proper divisors: 1, 3, 5 -> Sum: 9 < 15 -> False (Deficient)

Concepts:
- Proper divisors summation O(sqrt(N))
- Abundance comparison: divisor_sum > n
"""

import math


def is_abundant(n: int) -> bool:
    """Check if sum of proper divisors of n strictly exceeds n."""
    if n <= 1:
        return False

    divisor_sum = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i

    return divisor_sum > n


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 77: Abundant Number Tests")
    print("=" * 50)

    test_cases = [
        (12, True),
        (18, True),
        (20, True),
        (24, True),
        (15, False),
        (16, False),  # divisors: 1, 2, 4, 8 -> sum 15 < 16
        (28, False),  # perfect number (sum == 28, not > 28)
        (1, False),
    ]

    for num, expected in test_cases:
        res = is_abundant(num)
        print(f"Number: {num:3d} -> Abundant? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Abundant Number tests passed successfully!")
