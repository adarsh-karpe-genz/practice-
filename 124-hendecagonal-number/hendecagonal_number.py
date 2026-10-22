"""
Problem 124: Check Hendecagonal Number (11-gon)
Difficulty: Beginner / Easy

Problem Statement:
A hendecagonal (or undecagonal) number is a figurate number that represents
an 11-sided regular polygon.
Formula:
  Hen(n) = (9n^2 - 7n) // 2, for n >= 1.
First few hendecagonal numbers:
  n = 1 -> 1
  n = 2 -> 11
  n = 3 -> 30
  n = 4 -> 58
  n = 5 -> 95
  n = 6 -> 141

Concepts:
- 11-sided polygon figurate numbers
- Solving 9n^2 - 7n - 2*val = 0
- Discriminant D = 49 + 72*val
"""

import math

def get_hendecagonal_number(n: int) -> int:
    """Return the n-th hendecagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return (9 * n * n - 7 * n) // 2

def is_hendecagonal_number(val: int) -> bool:
    """Check if val is a hendecagonal number:
    Discriminant D = 49 + 72*val
    n = (7 + sqrt(D)) / 18
    """
    if val < 1:
        return False
    disc = 49 + 72 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 7 + r
    return numerator % 18 == 0 and numerator // 18 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 124: Hendecagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 11),
        (3, 30),
        (4, 58),
        (5, 95),
        (6, 141),
    ]

    for n, expected in test_cases:
        res = get_hendecagonal_number(n)
        print(f"Hen({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_hendecagonal_number(expected) is True

    assert is_hendecagonal_number(2) is False
    assert is_hendecagonal_number(12) is False
    assert is_hendecagonal_number(40) is False

    print("\n[PASS] All Hendecagonal Number tests passed successfully!")
