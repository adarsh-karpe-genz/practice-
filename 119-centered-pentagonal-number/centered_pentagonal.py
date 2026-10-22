"""
Problem 119: Check Centered Pentagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A centered pentagonal number is a centered figurate number that represents
a pentagon with a dot in the center and all other dots surrounding the center
in successive pentagonal layers.
Formula:
  CP(n) = (5n^2 - 5n + 2) // 2, for n >= 1 (or (5n^2 + 5n + 2)//2 for n >= 0).
First few centered pentagonal numbers:
  n = 1 -> 1
  n = 2 -> 6
  n = 3 -> 16
  n = 4 -> 31
  n = 5 -> 51
  n = 6 -> 76

Concepts:
- Centered 5-sided polygon figurates
- Quadratic check 5n^2 - 5n + 2 - 2*val = 0
- Discriminant D = 25 - 4*5*(2 - 2*val) = 40*val - 15
"""

import math

def get_centered_pentagonal(n: int) -> int:
    """Return the n-th centered pentagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return (5 * n * n - 5 * n + 2) // 2

def is_centered_pentagonal(val: int) -> bool:
    """Check if val is a centered pentagonal number:
    5n^2 - 5n + (2 - 2*val) = 0
    Discriminant D = 25 - 20*(2 - 2*val) = 40*val - 15
    n = (5 + sqrt(D)) / 10
    """
    if val < 1:
        return False
    disc = 40 * val - 15
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 5 + r
    return numerator % 10 == 0 and numerator // 10 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 119: Centered Pentagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 6),
        (3, 16),
        (4, 31),
        (5, 51),
        (6, 76),
    ]

    for n, expected in test_cases:
        res = get_centered_pentagonal(n)
        print(f"CP({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_pentagonal(expected) is True

    assert is_centered_pentagonal(2) is False
    assert is_centered_pentagonal(7) is False
    assert is_centered_pentagonal(20) is False

    print("\n[PASS] All Centered Pentagonal Number tests passed successfully!")
