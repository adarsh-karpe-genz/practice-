"""
Problem 76: Check Pronic Number (Heteromecic Number)
Difficulty: Beginner / Easy

Problem Statement:
A pronic number (or oblong number) is a number that is the product of two
consecutive integers: n = k * (k + 1) for some non-negative integer k.
Examples:
  6  = 2 * 3   -> True
  12 = 3 * 4   -> True
  20 = 4 * 5   -> True
  8            -> False (no consecutive ints product to 8)
  0  = 0 * 1   -> True

Concepts:
- Consecutive integer multiplication
- Integer square root math.isqrt()
- Loop bounds optimization
"""

import math

def is_pronic(n: int) -> bool:
    """Check if n is a pronic number (k * (k + 1))."""
    if n < 0:
        return False
    k = math.isqrt(n)
    return k * (k + 1) == n

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 76: Pronic Number Tests")
    print("=" * 50)

    test_cases = [
        (0, True),
        (2, True),
        (6, True),
        (12, True),
        (20, True),
        (42, True),
        (8, False),
        (10, False),
        (25, False),
    ]

    for num, expected in test_cases:
        res = is_pronic(num)
        print(f"Num: {num:3d} -> Pronic? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Pronic Number tests passed successfully!")
