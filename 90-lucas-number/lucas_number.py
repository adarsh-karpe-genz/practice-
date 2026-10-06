"""
Problem 90: Check and Generate Lucas Numbers
Difficulty: Beginner / Easy

Problem Statement:
Lucas numbers follow the same recurrence relation as Fibonacci numbers
(L(n) = L(n-1) + L(n-2)), but with different base cases:
  L(0) = 2
  L(1) = 1
First few Lucas numbers: 2, 1, 3, 4, 7, 11, 18, 29, 47, ...
Given an integer, check if it belongs to the Lucas sequence.

Concepts:
- Sequence generation with custom initial conditions
- Iterative loop comparison
- Dynamic programming / accumulator
"""

def get_lucas_number(n: int) -> int:
    """Return the n-th Lucas number."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_lucas_number(val: int) -> bool:
    """Check if val is present in the Lucas sequence."""
    if val < 1 and val != 2:
        return False
    if val == 2 or val == 1:
        return True
    a, b = 2, 1
    while b < val:
        a, b = b, a + b
    return b == val

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 90: Lucas Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 2),
        (1, 1),
        (2, 3),
        (3, 4),
        (4, 7),
        (5, 11),
        (6, 18),
    ]

    for n, expected in test_cases:
        res = get_lucas_number(n)
        print(f"L({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_lucas_number(expected) is True

    assert is_lucas_number(5) is False
    assert is_lucas_number(6) is False
    assert is_lucas_number(29) is True

    print("\n[PASS] All Lucas Number tests passed successfully!")
