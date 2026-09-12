"""
Problem 45: Check if a List is Sorted
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, check if it is sorted in non-decreasing (ascending) order.
An empty list or single-element list is considered sorted.
Example: [1, 2, 2, 4, 5] -> True
Example: [1, 3, 2, 4] -> False

Concepts:
- Pairwise comparison in a loop (nums[i] <= nums[i+1])
- Early exit optimization
- all() with zip() or list comprehension
"""

from typing import List


def is_sorted_loop(nums: List[int]) -> bool:
    """Check if list is sorted using adjacent loop comparison (O(N) time, O(1) space)."""
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def is_sorted_pythonic(nums: List[int]) -> bool:
    """Check using all() and zip()."""
    return all(x <= y for x, y in zip(nums, nums[1:]))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 45: Check Sorted List Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4, 5], True),
        ([1, 2, 2, 3, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([1, 3, 2, 4], False),
        ([], True),
        ([42], True),
        ([-10, -5, 0, 5, 10], True),
    ]

    for nums, expected in test_cases:
        r1 = is_sorted_loop(nums)
        r2 = is_sorted_pythonic(nums)
        print(f"List: {nums} -> Sorted? {r1} | Expected: {expected}")
        assert r1 == expected and r2 == expected

    print("\n[PASS] All Check Sorted List tests passed successfully!")
