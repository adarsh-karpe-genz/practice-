"""
Problem 41: Check if a Number is a Power of Two
Difficulty: Beginner / Easy

Problem Statement:
Given an integer n, determine if it is a power of 2.
A number n is a power of 2 if n = 2^k for some non-negative integer k.
Examples:
  1   -> True  (2^0)
  16  -> True  (2^4)
  18  -> False
  0   -> False
  -4  -> False

Concepts:
- Bit manipulation trick: n & (n - 1) == 0  (clears lowest set bit)
- Division loop: keep dividing by 2 while even
- math.log2 formula check
"""

import math


def is_power_of_two_bitwise(n: int) -> bool:
    """Method 1: Bit manipulation O(1) - n > 0 and n has exactly one set bit."""
    return n > 0 and (n & (n - 1)) == 0


def is_power_of_two_loop(n: int) -> bool:
    """Method 2: Division loop."""
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1


def is_power_of_two_math(n: int) -> bool:
    """Method 3: math.log2 check."""
    if n <= 0:
        return False
    log_val = math.log2(n)
    return log_val == int(log_val)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 41: Power of Two Tests")
    print("=" * 50)

    test_cases = [
        (1, True),
        (2, True),
        (16, True),
        (64, True),
        (1024, True),
        (0, False),
        (-4, False),
        (18, False),
        (3, False),
        (100, False),
    ]

    for n, expected in test_cases:
        r1 = is_power_of_two_bitwise(n)
        r2 = is_power_of_two_loop(n)
        r3 = is_power_of_two_math(n)
        print(f"n={n:6d} -> Power of 2? {r1} | Expected: {expected}")
        assert r1 == expected, f"Bitwise failed for {n}"
        assert r2 == expected, f"Loop failed for {n}"
        assert r3 == expected, f"Math failed for {n}"

    print("\n[PASS] All Power of Two tests passed successfully!")
