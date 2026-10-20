"""
Problem 114: Check Dodecahedral Number
Difficulty: Beginner / Easy

Problem Statement:
A dodecahedral number is a figurate number that represents a regular dodecahedron
(12-faced regular polyhedron).
Formula:
  D(n) = n(3n - 1)(3n - 2) // 2, for n >= 1.
First few dodecahedral numbers:
  n = 1 -> 1
  n = 2 -> 2 * 5 * 4 // 2 = 20
  n = 3 -> 3 * 8 * 7 // 2 = 84
  n = 4 -> 4 * 11 * 10 // 2 = 220
  n = 5 -> 5 * 14 * 13 // 2 = 455

Concepts:
- Platonic solid figurate numbers
- Polynomial sequence generation
- Searching sequence values
"""

def get_dodecahedral_number(n: int) -> int:
    """Return the n-th dodecahedral number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (3 * n - 1) * (3 * n - 2) // 2

def is_dodecahedral_number(val: int) -> bool:
    """Check if val is a dodecahedral number."""
    if val < 1:
        return False
    n = 1
    while True:
        d = get_dodecahedral_number(n)
        if d == val:
            return True
        if d > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 114: Dodecahedral Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 20),
        (3, 84),
        (4, 220),
        (5, 455),
    ]

    for n, expected in test_cases:
        res = get_dodecahedral_number(n)
        print(f"D({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_dodecahedral_number(expected) is True

    assert is_dodecahedral_number(2) is False
    assert is_dodecahedral_number(15) is False
    assert is_dodecahedral_number(50) is False

    print("\n[PASS] All Dodecahedral Number tests passed successfully!")
