"""
Problem 112: Check Stella Octangula Number
Difficulty: Beginner / Easy

Problem Statement:
A stella octangula number (or star tetrahedral number) is a figurate number that
represents a stella octangula (a three-dimensional eight-pointed star).
Formula:
  St(n) = n(2n^2 - 1) = 2n^3 - n, for n >= 1.
First few stella octangula numbers:
  n = 1 -> 1
  n = 2 -> 14
  n = 3 -> 51
  n = 4 -> 124
  n = 5 -> 245
  n = 6 -> 426

Concepts:
- 3D star polyhedral figurate numbers
- Cubic polynomial growth
- Sequence search iteration
"""

def get_stella_octangula(n: int) -> int:
    """Return the n-th stella octangula number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (2 * n * n - 1)

def is_stella_octangula(val: int) -> bool:
    """Check if val is a stella octangula number."""
    if val < 1:
        return False
    n = 1
    while True:
        s = get_stella_octangula(n)
        if s == val:
            return True
        if s > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 112: Stella Octangula Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 14),
        (3, 51),
        (4, 124),
        (5, 245),
        (6, 426),
    ]

    for n, expected in test_cases:
        res = get_stella_octangula(n)
        print(f"St({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_stella_octangula(expected) is True

    assert is_stella_octangula(2) is False
    assert is_stella_octangula(15) is False
    assert is_stella_octangula(100) is False

    print("\n[PASS] All Stella Octangula Number tests passed successfully!")
