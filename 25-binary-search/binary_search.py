"""
Problem 25: Binary Search Algorithm
Difficulty: Beginner / Easy

Problem Statement:
Given a SORTED list of integers and a target value, use the Binary Search
algorithm to find the index of the target. Return -1 if not found.
Example: nums = [2, 5, 8, 12, 16, 23, 38, 56], target = 23 -> Returns 5

Time Complexity: O(log N)
Space Complexity: O(1) iterative / O(log N) recursive
"""

from typing import List


def binary_search_iterative(nums: List[int], target: int) -> int:
    """Iterative Binary Search."""
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(nums: List[int], target: int) -> int:
    """Recursive Binary Search."""
    def _search(low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return _search(mid + 1, high)
        else:
            return _search(low, mid - 1)
    return _search(0, len(nums) - 1)


def search_insert_position(nums: List[int], target: int) -> int:
    """Finds index where target should be inserted to maintain sorted order."""
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


def binary_search_range(nums: List[int], target: int) -> tuple[int, int]:
    """
    Finds first and last position of target in sorted array nums.
    Returns (-1, -1) if target is not present.
    """
    def find_bound(is_first: bool) -> int:
        low, high = 0, len(nums) - 1
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                if is_first:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

    return (find_bound(True), find_bound(False))


if __name__ == "__main__":
    nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    targets = [
        (23, 5),
        (2, 0),
        (91, 9),
        (50, -1),
        (1, -1),
        (100, -1),
    ]

    for target, expected in targets:
        r1 = binary_search_iterative(nums, target)
        r2 = binary_search_recursive(nums, target)
        assert r1 == expected, f"Iterative failed for target {target}"
        assert r2 == expected, f"Recursive failed for target {target}"

    assert binary_search_iterative([], 5) == -1
    assert search_insert_position([1, 3, 5, 6], 5) == 2
    assert search_insert_position([1, 3, 5, 6], 2) == 1

    # Test search range
    dup_nums = [5, 7, 7, 8, 8, 10]
    assert binary_search_range(dup_nums, 8) == (3, 4)
    assert binary_search_range(dup_nums, 6) == (-1, -1)

    print("[PASS] Problem 25: Binary Search tests passed successfully!")
