"""
Problem 67: Find Difference of Two Lists (Elements in A not in B)
Difficulty: Beginner / Easy

Problem Statement:
Given two lists A and B, return all unique elements that are present in A
but NOT present in B. Return the result sorted.
Example: A = [1, 2, 3, 4, 5], B = [2, 4, 6] -> [1, 3, 5]

Concepts:
- Set difference operator (-)
- Converting lists to sets and back
- Preserving uniqueness and sorting
"""

from typing import List


def list_difference(a: List[int], b: List[int]) -> List[int]:
    """Find unique elements in a that are not in b."""
    return sorted(set(a) - set(b))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 67: List Difference Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4, 5], [2, 4, 6], [1, 3, 5]),
        ([1, 2, 3], [1, 2, 3], []),
        ([], [1, 2], []),
        ([1, 2, 3], [], [1, 2, 3]),
        ([5, 5, 6, 7], [6], [5, 7]),
    ]

    for a, b, expected in test_cases:
        res = list_difference(a, b)
        print(f"A={a}, B={b} -> A - B: {res} | Expected: {expected}")
        assert res == expected, f"Failed for A={a}, B={b}"

    print("\n[PASS] All List Difference tests passed successfully!")
