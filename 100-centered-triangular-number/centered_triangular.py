"""
Problem 100: Centered Triangular Number (🎉 Problem 100 Milestone!)
Difficulty: Beginner / Easy

Problem Statement:
A centered triangular number is a figurate number that represents a triangle
with a dot in the center and all other dots surrounding the center in successive
triangular layers.
The n-th centered triangular number is given by the formula:
  C_3(n) = (3 * n^2 + 3 * n + 2) // 2, for n >= 0.
First few centered triangular numbers:
  n = 0 -> 1
  n = 1 -> 4
  n = 2 -> 10
  n = 3 -> 19
  n = 4 -> 31
  n = 5 -> 46
  n = 6 -> 64

Concepts:
- Figurate numbers and polygon representations
- Quadratic algebraic formulas
- Quadratic equation inverse solver (isqrt)
"""

import math

def get_centered_triangular(n: int) -> int:
    """Return the n-th centered triangular number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return (3 * n * n + 3 * n + 2) // 2

def is_centered_triangular(val: int) -> bool:
    """Check if val is a centered triangular number by solving the quadratic:
    3n^2 + 3n + (2 - 2*val) = 0
    Discriminant D = b^2 - 4ac = 9 - 4*3*(2 - 2*val) = 9 - 24 + 24*val = 24*val - 15
    """
    if val < 1:
        return False
    disc = 24 * val - 15
    if disc < 0:
        return False
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    # n = (-3 + sqrt(disc)) / 6
    numerator = -3 + r
    return numerator >= 0 and numerator % 6 == 0

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 100: Centered Triangular Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 1),
        (1, 4),
        (2, 10),
        (3, 19),
        (4, 31),
        (5, 46),
        (6, 64),
    ]

    for n, expected in test_cases:
        res = get_centered_triangular(n)
        print(f"C_3({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_triangular(expected) is True

    assert is_centered_triangular(2) is False
    assert is_centered_triangular(5) is False
    assert is_centered_triangular(20) is False

    print("\n[PASS] All Problem 100 Centered Triangular Number tests passed successfully!")
