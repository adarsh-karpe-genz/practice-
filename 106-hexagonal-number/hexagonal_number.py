"""
Problem 106: Check Hexagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A hexagonal number is a figurate number that represents a regular hexagon.
The n-th hexagonal number is given by:
  Hex(n) = 2n^2 - n = n(2n - 1), for n >= 1.
Notice that every hexagonal number is also a triangular number:
  Hex(n) = T(2n - 1).
First few hexagonal numbers:
  n = 1 -> 1
  n = 2 -> 6
  n = 3 -> 15
  n = 4 -> 28
  n = 5 -> 45
  n = 6 -> 66
  n = 7 -> 91

Concepts:
- 6-sided figurate numbers
- Solving quadratic equation 2n^2 - n - val = 0
- Discriminant D = 1 + 8*val
"""

import math

def get_hexagonal_number(n: int) -> int:
    """Return the n-th hexagonal number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return 2 * n * n - n

def is_hexagonal_number(val: int) -> bool:
    """Check if val is a hexagonal number:
    2n^2 - n - val = 0
    Discriminant D = 1 + 8*val
    n = (1 + sqrt(D)) / 4
    """
    if val < 1:
        return False
    disc = 1 + 8 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 1 + r
    return numerator % 4 == 0 and numerator // 4 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 106: Hexagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 6),
        (3, 15),
        (4, 28),
        (5, 45),
        (6, 66),
        (7, 91),
    ]

    for n, expected in test_cases:
        res = get_hexagonal_number(n)
        print(f"Hex({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_hexagonal_number(expected) is True

    assert is_hexagonal_number(2) is False
    assert is_hexagonal_number(5) is False
    assert is_hexagonal_number(20) is False

    print("\n[PASS] All Hexagonal Number tests passed successfully!")
