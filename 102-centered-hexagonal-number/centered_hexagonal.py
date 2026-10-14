"""
Problem 102: Centered Hexagonal Number (Hex Number)
Difficulty: Beginner / Easy

Problem Statement:
A centered hexagonal number is a figurate number that represents a hexagon with
a dot in the center and dots surrounding the center in successive hexagonal layers.
The n-th centered hexagonal number is given by:
  H(n) = 3n(n - 1) + 1, for n >= 1 (or 3n^2 + 3n + 1 for n >= 0).
First few centered hexagonal numbers:
  n = 1 -> 1
  n = 2 -> 7
  n = 3 -> 19
  n = 4 -> 37
  n = 5 -> 61
  n = 6 -> 91
  n = 7 -> 127

Concepts:
- Hexagonal lattice figurate numbers
- Difference of consecutive cubes identity: n^3 - (n-1)^3 = 3n(n-1) + 1
- Quadratic inverse checking
"""

import math

def get_centered_hexagonal(n: int) -> int:
    """Return the n-th centered hexagonal number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return 3 * n * (n - 1) + 1

def is_centered_hexagonal(val: int) -> bool:
    """Check if val is a centered hexagonal number:
    3n^2 - 3n + 1 - val = 0
    Discriminant D = 9 - 12*(1 - val) = 12*val - 3
    """
    if val < 1:
        return False
    disc = 12 * val - 3
    if disc < 0:
        return False
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    # n = (3 + sqrt(disc)) / 6
    numerator = 3 + r
    return numerator % 6 == 0 and numerator // 6 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 102: Centered Hexagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 7),
        (3, 19),
        (4, 37),
        (5, 61),
        (6, 91),
        (7, 127),
    ]

    for n, expected in test_cases:
        res = get_centered_hexagonal(n)
        print(f"H({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_hexagonal(expected) is True

    assert is_centered_hexagonal(2) is False
    assert is_centered_hexagonal(8) is False
    assert is_centered_hexagonal(20) is False

    print("\n[PASS] All Centered Hexagonal Number tests passed successfully!")
