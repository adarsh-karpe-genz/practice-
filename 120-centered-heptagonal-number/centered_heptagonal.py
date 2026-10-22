"""
Problem 120: Check Centered Heptagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A centered heptagonal number is a centered figurate number that represents
a heptagon with a dot in the center and dots in successive heptagonal layers.
Formula:
  CH(n) = (7n^2 - 7n + 2) // 2, for n >= 1.
First few centered heptagonal numbers:
  n = 1 -> 1
  n = 2 -> 8
  n = 3 -> 22
  n = 4 -> 43
  n = 5 -> 71
  n = 6 -> 106

Concepts:
- Centered 7-sided polygon figurate
- Solving 7n^2 - 7n + (2 - 2*val) = 0
- Discriminant D = 49 - 28*(2 - 2*val) = 56*val - 7
"""

import math

def get_centered_heptagonal(n: int) -> int:
    """Return the n-th centered heptagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return (7 * n * n - 7 * n + 2) // 2

def is_centered_heptagonal(val: int) -> bool:
    """Check if val is a centered heptagonal number:
    Discriminant D = 56*val - 7
    n = (7 + sqrt(D)) / 14
    """
    if val < 1:
        return False
    disc = 56 * val - 7
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 7 + r
    return numerator % 14 == 0 and numerator // 14 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 120: Centered Heptagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 8),
        (3, 22),
        (4, 43),
        (5, 71),
        (6, 106),
    ]

    for n, expected in test_cases:
        res = get_centered_heptagonal(n)
        print(f"CH({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_heptagonal(expected) is True

    assert is_centered_heptagonal(2) is False
    assert is_centered_heptagonal(10) is False
    assert is_centered_heptagonal(30) is False

    print("\n[PASS] All Centered Heptagonal Number tests passed successfully!")
