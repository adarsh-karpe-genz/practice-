"""
Problem 95: Calculate and Check Bell Numbers
Difficulty: Beginner / Easy

Problem Statement:
The n-th Bell number, B_n, is the number of partitions of a set of size n.
First few Bell numbers for n = 0, 1, 2, 3, 4, 5:
  B(0) = 1
  B(1) = 1
  B(2) = 2
  B(3) = 5
  B(4) = 15
  B(5) = 52
Generated using the Bell Triangle.

Concepts:
- Bell Triangle 2D dynamic programming
- Combinatorics partitions
- Sequence lookup
"""

def get_bell_number(n: int) -> int:
    """Calculate the n-th Bell number using Bell Triangle."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1

    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1

    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

    return bell[n][0]

def is_bell_number(val: int) -> bool:
    """Check if val is a Bell number."""
    if val < 1:
        return False
    n = 0
    while True:
        b = get_bell_number(n)
        if b == val:
            return True
        if b > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 95: Bell Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 15),
        (5, 52),
    ]

    for n, expected in test_cases:
        res = get_bell_number(n)
        print(f"B({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_bell_number(expected) is True

    assert is_bell_number(3) is False
    assert is_bell_number(10) is False

    print("\n[PASS] All Bell Number tests passed successfully!")
