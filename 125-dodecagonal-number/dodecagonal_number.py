"""
Problem 125: Check Dodecagonal Number (12-gon)
Difficulty: Beginner / Easy

Problem Statement:
A dodecagonal number is a figurate number that represents a 12-sided regular polygon.
Formula:
  Dod(n) = 5n^2 - 4n, for n >= 1.
First few dodecagonal numbers:
  n = 1 -> 1
  n = 2 -> 12
  n = 3 -> 33
  n = 4 -> 64
  n = 5 -> 105
  n = 6 -> 156

Concepts:
- 12-sided polygon figurate numbers
- Solving 5n^2 - 4n - val = 0
- Discriminant D = 16 + 20*val
"""

import math

def get_dodecagonal_number(n: int) -> int:
    """Return the n-th dodecagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return 5 * n * n - 4 * n

def is_dodecagonal_number(val: int) -> bool:
    """Check if val is a dodecagonal number:
    Discriminant D = 16 + 20*val
    n = (4 + sqrt(D)) / 10
    """
    if val < 1:
        return False
    disc = 16 + 20 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 4 + r
    return numerator % 10 == 0 and numerator // 10 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 125: Dodecagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 12),
        (3, 33),
        (4, 64),
        (5, 105),
        (6, 156),
    ]

    for n, expected in test_cases:
        res = get_dodecagonal_number(n)
        print(f"Dod({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_dodecagonal_number(expected) is True

    assert is_dodecagonal_number(2) is False
    assert is_dodecagonal_number(13) is False
    assert is_dodecagonal_number(50) is False

    print("\n[PASS] All Dodecagonal Number tests passed successfully!")
