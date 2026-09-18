"""
Problem 64: Symmetric Difference of Two Lists
Difficulty: Beginner / Easy

Problem Statement:
Given two lists, find their symmetric difference: the set of elements
that are in either of the lists, but NOT in both.
Return the result as a sorted list with unique items.
Example: list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6]
         -> [1, 2, 5, 6]

Concepts:
- Set symmetric difference operator (^)
- set1.symmetric_difference(set2)
- Sorted deduplicated output
"""

from typing import List


def symmetric_difference(list1: List[int], list2: List[int]) -> List[int]:
    """Return sorted unique elements present in either list1 or list2, but not both."""
    return sorted(set(list1) ^ set(list2))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 64: Symmetric Difference Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4], [3, 4, 5, 6], [1, 2, 5, 6]),
        ([1, 2], [1, 2], []),
        ([], [1, 2], [1, 2]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([10, 20, 30], [20, 40], [10, 30, 40]),
    ]

    for l1, l2, expected in test_cases:
        res = symmetric_difference(l1, l2)
        print(f"Lists: {l1} & {l2} -> Sym Diff: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {l1}, {l2}"

    print("\n[PASS] All Symmetric Difference tests passed successfully!")
