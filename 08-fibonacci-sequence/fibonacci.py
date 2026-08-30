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


def generate_fibonacci(n_terms: int) -> List[int]:
    """Method 1: Generate the first `n_terms` using an iterative list."""
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n_terms):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def nth_fibonacci_iterative(n: int) -> int:
    """Method 2: Compute Nth Fibonacci number in O(N) time and O(1) space."""
    if n < 0:
        raise ValueError("Index n must be non-negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def nth_fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """Method 3: Top-Down Dynamic Programming with Memoization."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1

    memo[n] = nth_fibonacci_memo(n - 1, memo) + nth_fibonacci_memo(n - 2, memo)
    return memo[n]


# ==============================================================================
# Comprehensive Unit Test Harness
# ==============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("Running Problem 08: Fibonacci Sequence Tests")
    print("=" * 55)

    # 1. Test sequence generator
    seq_tests = [
        (0, []),
        (1, [0]),
        (5, [0, 1, 1, 2, 3]),
        (8, [0, 1, 1, 2, 3, 5, 8, 13]),
    ]
    for terms, expected in seq_tests:
        res = generate_fibonacci(terms)
        print(f"generate_fibonacci({terms}) -> {res} | Expected: {expected}")
        assert res == expected, f"Failed for {terms} terms"

    # 2. Test Nth Fibonacci methods
    nth_tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (6, 8),
        (10, 55),
        (15, 610),
    ]
    print("\nTesting Nth Fibonacci calculations:")
    for n_val, expected in nth_tests:
        r_iter = nth_fibonacci_iterative(n_val)
        r_memo = nth_fibonacci_memo(n_val)
        print(f"F({n_val:2d}) -> Iterative: {r_iter:<4} | Memo: {r_memo:<4} | Expected: {expected}")
        assert r_iter == expected
        assert r_memo == expected

    # 3. Test negative index exception handling
    try:
        nth_fibonacci_iterative(-3)
    except ValueError:
        print("\nNegative index validation test: [PASS]")

    print("\n[PASS] All Fibonacci tests passed successfully!")
