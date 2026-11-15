"""
Problem 85: Check Ugly Number
Difficulty: Beginner / Easy

Problem Statement:
An Ugly Number is a positive integer whose prime factors are limited to 2, 3, and 5.
Examples:
  6  = 2 * 3 -> True
  8  = 2 * 2 * 2 -> True
  14 = 2 * 7 (contains 7) -> False
  1  is typically treated as an ugly number -> True

Concepts:
- Prime factor reduction via repeated division
- Divisibility by 2, 3, 5
- While loop factor elimination
"""

def is_ugly(n: int) -> bool:
    """Check if prime factors of n are limited to 2, 3, and 5."""
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1

def get_nth_ugly_number(n: int) -> int:
    """Find the nth ugly number in O(n) time using dynamic programming 3-pointers."""
    if n <= 0:
        return 0
    ugly = [1] * n
    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5
    for i in range(1, n):
        nxt = min(next2, next3, next5)
        ugly[i] = nxt
        if nxt == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if nxt == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if nxt == next5:
            i5 += 1
            next5 = ugly[i5] * 5
    return ugly[-1]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 85: Ugly Number Tests")
    print("=" * 50)

    test_cases = [
        (6, True),
        (8, True),
        (1, True),
        (14, False),
        (7, False),
        (30, True),
        (0, False),
    ]

    for num, expected in test_cases:
        res = is_ugly(num)
        print(f"Num: {num:2d} -> Ugly? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"
    assert [get_nth_ugly_number(i) for i in range(1, 11)] == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

    print("\n[PASS] All Ugly Number tests passed successfully!")
