"""
Problem 99: Check and Calculate Motzkin Numbers
Difficulty: Beginner / Easy

Problem Statement:
The n-th Motzkin number is the number of different ways of drawing non-intersecting
chords between n points on a circle.
Recurrence relation:
  M(0) = 1
  M(1) = 1
  M(n) = M(n-1) + sum(M(k) * M(n-2-k) for k in range(n-1))
First few Motzkin numbers:
  1, 1, 2, 4, 9, 21, 51, 127, 323, 835, ...

Concepts:
- Combinatorics counting
- 1D dynamic programming memoization
- Sequence membership test
"""

def get_motzkin_number(n: int) -> int:
    """Calculate the n-th Motzkin number using dynamic programming."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1]
        for k in range(i - 1):
            dp[i] += dp[k] * dp[i - 2 - k]

    return dp[n]

def is_motzkin_number(val: int) -> bool:
    """Check if val belongs to the Motzkin sequence."""
    if val < 1:
        return False
    n = 0
    while True:
        m = get_motzkin_number(n)
        if m == val:
            return True
        if m > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 99: Motzkin Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 9),
        (5, 21),
        (6, 51),
        (7, 127),
    ]

    for n, expected in test_cases:
        res = get_motzkin_number(n)
        print(f"M({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_motzkin_number(expected) is True

    assert is_motzkin_number(3) is False
    assert is_motzkin_number(10) is False

    print("\n[PASS] All Motzkin Number tests passed successfully!")
