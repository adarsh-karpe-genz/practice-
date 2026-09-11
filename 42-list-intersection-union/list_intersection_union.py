"""
Problem 42: List Intersection and Union
Difficulty: Beginner / Easy

Problem Statement:
Given two lists, compute:
1. Intersection: elements present in BOTH lists (no duplicates).
2. Union: all unique elements from BOTH lists combined.
Examples:
  list1 = [1, 2, 3, 4, 5]
  list2 = [3, 4, 5, 6, 7]
  Intersection -> [3, 4, 5]
  Union        -> [1, 2, 3, 4, 5, 6, 7]

Concepts:
- Python set operations: & (intersection), | (union)
- Manual loop with membership check (in) for O(N*M) approach
- Sorted output for consistent results
"""

from typing import List


def intersection(list1: List[int], list2: List[int]) -> List[int]:
    """Return sorted list of elements common to both lists (no duplicates)."""
    return sorted(set(list1) & set(list2))


def union(list1: List[int], list2: List[int]) -> List[int]:
    """Return sorted list of all unique elements from both lists."""
    return sorted(set(list1) | set(list2))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 42: Intersection & Union Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [3, 4, 5], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 1, 2], [2, 2, 3], [2], [1, 2, 3]),
        ([], [1, 2], [], [1, 2]),
        ([5, 6], [], [], [5, 6]),
        ([1, 2], [1, 2], [1, 2], [1, 2]),
    ]

    for l1, l2, exp_inter, exp_union in test_cases:
        res_inter = intersection(l1, l2)
        res_union = union(l1, l2)
        print(f"list1={l1}, list2={l2}")
        print(f"  Intersection: {res_inter} | Expected: {exp_inter}")
        print(f"  Union:        {res_union} | Expected: {exp_union}")
        assert res_inter == exp_inter, f"Intersection failed"
        assert res_union == exp_union, f"Union failed"

    print("\n[PASS] All Intersection & Union tests passed successfully!")
