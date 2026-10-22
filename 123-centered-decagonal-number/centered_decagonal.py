"""
Problem 123: Check Centered Decagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A centered decagonal number represents a 10-gon with a dot in the center and
dots surrounding the center in successive 10-sided layers.
Formula:
  CD(n) = 5n^2 - 5n + 1 = 5n(n - 1) + 1, for n >= 1.
First few centered decagonal numbers:
  n = 1 -> 1
  n = 2 -> 11
  n = 3 -> 31
  n = 4 -> 61
  n = 5 -> 101
  n = 6 -> 151

Concepts:
- Centered 10-gon figurates
- (val - 1) % 5 == 0 check
- Pronic relation (val - 1) // 5 = n*(n - 1)
"""

import math

def get_centered_decagonal(n: int) -> int:
    """Return the n-th centered decagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return 5 * n * (n - 1) + 1

def is_centered_decagonal(val: int) -> bool:
    """Check if val is a centered decagonal number:
    5n(n-1) = val - 1 => k = (val - 1)//5 is pronic m*(m+1).
    """
    if val < 1:
        return False
    if (val - 1) % 5 != 0:
        return False
    k = (val - 1) // 5
    m = math.isqrt(k)
    return m * (m + 1) == k

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 123: Centered Decagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 11),
        (3, 31),
        (4, 61),
        (5, 101),
        (6, 151),
    ]

    for n, expected in test_cases:
        res = get_centered_decagonal(n)
        print(f"CD({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_centered_decagonal(expected) is True

    assert is_centered_decagonal(2) is False
    assert is_centered_decagonal(12) is False
    assert is_centered_decagonal(50) is False

    print("\n[PASS] All Centered Decagonal Number tests passed successfully!")
