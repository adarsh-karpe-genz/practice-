"""
Problem 109: Check Square Pyramidal Number
Difficulty: Beginner / Easy

Problem Statement:
A square pyramidal number is a figurate number that represents the number of
spheres in a pyramid with a square base. It is the sum of squares of the first n natural numbers:
  P(n) = n(n + 1)(2n + 1) // 6, for n >= 1.
First few square pyramidal numbers:
  n = 1 -> 1
  n = 2 -> 1 + 4 = 5
  n = 3 -> 1 + 4 + 9 = 14
  n = 4 -> 1 + 4 + 9 + 16 = 30
  n = 5 -> 55
  n = 6 -> 91

Concepts:
- Sum of squares formula
- Monotonic sequence search
- 3D figurate numbers
"""

def get_square_pyramidal(n: int) -> int:
    """Return the n-th square pyramidal number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (n + 1) * (2 * n + 1) // 6

def is_square_pyramidal(val: int) -> bool:
    """Check if val is a square pyramidal number."""
    if val < 1:
        return False
    n = 1
    while True:
        p = get_square_pyramidal(n)
        if p == val:
            return True
        if p > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 109: Square Pyramidal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 5),
        (3, 14),
        (4, 30),
        (5, 55),
        (6, 91),
        (7, 140),
    ]

    for n, expected in test_cases:
        res = get_square_pyramidal(n)
        print(f"P({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_square_pyramidal(expected) is True

    assert is_square_pyramidal(2) is False
    assert is_square_pyramidal(10) is False
    assert is_square_pyramidal(25) is False

    print("\n[PASS] All Square Pyramidal Number tests passed successfully!")
