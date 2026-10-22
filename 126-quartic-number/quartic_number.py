"""
Problem 126: Check Quartic Number (Fourth Power / Biquadratic Number)
Difficulty: Beginner / Easy

Problem Statement:
A quartic (or biquadratic) number is a figurate number that is the fourth power
of an integer: Q(n) = n^4, for n >= 0.
They represent hypercubes (tesseracts) in 4-dimensional space.
First few quartic numbers:
  0^4 = 0
  1^4 = 1
  2^4 = 16
  3^4 = 81
  4^4 = 256
  5^4 = 625
  6^4 = 1296

Concepts:
- 4-th power exponentiation
- Nested integer square root math.isqrt(math.isqrt(n))
- Tesseract geometry
"""

import math

def get_quartic_number(n: int) -> int:
    """Return n^4."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return n ** 4

def is_quartic_number(val: int) -> bool:
    """Check if val is an exact 4th power:
    val must be a square, and its square root must also be a square.
    """
    if val < 0:
        return False
    r1 = math.isqrt(val)
    if r1 * r1 != val:
        return False
    r2 = math.isqrt(r1)
    return r2 * r2 == r1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 126: Quartic Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 0),
        (1, 1),
        (2, 16),
        (3, 81),
        (4, 256),
        (5, 625),
        (6, 1296),
    ]

    for n, expected in test_cases:
        res = get_quartic_number(n)
        print(f"Q({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_quartic_number(expected) is True

    assert is_quartic_number(2) is False
    assert is_quartic_number(4) is False   # 4 is square but not fourth power
    assert is_quartic_number(8) is False
    assert is_quartic_number(25) is False

    print("\n[PASS] All Quartic Number tests passed successfully!")
