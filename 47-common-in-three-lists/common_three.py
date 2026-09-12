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

    print("\n[PASS] All Common in Three Lists tests passed successfully!")
