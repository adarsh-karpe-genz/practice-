"""
Problem 108: Check Triangular Number
Difficulty: Beginner / Easy

Problem Statement:
A triangular number counts objects arranged in an equilateral triangle.
The n-th triangular number is the sum of the first n natural numbers:
  T(n) = n(n + 1) // 2, for n >= 1.
First few triangular numbers:
  n = 1 -> 1
  n = 2 -> 3
  n = 3 -> 6
  n = 4 -> 10
  n = 5 -> 15
  n = 6 -> 21
  n = 7 -> 28

Concepts:
- Gauss summation formula
- Quadratic inverse: n^2 + n - 2*val = 0
- Discriminant D = 1 + 8*val
"""

import math

def get_triangular_number(n: int) -> int:
    """Return the n-th triangular number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (n + 1) // 2

def is_triangular_number(val: int) -> bool:
    """Check if val is a triangular number:
    n^2 + n - 2*val = 0
    Discriminant D = 1 + 8*val
    n = (-1 + sqrt(D)) / 2
    """
    if val < 1:
        return False
    disc = 1 + 8 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = -1 + r
    return numerator % 2 == 0 and numerator // 2 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 108: Triangular Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
        (6, 21),
        (7, 28),
    ]

    for n, expected in test_cases:
        res = get_triangular_number(n)
        print(f"T({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_triangular_number(expected) is True

    assert is_triangular_number(2) is False
    assert is_triangular_number(5) is False
    assert is_triangular_number(12) is False

    print("\n[PASS] All Triangular Number tests passed successfully!")
