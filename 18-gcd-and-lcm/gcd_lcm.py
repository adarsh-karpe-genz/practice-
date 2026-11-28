"""
Problem 18: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
Difficulty: Beginner / Easy

Problem Statement:
Given two integers `a` and `b`, compute both their:
1. Greatest Common Divisor (GCD) using the Euclidean Algorithm.
2. Least Common Multiple (LCM) using the identity: LCM(a, b) = |a * b| // GCD(a, b).
Example: a = 12, b = 18 -> GCD: 6, LCM: 36

Concepts:
- Euclidean algorithm for GCD (O(log(min(a, b))))
- Mathematical relation between GCD and LCM
"""

from typing import Tuple, List
import math
from functools import reduce


def compute_gcd(a: int, b: int) -> int:
    """Euclidean algorithm for GCD."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def compute_lcm(a: int, b: int) -> int:
    """LCM using GCD identity."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // compute_gcd(a, b)


def gcd_and_lcm(a: int, b: int) -> Tuple[int, int]:
    """Returns (gcd, lcm)."""
    g = compute_gcd(a, b)
    l = 0 if (a == 0 or b == 0) else abs(a * b) // g
    return (g, l)


def gcd_multiple(numbers: List[int]) -> int:
    """Computes GCD across a list of integers."""
    return reduce(compute_gcd, numbers)


def lcm_multiple(numbers: List[int]) -> int:
    """Computes LCM across a list of integers."""
    return reduce(compute_lcm, numbers)


def are_coprime(a: int, b: int) -> bool:
    """Returns True if a and b are mutually coprime (GCD == 1)."""
    return compute_gcd(a, b) == 1


if __name__ == "__main__":
    test_cases = [
        (12, 18, (6, 36)),
        (15, 25, (5, 75)),
        (7, 13, (1, 91)),
        (20, 0, (20, 0)),
        (100, 25, (25, 100)),
    ]

    for n1, n2, expected in test_cases:
        res = gcd_and_lcm(n1, n2)
        assert res == expected, f"Failed for {n1}, {n2}"
        assert compute_gcd(n1, n2) == math.gcd(n1, n2)
    assert gcd_multiple([12, 18, 24]) == 6
    assert lcm_multiple([4, 6, 8]) == 24

    # Test coprime check
    assert are_coprime(14, 15) is True
    assert are_coprime(14, 21) is False

    print("[PASS] Problem 18: GCD and LCM tests passed successfully!")
