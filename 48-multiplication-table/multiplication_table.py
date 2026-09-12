"""
Problem 48: Generate Multiplication Table
Difficulty: Beginner / Easy

Problem Statement:
Given an integer n, generate the multiplication table for n from 1 to 10.
Return the results as a list of formatted strings, e.g. "n x i = result".
Also provide a function returning the raw multiples as a list of integers.
Example: n = 5 -> [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

Concepts:
- For loops with range(1, 11)
- String formatting with f-strings
- List comprehensions
"""

from typing import List


def get_multiplication_table(n: int, up_to: int = 10) -> List[int]:
    """Return list of multiples of n up to given count."""
    return [n * i for i in range(1, up_to + 1)]


def format_multiplication_table(n: int, up_to: int = 10) -> List[str]:
    """Return formatted lines: 'n x i = result'."""
    return [f"{n} x {i} = {n * i}" for i in range(1, up_to + 1)]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 48: Multiplication Table Tests")
    print("=" * 50)

    table_5 = get_multiplication_table(5)
    expected_5 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    print(f"Multiples of 5: {table_5}")
    assert table_5 == expected_5

    formatted = format_multiplication_table(3, up_to=3)
    assert formatted == ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9"]
    for line in formatted:
        print(f"  {line}")

    print("\n[PASS] All Multiplication Table tests passed successfully!")
