"""
Problem 96: Check Perrin Number
Difficulty: Beginner / Easy

Problem Statement:
The Perrin sequence is defined by recurrence:
  P(0) = 3, P(1) = 0, P(2) = 2
  P(n) = P(n - 2) + P(n - 3) for n >= 3
First few Perrin numbers:
  3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, ...

Concepts:
- Third-order linear recurrence
- Sliding window / list simulation
- Sequence membership test
"""

def get_perrin_number(n: int) -> int:
    """Return the n-th Perrin number."""
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2

    p0, p1, p2 = 3, 0, 2
    for _ in range(3, n + 1):
        p_next = p1 + p0
        p0, p1, p2 = p1, p2, p_next
    return p2

def is_perrin_number(val: int) -> bool:
    """Check if val belongs to the Perrin sequence."""
    if val < 0:
        return False
    if val in (3, 0, 2):
        return True
    p0, p1, p2 = 3, 0, 2
    while p2 < val:
        p_next = p1 + p0
        p0, p1, p2 = p1, p2, p_next
        if p2 == val:
            return True
    return False

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 96: Perrin Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 3),
        (1, 0),
        (2, 2),
        (3, 3),
        (4, 2),
        (5, 5),
        (6, 5),
        (7, 7),
        (8, 10),
        (9, 12),
        (10, 17),
    ]

    for n, expected in test_cases:
        res = get_perrin_number(n)
        print(f"P({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_perrin_number(expected) is True

    assert is_perrin_number(4) is False
    assert is_perrin_number(6) is False

    print("\n[PASS] All Perrin Number tests passed successfully!")
