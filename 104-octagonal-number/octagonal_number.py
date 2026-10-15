"""
Problem 104: Check Octagonal Number
Difficulty: Beginner / Easy

Problem Statement:
An octagonal number is a figurate number that extends the concept of triangular
and square numbers to an octagon (8-gon).
The n-th octagonal number is given by the formula:
  Oct(n) = 3n^2 - 2n, for n >= 1.
First few octagonal numbers:
  n = 1 -> 1
  n = 2 -> 8
  n = 3 -> 21
  n = 4 -> 40
  n = 5 -> 65
  n = 6 -> 96
  n = 7 -> 133

Concepts:
- 8-sided figurate numbers
- Solving quadratic equation 3n^2 - 2n - val = 0
- math.isqrt() discriminant verification
"""

import math

def get_octagonal_number(n: int) -> int:
    """Return the n-th octagonal number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return 3 * n * n - 2 * n

def is_octagonal_number(val: int) -> bool:
    """Check if val is an octagonal number:
    3n^2 - 2n - val = 0
    Discriminant D = (-2)^2 - 4*3*(-val) = 4 + 12*val
    n = (2 + sqrt(D)) / 6
    """
    if val < 1:
        return False
    disc = 4 + 12 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 2 + r
    return numerator % 6 == 0 and numerator // 6 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 104: Octagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 8),
        (3, 21),
        (4, 40),
        (5, 65),
        (6, 96),
        (7, 133),
    ]

    for n, expected in test_cases:
        res = get_octagonal_number(n)
        print(f"Oct({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_octagonal_number(expected) is True

    assert is_octagonal_number(2) is False
    assert is_octagonal_number(10) is False
    assert is_octagonal_number(30) is False

    print("\n[PASS] All Octagonal Number tests passed successfully!")
