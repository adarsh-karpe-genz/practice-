"""
Problem 25: Binary Search Algorithm
Difficulty: Beginner / Easy

Problem Statement:
Given a SORTED list of integers and a target value, use the Binary Search
algorithm to find the index of the target. Return -1 if not found.
Example: nums = [2, 5, 8, 12, 16, 23, 38, 56], target = 23 -> Returns 5

Concepts:
- Divide and conquer approach (O(log N) time, O(1) space for iterative)
- Mid-point calculation: mid = left + (right - left) // 2
- Three-way comparison: found / go left / go right
"""

from typing import List


def binary_search_iterative(nums: List[int], target: int) -> int:
    """Method 1: Iterative Binary Search (O(log N) time, O(1) space)"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(nums: List[int], target: int, left: int = 0, right: int = None) -> int:
    """Method 2: Recursive Binary Search (O(log N) time, O(log N) stack space)"""
    if right is None:
        right = len(nums) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 25: Binary Search Tests")
    print("=" * 50)

    nums = [2, 5, 8, 12, 16, 23, 38, 56]
    test_cases = [
        (23, 5),
        (2, 0),
        (56, 7),
        (10, -1),
        (38, 6),
    ]

    for target, expected in test_cases:
        r1 = binary_search_iterative(nums, target)
        r2 = binary_search_recursive(nums, target)
        print(f"Target: {target:3d} -> Index: {r1:<2} | Expected: {expected:<2}")
        assert r1 == expected, f"Iterative failed for target {target}"
        assert r2 == expected, f"Recursive failed for target {target}"

    # Edge cases
    assert binary_search_iterative([], 5) == -1
    assert binary_search_iterative([7], 7) == 0
    assert binary_search_iterative([7], 1) == -1

    print("\n[PASS] All Binary Search tests passed successfully!")
