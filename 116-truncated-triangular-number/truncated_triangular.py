"""
Problem 116: Check Truncated Triangular Number
Difficulty: Beginner / Easy

Problem Statement:
A truncated triangular number is a figurate number obtained by removing
the vertices from an equilateral triangular grid of side n.
Formula:
  TT(n) = (3n^2 - 3n) // 2, for n >= 2.
First few values for n = 2, 3, 4, 5, 6, 7:
  n = 2 -> 3
  n = 3 -> 9
  n = 4 -> 18
  n = 5 -> 30
  n = 6 -> 45
  n = 7 -> 63

Notice: TT(n) = 3 * T(n - 1) where T(n) is the triangular number.

Concepts:
- Truncated polygon figurates
- Tripled triangular numbers
- Quadratic checks
"""

import math

def get_truncated_triangular(n: int) -> int:
    """Return the n-th truncated triangular number for n >= 2."""
    if n < 2:
        raise ValueError("n must be at least 2")
    return (3 * n * n - 3 * n) // 2

def is_truncated_triangular(val: int) -> bool:
    """Check if val is a truncated triangular number:
    val must be divisible by 3, and val // 3 must be a triangular number T(n - 1).
    """
    if val < 3 or val % 3 != 0:
        return False
    t = val // 3
    # Check if t is a triangular number: 8*t + 1 must be a square
    disc = 8 * t + 1
    r = math.isqrt(disc)
    return r * r == disc and (-1 + r) % 2 == 0 and (-1 + r) // 2 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 116: Truncated Triangular Number Tests")
    print("=" * 50)

    test_cases = [
        (2, 3),
        (3, 9),
        (4, 18),
        (5, 30),
        (6, 45),
        (7, 63),
    ]

    for n, expected in test_cases:
        res = get_truncated_triangular(n)
        print(f"TT({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_truncated_triangular(expected) is True

    assert is_truncated_triangular(4) is False
    assert is_truncated_triangular(10) is False
    assert is_truncated_triangular(20) is False

    print("\n[PASS] All Truncated Triangular Number tests passed successfully!")
