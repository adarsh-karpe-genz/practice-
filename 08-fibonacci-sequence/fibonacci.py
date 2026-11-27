"""
Problem 08: Fibonacci Sequence & Nth Fibonacci Number
Difficulty: Beginner / Easy

Problem Statement:
The Fibonacci sequence is a series of numbers where each number is the sum
of the two preceding ones, starting from 0 and 1.
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Concepts Covered:
1. Iterative list generation
2. Space-optimized Nth Fibonacci calculation (O(1) space)
3. Memoized Dynamic Programming / Recursion
4. Robust unit test assertions and input validation
"""

from typing import List, Dict


def fibonacci_series(n: int) -> List[int]:
    """Generates the first n numbers of the Fibonacci series."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series


def nth_fibonacci_iterative(n: int) -> int:
    """Returns the n-th Fibonacci number in O(n) time and O(1) space."""
    if n < 0:
        raise ValueError("Index must be non-negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def nth_fibonacci_memo(n: int, memo: Dict[int, int] | None = None) -> int:
    """Returns the n-th Fibonacci number using top-down Dynamic Programming."""
    if n < 0:
        raise ValueError("Index must be non-negative.")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = nth_fibonacci_memo(n - 1, memo) + nth_fibonacci_memo(n - 2, memo)
    return memo[n]


def nth_fibonacci_binet(n: int) -> int:
    """Closed-form Binet formula for Fibonacci numbers."""
    if n < 0:
        raise ValueError("Index must be non-negative.")
    phi = (1 + 5 ** 0.5) / 2
    return round((phi ** n) / (5 ** 0.5))


def fibonacci_matrix_power(n: int) -> int:
    """
    Computes F(n) in O(log n) time using 2x2 matrix exponentiation:
    [[1, 1], [1, 0]]^n = [[F(n+1), F(n)], [F(n), F(n-1)]].
    """
    if n < 0:
        raise ValueError("Index must be non-negative.")
    if n == 0:
        return 0

    def mat_mult(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def mat_pow(M: list[list[int]], p: int) -> list[list[int]]:
        res = [[1, 0], [0, 1]]
        base = M
        while p > 0:
            if p % 2 == 1:
                res = mat_mult(res, base)
            base = mat_mult(base, base)
            p //= 2
        return res

    T = [[1, 1], [1, 0]]
    result = mat_pow(T, n)
    return result[0][1]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 08: Fibonacci Tests")
    print("=" * 50)

    nth_tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (6, 8),
        (10, 55),
        (15, 610),
    ]

    for n_val, expected in nth_tests:
        assert nth_fibonacci_iterative(n_val) == expected
        assert nth_fibonacci_memo(n_val) == expected
        assert nth_fibonacci_binet(n_val) == expected
        assert fibonacci_matrix_power(n_val) == expected

    print("[PASS] All Fibonacci tests passed successfully!")
