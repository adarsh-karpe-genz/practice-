"""
Problem 122: Check Centered Nonagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A centered nonagonal (or enneagonal) number is a centered figurate number
representing a 9-gon.
Formula:
  CN(n) = (9n^2 - 9n + 2) // 2, for n >= 1.
First few centered nonagonal numbers:
  n = 1 -> 1
  n = 2 -> 10
  n = 3 -> 28
  n = 4 -> 55
  n = 5 -> 91
  n = 6 -> 136

Concepts:
- Centered 9-gon figurate representation
- Solving 9n^2 - 9n + (2 - 2*val) = 0
- Discriminant D = 81 - 36*(2 - 2*val) = 72*val + 9
"""

import math

def get_centered_nonagonal(n: int) -> int:
    """Return the n-th centered nonagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return (9 * n * n - 9 * n + 2) // 2

def is_centered_nonagonal(val: int) -> bool:
    """Check if val is a centered nonagonal number:
    Discriminant D = 72*val + 9
    n = (9 + sqrt(D)) / 18
    """
    if val < 1:
        return False
    disc = 72 * val + 9
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 9 + r
    return numerator % 18 == 0 and numerator // 18 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 122: Centered Nonagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 10),
        (3, 28),
        (4, 55),
        (5, 91),
        (6, 136),
    ]

    for n, expected in test_cases:
        res = get_centered_nonagonal(n)
        print(f"CN({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_nonagonal(expected) is True

    assert is_centered_nonagonal(2) is False
    assert is_centered_nonagonal(15) is False
    assert is_centered_nonagonal(40) is False

    print("\n[PASS] All Centered Nonagonal Number tests passed successfully!")
