"""
Problem 115: Check Icosahedral Number
Difficulty: Beginner / Easy

Problem Statement:
An icosahedral number is a figurate number that represents a regular icosahedron
(20-faced regular polyhedron).
Formula:
  I(n) = n(5n^2 - 5n + 2) // 2, for n >= 1.
First few icosahedral numbers:
  n = 1 -> 1
  n = 2 -> 2 * (20 - 10 + 2) // 2 = 12
  n = 3 -> 3 * (45 - 15 + 2) // 2 = 48
  n = 4 -> 4 * (80 - 20 + 2) // 2 = 124
  n = 5 -> 5 * (125 - 25 + 2) // 2 = 255

Concepts:
- 20-faced Platonic solid figurate representation
- Cubic formula calculation
- Sequence membership test
"""

def get_icosahedral_number(n: int) -> int:
    """Return the n-th icosahedral number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (5 * n * n - 5 * n + 2) // 2

def is_icosahedral_number(val: int) -> bool:
    """Check if val is an icosahedral number."""
    if val < 1:
        return False
    n = 1
    while True:
        i = get_icosahedral_number(n)
        if i == val:
            return True
        if i > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 115: Icosahedral Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 12),
        (3, 48),
        (4, 124),
        (5, 255),
    ]

    for n, expected in test_cases:
        res = get_icosahedral_number(n)
        print(f"I({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_icosahedral_number(expected) is True

    assert is_icosahedral_number(2) is False
    assert is_icosahedral_number(20) is False
    assert is_icosahedral_number(50) is False

    print("\n[PASS] All Icosahedral Number tests passed successfully!")
