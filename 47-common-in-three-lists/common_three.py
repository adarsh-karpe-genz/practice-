"""
Problem 47: Find Common Elements in Three Lists
Difficulty: Beginner / Easy

Problem Statement:
Given three lists of integers, find all unique elements that appear in all three lists.
Return the result as a sorted list.
Example:
  l1 = [1, 5, 10, 20, 40, 80]
  l2 = [6, 7, 20, 80, 100]
  l3 = [3, 4, 15, 20, 30, 70, 80, 120]
  Result -> [20, 80]

Concepts:
- Set intersection operation set.intersection() or &
- Type conversions (list to set and back)
- Sorting the final result
"""

from typing import List


def common_in_three_lists(l1: List[int], l2: List[int], l3: List[int]) -> List[int]:
    """Find unique common elements in three lists using set intersection."""
    return sorted(set(l1) & set(l2) & set(l3))


def common_in_three_sorted(l1: list, l2: list, l3: list) -> list:
    """Find common elements in three sorted lists in O(n1 + n2 + n3) using 3 pointers."""
    i, j, k = 0, 0, 0
    common = []
    while i < len(l1) and j < len(l2) and k < len(l3):
        if l1[i] == l2[j] == l3[k]:
            if not common or common[-1] != l1[i]:
                common.append(l1[i])
            i += 1
            j += 1
            k += 1
        elif l1[i] < l2[j]:
            i += 1
        elif l2[j] < l3[k]:
            j += 1
        else:
            k += 1
    return common


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 47: Common in Three Lists Tests")
    print("=" * 50)

    l1 = [1, 5, 10, 20, 40, 80]
    l2 = [6, 7, 20, 80, 100]
    l3 = [3, 4, 15, 20, 30, 70, 80, 120]
    res = common_in_three_lists(l1, l2, l3)
    print(f"Common: {res} | Expected: [20, 80]")
    assert res == [20, 80]

    # No common elements
    assert common_in_three_lists([1, 2], [3, 4], [5, 6]) == []

    # All identical
    assert common_in_three_lists([1, 2, 3], [1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert common_in_three_sorted([1, 5, 10, 20], [5, 10, 20], [5, 20]) == [5, 20]

    print("\n[PASS] All Common in Three Lists tests passed successfully!")
