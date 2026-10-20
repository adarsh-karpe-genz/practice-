"""
Problem 110: Check Tetrahedral Number (Triangular Pyramidal)
Difficulty: Beginner / Easy

Problem Statement:
A tetrahedral number represents a pyramid with a triangular base (tetrahedron).
It is the sum of the first n triangular numbers:
  Te(n) = n(n + 1)(n + 2) // 6, for n >= 1.
First few tetrahedral numbers:
  n = 1 -> 1
  n = 2 -> 1 + 3 = 4
  n = 3 -> 1 + 3 + 6 = 10
  n = 4 -> 1 + 3 + 6 + 10 = 20
  n = 5 -> 35
  n = 6 -> 56

Concepts:
- Sum of triangular numbers
- Binomial coefficient C(n+2, 3)
- Sequence generation
"""

def get_tetrahedral(n: int) -> int:
    """Return the n-th tetrahedral number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (n + 1) * (n + 2) // 6

def is_tetrahedral(val: int) -> bool:
    """Check if val is a tetrahedral number."""
    if val < 1:
        return False
    n = 1
    while True:
        t = get_tetrahedral(n)
        if t == val:
            return True
        if t > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 110: Tetrahedral Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 4),
        (3, 10),
        (4, 20),
        (5, 35),
        (6, 56),
        (7, 84),
    ]

    for n, expected in test_cases:
        res = get_tetrahedral(n)
        print(f"Te({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_tetrahedral(expected) is True

    assert is_tetrahedral(2) is False
    assert is_tetrahedral(5) is False
    assert is_tetrahedral(15) is False

    print("\n[PASS] All Tetrahedral Number tests passed successfully!")
