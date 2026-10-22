"""
Problem 117: Check Nonagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A nonagonal (or enneagonal) number is a figurate number that represents a 9-sided polygon.
The n-th nonagonal number is given by:
  Non(n) = n(7n - 5) // 2, for n >= 1.
First few nonagonal numbers:
  n = 1 -> 1
  n = 2 -> 9
  n = 3 -> 24
  n = 4 -> 46
  n = 5 -> 75
  n = 6 -> 111

Concepts:
- 9-sided polygon figurate numbers
- Solving 7n^2 - 5n - 2*val = 0
- Discriminant D = 25 + 56*val
"""

import math

def get_nonagonal_number(n: int) -> int:
    """Return the n-th nonagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (7 * n - 5) // 2

def is_nonagonal_number(val: int) -> bool:
    """Check if val is a nonagonal number:
    7n^2 - 5n - 2*val = 0
    Discriminant D = 25 + 56*val
    n = (5 + sqrt(D)) / 14
    """
    if val < 1:
        return False
    disc = 25 + 56 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 5 + r
    return numerator % 14 == 0 and numerator // 14 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 117: Nonagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 9),
        (3, 24),
        (4, 46),
        (5, 75),
        (6, 111),
    ]

    for n, expected in test_cases:
        res = get_nonagonal_number(n)
        print(f"Non({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_nonagonal_number(expected) is True

    assert is_nonagonal_number(2) is False
    assert is_nonagonal_number(10) is False
    assert is_nonagonal_number(30) is False

    print("\n[PASS] All Nonagonal Number tests passed successfully!")
