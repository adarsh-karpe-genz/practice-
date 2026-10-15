"""
Problem 105: Check Heptagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A heptagonal number is a figurate number that represents a regular 7-sided polygon.
The n-th heptagonal number is given by:
  Hep(n) = (5n^2 - 3n) // 2, for n >= 1.
First few heptagonal numbers:
  n = 1 -> 1
  n = 2 -> 7
  n = 3 -> 18
  n = 4 -> 34
  n = 5 -> 55
  n = 6 -> 81
  n = 7 -> 112

Concepts:
- 7-sided figurate numbers
- Solving quadratic equation 5n^2 - 3n - 2*val = 0
- Discriminant D = 9 + 40*val
"""

import math

def get_heptagonal_number(n: int) -> int:
    """Return the n-th heptagonal number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return (5 * n * n - 3 * n) // 2

def is_heptagonal_number(val: int) -> bool:
    """Check if val is a heptagonal number:
    5n^2 - 3n - 2*val = 0
    Discriminant D = 9 + 40*val
    n = (3 + sqrt(D)) / 10
    """
    if val < 1:
        return False
    disc = 9 + 40 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 3 + r
    return numerator % 10 == 0 and numerator // 10 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 105: Heptagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 7),
        (3, 18),
        (4, 34),
        (5, 55),
        (6, 81),
        (7, 112),
    ]

    for n, expected in test_cases:
        res = get_heptagonal_number(n)
        print(f"Hep({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_heptagonal_number(expected) is True

    assert is_heptagonal_number(2) is False
    assert is_heptagonal_number(10) is False
    assert is_heptagonal_number(25) is False

    print("\n[PASS] All Heptagonal Number tests passed successfully!")
