"""
Problem 86: Calculate and Check Catalan Number
Difficulty: Beginner / Easy

Problem Statement:
Catalan numbers are a sequence of natural numbers that occur in various
counting problems, often involving recursively-defined objects.
The n-th Catalan number is given by:
  C(n) = (2n)! / ((n + 1)! * n!)
First few Catalan numbers for n = 0, 1, 2, 3, 4, 5 are:
  1, 1, 2, 5, 14, 42

Concepts:
- math.factorial formula application
- Integer division
- Combinatorics counting
"""

import math

def get_catalan_number(n: int) -> int:
    """Calculate the n-th Catalan number using factorial formula."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))

def is_catalan_number(val: int) -> bool:
    """Check if a given positive integer is a Catalan number."""
    if val < 1:
        return False
    n = 0
    while True:
        c = get_catalan_number(n)
        if c == val:
            return True
        if c > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 86: Catalan Number Tests")
    print("=" * 50)

    test_cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 14),
        (5, 42),
        (6, 132),
    ]

    for n, expected in test_cases:
        res = get_catalan_number(n)
        print(f"n = {n} -> C(n) = {res} | Expected: {expected}")
        assert res == expected
        assert is_catalan_number(expected) is True

    assert is_catalan_number(7) is False
    assert is_catalan_number(10) is False

    print("\n[PASS] All Catalan Number tests passed successfully!")
