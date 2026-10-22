"""
Problem 121: Check Centered Octagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A centered octagonal number represents an octagon with a center dot and
successive octagonal layers.
Formula:
  CO(n) = 4n^2 - 4n + 1 = (2n - 1)^2, for n >= 1.
Notice: Every centered octagonal number is simply an ODD PERFECT SQUARE!
First few centered octagonal numbers:
  n = 1 -> 1^2 = 1
  n = 2 -> 3^2 = 9
  n = 3 -> 5^2 = 25
  n = 4 -> 7^2 = 49
  n = 5 -> 9^2 = 81

Concepts:
- Figurate relationship to odd squares (2n-1)^2
- Integer square root math.isqrt()
- Odd number condition
"""

import math

def get_centered_octagonal(n: int) -> int:
    """Return the n-th centered octagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return (2 * n - 1) ** 2

def is_centered_octagonal(val: int) -> bool:
    """Check if val is an odd perfect square."""
    if val < 1:
        return False
    r = math.isqrt(val)
    return r * r == val and r % 2 != 0

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 121: Centered Octagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 9),
        (3, 25),
        (4, 49),
        (5, 81),
        (6, 121),
    ]

    for n, expected in test_cases:
        res = get_centered_octagonal(n)
        print(f"CO({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_octagonal(expected) is True

    assert is_centered_octagonal(4) is False   # Even square
    assert is_centered_octagonal(16) is False  # Even square
    assert is_centered_octagonal(10) is False

    print("\n[PASS] All Centered Octagonal Number tests passed successfully!")
