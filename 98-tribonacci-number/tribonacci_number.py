"""
Problem 98: Check Tribonacci Number
Difficulty: Beginner / Easy

Problem Statement:
The Tribonacci sequence is a generalization of Fibonacci where each term
is the sum of the preceding three terms:
  T(0) = 0, T(1) = 1, T(2) = 1
  T(n) = T(n - 1) + T(n - 2) + T(n - 3) for n >= 3
First few terms:
  0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, ...

Concepts:
- Sum of three previous terms
- Tuple multiple assignment
- Membership checking
"""

def get_tribonacci_number(n: int) -> int:
    """Return the n-th Tribonacci number."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1

    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c

def is_tribonacci_number(val: int) -> bool:
    """Check if val belongs to the Tribonacci sequence."""
    if val < 0:
        return False
    if val in (0, 1):
        return True
    a, b, c = 0, 1, 1
    while c < val:
        a, b, c = b, c, a + b + c
    return c == val

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 98: Tribonacci Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 7),
        (6, 13),
        (7, 24),
        (8, 44),
    ]

    for n, expected in test_cases:
        res = get_tribonacci_number(n)
        print(f"T({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_tribonacci_number(expected) is True

    assert is_tribonacci_number(3) is False
    assert is_tribonacci_number(5) is False
    assert is_tribonacci_number(6) is False

    print("\n[PASS] All Tribonacci Number tests passed successfully!")
