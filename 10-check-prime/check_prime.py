"""
Problem 10: Check Prime Number
Difficulty: Beginner / Easy

Problem Statement:
Given an integer `n`, determine whether it is a Prime Number.
A prime number is a natural number greater than 1 that has no positive divisors
other than 1 and itself.
Examples of Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23
Examples of Non-Primes: 0, 1, 4, 6, 8, 9, 10

Concepts:
- Trial division optimization up to sqrt(n) (O(sqrt(N)) time complexity)
- Handling edge cases (n <= 1, n = 2, even numbers)
"""

import math


def is_prime(n: int) -> bool:
    """Check if n is prime in O(sqrt(N)) time."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False  # all other even numbers are composite

    # Check odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 10: Check Prime Number Tests")
    print("=" * 50)

    test_cases = [
        (-7, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (25, False),
        (29, True),
        (97, True),
        (100, False),
    ]

    for num, expected in test_cases:
        res = is_prime(num)
        print(f"Number: {num:3d} -> Prime? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Prime Number tests passed successfully!")
