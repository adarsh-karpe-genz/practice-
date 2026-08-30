"""
Problem 08: Fibonacci Sequence Generator
Difficulty: Beginner / Easy

Problem Statement:
The Fibonacci sequence is a series of numbers where each number is the sum
of the two preceding ones, starting from 0 and 1.
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Concepts:
- Iterative list building
- Tuple unpacking in Python (a, b = b, a + b)
"""

from typing import List


def generate_fibonacci(n_terms: int) -> List[int]:
    """Generate the first `n_terms` of the Fibonacci sequence."""
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n_terms):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    print("Generating first 8 Fibonacci numbers:")
    print(generate_fibonacci(8))
