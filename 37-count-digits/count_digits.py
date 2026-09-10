"""
Problem 37: Count Digits in a Number
Difficulty: Beginner / Easy

Problem Statement:
Given an integer, count the number of digits it contains.
Negative numbers have the same digit count as their positive equivalents.
Examples:
  12345  -> 5
  -987   -> 3
  0      -> 1

Concepts:
- Division loop to extract digits (O(log10(N)) time)
- len(str(abs(n))) shortcut
- math.floor(math.log10(n)) + 1 formula (for n > 0)
"""

import math


def count_digits_loop(n: int) -> int:
    """Method 1: Division loop (O(log10(N)) time)"""
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def count_digits_string(n: int) -> int:
    """Method 2: String conversion (Pythonic)"""
    return len(str(abs(n)))


def count_digits_math(n: int) -> int:
    """Method 3: Math formula (O(1) time, only for n != 0)"""
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n))) + 1


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 37: Count Digits Tests")
    print("=" * 50)

    test_cases = [
        (12345, 5),
        (-987, 3),
        (0, 1),
        (1, 1),
        (100, 3),
        (999999999, 9),
    ]

    for num, expected in test_cases:
        r1 = count_digits_loop(num)
        r2 = count_digits_string(num)
        r3 = count_digits_math(num)
        print(f"Number: {num:12d} -> Digits: {r1} | Expected: {expected}")
        assert r1 == expected, f"Loop failed for {num}"
        assert r2 == expected, f"String failed for {num}"
        assert r3 == expected, f"Math failed for {num}"

    print("\n[PASS] All Count Digits tests passed successfully!")
