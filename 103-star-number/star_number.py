"""
Problem 103: Check Star Number
Difficulty: Beginner / Easy

Problem Statement:
A star number is a centered figurate number that represents a centered hexagram
(six-pointed star), such as the Chinese checkers board.
The n-th star number is given by the formula:
  S(n) = 6n(n - 1) + 1, for n >= 1.
First few star numbers:
  n = 1 -> 1
  n = 2 -> 13
  n = 3 -> 37
  n = 4 -> 73
  n = 5 -> 121
  n = 6 -> 181
  n = 7 -> 253

Concepts:
- Centered hexagram figurate numbers
- Quadratic equation inverse solver
- Modulo arithmetic check
"""

import math

def get_star_number(n: int) -> int:
    """Return the n-th star number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return 6 * n * (n - 1) + 1

def is_star_number(val: int) -> bool:
    """Check if val is a star number:
    6n^2 - 6n + 1 - val = 0
    Discriminant D = 36 - 24*(1 - val) = 24*val + 12 = 12*(2*val + 1)
    Also (val - 1) must be divisible by 6, and root of 1 + 4*(val - 1)/6
    More cleanly: 6n(n-1) = val - 1 => n(n-1) = (val - 1) // 6.
    Let k = (val - 1) // 6. Then k is a pronic number (n*(n-1)).
    """
    if val < 1:
        return False
    if (val - 1) % 6 != 0:
        return False
    k = (val - 1) // 6
    # Check if k = m * (m + 1) where m = n - 1 >= 0
    m = math.isqrt(k)
    return m * (m + 1) == k

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 103: Star Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 13),
        (3, 37),
        (4, 73),
        (5, 121),
        (6, 181),
        (7, 253),
    ]

    for n, expected in test_cases:
        res = get_star_number(n)
        print(f"S({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_star_number(expected) is True

    assert is_star_number(2) is False
    assert is_star_number(12) is False
    assert is_star_number(50) is False

    print("\n[PASS] All Star Number tests passed successfully!")
