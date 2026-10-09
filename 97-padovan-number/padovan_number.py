"""
Problem 97: Check Padovan Number
Difficulty: Beginner / Easy

Problem Statement:
The Padovan sequence is defined by recurrence:
  P(0) = 1, P(1) = 1, P(2) = 1
  P(n) = P(n - 2) + P(n - 3) for n >= 3
First few terms:
  1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, ...

Concepts:
- Third-order linear recurrence
- Plastic number connection
- Dynamic sequence generation
"""

def get_padovan_number(n: int) -> int:
    """Return the n-th Padovan number."""
    if n in (0, 1, 2):
        return 1

    p0, p1, p2 = 1, 1, 1
    for _ in range(3, n + 1):
        p_next = p1 + p0
        p0, p1, p2 = p1, p2, p_next
    return p2

def is_padovan_number(val: int) -> bool:
    """Check if val belongs to the Padovan sequence."""
    if val < 1:
        return False
    if val == 1:
        return True
    p0, p1, p2 = 1, 1, 1
    while p2 < val:
        p_next = p1 + p0
        p0, p1, p2 = p1, p2, p_next
        if p2 == val:
            return True
    return False

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 97: Padovan Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 4),
        (7, 5),
        (8, 7),
        (9, 9),
        (10, 12),
    ]

    for n, expected in test_cases:
        res = get_padovan_number(n)
        print(f"P({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_padovan_number(expected) is True

    assert is_padovan_number(6) is False
    assert is_padovan_number(8) is False

    print("\n[PASS] All Padovan Number tests passed successfully!")
