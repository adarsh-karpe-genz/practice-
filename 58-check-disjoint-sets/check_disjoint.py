"""
Problem 58: Check if Two Sets are Disjoint
Difficulty: Beginner / Easy

Problem Statement:
Two sets are disjoint if they have no common elements (their intersection is empty).
Given two lists, determine if they are disjoint.
Example: [1, 2, 3] and [4, 5, 6] -> True
Example: [1, 2, 3] and [3, 4, 5] -> False

Concepts:
- Python set.isdisjoint() method
- Set conversion and intersection
- Loop with hash set lookup O(N + M)
"""

from typing import List, Any


def are_disjoint(list1: List[Any], list2: List[Any]) -> bool:
    """Check if two lists share no common elements."""
    set1 = set(list1)
    return set1.isdisjoint(list2)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 58: Disjoint Sets Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3], [4, 5, 6], True),
        ([1, 2, 3], [3, 4, 5], False),
        ([], [1, 2], True),
        (["a", "b"], ["c", "d"], True),
        (["apple", "banana"], ["banana", "orange"], False),
    ]

    for l1, l2, expected in test_cases:
        res = are_disjoint(l1, l2)
        print(f"Lists: {l1} & {l2} -> Disjoint? {res} | Expected: {expected}")
        assert res == expected, f"Failed for {l1}, {l2}"

    print("\n[PASS] All Disjoint Sets tests passed successfully!")
