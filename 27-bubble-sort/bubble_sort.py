"""
Problem 27: Bubble Sort Implementation
Difficulty: Beginner / Easy

Problem Statement:
Implement the Bubble Sort algorithm to sort a list of numbers in ascending order.
Bubble Sort repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order.
Example: [64, 34, 25, 12, 22, 11, 90] -> [11, 12, 22, 25, 34, 64, 90]

Concepts:
- Nested loops and in-place swapping
- Early exit optimization flag
- Cocktail shaker sort bidirectional variant
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Optimized Bubble Sort with early exit flag."""
    nums = arr.copy()
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


def cocktail_shaker_sort(arr: List[int]) -> List[int]:
    """Bidirectional Bubble Sort."""
    nums = arr.copy()
    n = len(nums)
    start = 0
    end = n - 1
    while start < end:
        swapped = False
        for i in range(start, end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        start += 1
        if not swapped:
            break
    return nums


def count_bubble_swaps(arr: List[int]) -> int:
    """
    Sorts a copy of arr and returns total number of adjacent swaps executed.
    """
    nums = arr.copy()
    n = len(nums)
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                swaps += 1
        if not swapped:
            break
    return swaps


if __name__ == "__main__":
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([], []),
        ([42], [42]),
        ([-3, 0, -1, 5, 2], [-3, -1, 0, 2, 5]),
    ]

    for nums, expected in test_cases:
        res = bubble_sort(nums)
        assert res == expected, f"Failed for {nums}"
        assert cocktail_shaker_sort(nums) == expected

    # Test swap count
    assert count_bubble_swaps([1, 2, 3, 4]) == 0
    assert count_bubble_swaps([4, 3, 2, 1]) == 6  # 4*(4-1)/2 = 6

    print("[PASS] Problem 27: Bubble Sort tests passed successfully!")
