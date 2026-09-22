"""
Problem 72: Check Sunny Number
Difficulty: Beginner / Easy

Problem Statement:
A number N is called a Sunny Number if N + 1 is a perfect square.
Examples:
  8  -> 8 + 1 = 9 (which is 3^2)   -> True (Sunny Number)
  15 -> 15 + 1 = 16 (which is 4^2) -> True (Sunny Number)
  3  -> 3 + 1 = 4 (which is 2^2)   -> True (Sunny Number)
  10 -> 10 + 1 = 11 (not a square) -> False

Concepts:
- math.isqrt() integer square root checking
- Perfect square condition: root * root == (n + 1)
- Arithmetic operations
"""

import math


def is_sunny_number(n: int) -> bool:
    """Check if n + 1 is a perfect square."""
    if n < 0:
        return False
    target = n + 1
    root = math.isqrt(target)
    return root * root == target


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 72: Sunny Number Tests")
    print("=" * 50)

    test_cases = [
        (8, True),
        (15, True),
        (3, True),
        (24, True),   # 24 + 1 = 25 (5^2)
        (35, True),   # 35 + 1 = 36 (6^2)
        (0, True),    # 0 + 1 = 1 (1^2)
        (10, False),
        (5, False),
    ]

    for num, expected in test_cases:
        res = is_sunny_number(num)
        print(f"Number: {num:2d} -> Sunny? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Sunny Number tests passed successfully!")
