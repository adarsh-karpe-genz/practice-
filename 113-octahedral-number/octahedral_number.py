"""
Problem 113: Check Octahedral Number
Difficulty: Beginner / Easy

Problem Statement:
An octahedral number is a figurate number that represents the number of spheres
in an octahedron.
Formula:
  O(n) = n(2n^2 + 1) // 3, for n >= 1.
First few octahedral numbers:
  n = 1 -> 1
  n = 2 -> 6
  n = 3 -> 19
  n = 4 -> 44
  n = 5 -> 85
  n = 6 -> 146

Concepts:
- Polyhedral figurate numbers
- Cubic growth rate
- Verification via sequence traversal
"""

def get_octahedral_number(n: int) -> int:
    """Return the n-th octahedral number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (2 * n * n + 1) // 3

def is_octahedral_number(val: int) -> bool:
    """Check if val is an octahedral number."""
    if val < 1:
        return False
    n = 1
    while True:
        o = get_octahedral_number(n)
        if o == val:
            return True
        if o > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 113: Octahedral Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 6),
        (3, 19),
        (4, 44),
        (5, 85),
        (6, 146),
    ]

    for n, expected in test_cases:
        res = get_octahedral_number(n)
        print(f"O({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_octahedral_number(expected) is True

    assert is_octahedral_number(2) is False
    assert is_octahedral_number(7) is False
    assert is_octahedral_number(50) is False

    print("\n[PASS] All Octahedral Number tests passed successfully!")
