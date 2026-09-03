"""
Problem 18: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
Difficulty: Beginner / Easy

Problem Statement:
Given two integers `a` and `b`, compute:
1. GCD (Greatest Common Divisor): Largest positive integer that divides both numbers without a remainder.
2. LCM (Least Common Multiple): Smallest positive integer that is divisible by both numbers.
Formula: LCM(a, b) = (|a * b|) // GCD(a, b)
Example: a = 12, b = 18 -> GCD = 6, LCM = 36

Concepts:
- Euclidean Algorithm for GCD (O(log(min(A, B))) time)
- Relationship between GCD and LCM
- math.gcd built-in comparison
"""

import math
from typing import Tuple


def compute_gcd(a: int, b: int) -> int:
    """Method 1: Euclidean Algorithm for GCD (O(log(min(A, B))) time, O(1) space)"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def compute_lcm(a: int, b: int) -> int:
    """Compute LCM using formula: (a * b) // GCD(a, b)"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // compute_gcd(a, b)


def gcd_and_lcm(a: int, b: int) -> Tuple[int, int]:
    """Return both GCD and LCM as a tuple."""
    g = compute_gcd(a, b)
    l = compute_lcm(a, b)
    return g, l


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 18: GCD & LCM Tests")
    print("=" * 50)

    test_cases = [
        (12, 18, (6, 36)),
        (10, 15, (5, 30)),
        (7, 13, (1, 91)),
        (20, 0, (20, 0)),
        (100, 25, (25, 100)),
    ]

    for n1, n2, expected in test_cases:
        res = gcd_and_lcm(n1, n2)
        print(f"Numbers: ({n1:3d}, {n2:3d}) -> GCD & LCM: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {n1}, {n2}"
        # Verify against math.gcd
        assert compute_gcd(n1, n2) == math.gcd(n1, n2)

    print("\n[PASS] All GCD & LCM tests passed successfully!")
