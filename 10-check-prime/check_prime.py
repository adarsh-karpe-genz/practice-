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
    """Trial division optimized to 6k +/- 1 check."""
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_primes(limit: int) -> list[int]:
    """Sieve of Eratosthenes generating all primes up to limit."""
    if limit < 2:
        return []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [i for i, prime in enumerate(is_p) if prime]


def prime_factors(n: int) -> list[int]:
    """Returns the prime factorization of positive integer n as a sorted list."""
    if n <= 1:
        return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


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
        assert is_prime(num) == expected

    assert sieve_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Test prime factors
    assert prime_factors(60) == [2, 2, 3, 5]
    assert prime_factors(13) == [13]
    assert prime_factors(1) == []

    print("[PASS] All Prime Number tests passed successfully!")
