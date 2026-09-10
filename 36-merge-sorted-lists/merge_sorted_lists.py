"""
Problem 36: Merge Two Sorted Lists
Difficulty: Beginner / Easy

Problem Statement:
Given two sorted lists of integers, merge them into a single sorted list.
The merged list must remain sorted.
Example:
  list1 = [1, 3, 5, 7]
  list2 = [2, 4, 6, 8]
  Result -> [1, 2, 3, 4, 5, 6, 7, 8]

Concepts:
- Two-pointer technique for linear merge (O(M+N) time, O(M+N) space)
- Handling remaining elements after one list is exhausted
- Pythonic sorted() merge as a shortcut
"""

from typing import List


def merge_sorted_two_pointers(list1: List[int], list2: List[int]) -> List[int]:
    """Method 1: Two-pointer linear merge (O(M+N) time)"""
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def merge_sorted_pythonic(list1: List[int], list2: List[int]) -> List[int]:
    """Method 2: Pythonic approach using sorted()"""
    return sorted(list1 + list2)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 36: Merge Sorted Lists Tests")
    print("=" * 50)

    test_cases = [
        ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [4, 5, 6], [4, 5, 6]),
        ([], [], []),
        ([1], [1], [1, 1]),
        ([-5, 0, 3], [-2, 1, 4], [-5, -2, 0, 1, 3, 4]),
    ]

    for l1, l2, expected in test_cases:
        r1 = merge_sorted_two_pointers(l1, l2)
        r2 = merge_sorted_pythonic(l1, l2)
        print(f"list1={l1}, list2={l2} -> {r1} | Expected: {expected}")
        assert r1 == expected, f"Two-pointer failed"
        assert r2 == expected, f"Pythonic failed"

    print("\n[PASS] All Merge Sorted Lists tests passed successfully!")
