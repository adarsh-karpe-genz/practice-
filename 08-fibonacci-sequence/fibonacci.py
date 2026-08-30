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


if __name__ == "__main__":
    print("First 8 terms:", generate_fibonacci(8))
    print("10th Fibonacci (Iterative):", nth_fibonacci_iterative(10))
    print("10th Fibonacci (Memoized):", nth_fibonacci_memo(10))
