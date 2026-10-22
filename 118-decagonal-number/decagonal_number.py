"""
Problem 118: Check Decagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A decagonal number is a figurate number that represents a 10-sided polygon.
The n-th decagonal number is given by:
  Dec(n) = 4n^2 - 3n, for n >= 1.
First few decagonal numbers:
  n = 1 -> 1
  n = 2 -> 10
  n = 3 -> 27
  n = 4 -> 52
  n = 5 -> 85
  n = 6 -> 126

Concepts:
- 10-sided polygon figurate numbers
- Solving 4n^2 - 3n - val = 0
- Discriminant D = 9 + 16*val
"""

import math

def get_decagonal_number(n: int) -> int:
    """Return the n-th decagonal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return 4 * n * n - 3 * n

def is_decagonal_number(val: int) -> bool:
    """Check if val is a decagonal number:
    4n^2 - 3n - val = 0
    Discriminant D = 9 + 16*val
    n = (3 + sqrt(D)) / 8
    """
    if val < 1:
        return False
    disc = 9 + 16 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 3 + r
    return numerator % 8 == 0 and numerator // 8 >= 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 118: Decagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 10),
        (3, 27),
        (4, 52),
        (5, 85),
        (6, 126),
    ]

    for n, expected in test_cases:
        res = get_decagonal_number(n)
        print(f"Dec({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_decagonal_number(expected) is True

    assert is_decagonal_number(2) is False
    assert is_decagonal_number(11) is False
    assert is_decagonal_number(40) is False

    print("\n[PASS] All Decagonal Number tests passed successfully!")
