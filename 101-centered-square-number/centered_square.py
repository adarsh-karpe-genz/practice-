"""
Problem 101: Centered Square Number
Difficulty: Beginner / Easy

Problem Statement:
A centered square number is a figurate number that gives the number of dots
in a square with a dot in the center and successive square layers of dots.
The n-th centered square number is given by:
  C_4(n) = n^2 + (n - 1)^2, for n >= 1 (or 2n(n-1) + 1).
First few centered square numbers:
  n = 1 -> 1
  n = 2 -> 5
  n = 3 -> 13
  n = 4 -> 25
  n = 5 -> 41
  n = 6 -> 61
  n = 7 -> 85

Concepts:
- Sum of two consecutive squares: n^2 + (n-1)^2
- Quadratic formula check
- Inverting via integer square root
"""

import math

def get_centered_square(n: int) -> int:
    """Return the n-th centered square number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * n + (n - 1) * (n - 1)

def is_centered_square(val: int) -> bool:
    """Check if val is a centered square number:
    2n^2 - 2n + 1 - val = 0
    Discriminant D = 4 - 4*2*(1 - val) = 4 - 8 + 8*val = 8*val - 4
    """
    if val < 1:
        return False
    disc = 8 * val - 4
    if disc < 0:
        return False
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    # n = (2 + sqrt(disc)) / 4
    numerator = 2 + r
    return numerator % 4 == 0 and numerator // 4 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 101: Centered Square Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 5),
        (3, 13),
        (4, 25),
        (5, 41),
        (6, 61),
        (7, 85),
    ]

    for n, expected in test_cases:
        res = get_centered_square(n)
        print(f"C_4({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_square(expected) is True

    assert is_centered_square(2) is False
    assert is_centered_square(10) is False
    assert is_centered_square(20) is False

    print("\n[PASS] All Centered Square Number tests passed successfully!")
