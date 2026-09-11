"""
Problem 38: Selection Sort Implementation
Difficulty: Beginner / Easy

Problem Statement:
Implement the Selection Sort algorithm to sort a list in ascending order.
Selection Sort divides the list into a sorted and an unsorted part.
In each pass, it finds the minimum element from the unsorted part and
places it at the beginning of that part.
Example: [64, 25, 12, 22, 11] -> [11, 12, 22, 25, 64]

Complexity: O(N^2) time (all cases), O(1) space (in-place)

Concepts:
- Two nested loops: outer for sorted boundary, inner to find minimum
- Index tracking to locate the minimum element
- Swap only when a new minimum is found
"""

from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    """Selection Sort - O(N^2) time, O(1) space (in-place on a copy)."""
    arr = nums[:]
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 38: Selection Sort Tests")
    print("=" * 50)

    test_cases = [
        ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([], []),
        ([42], [42]),
        ([-3, 0, -1, 5, 2], [-3, -1, 0, 2, 5]),
    ]

    for nums, expected in test_cases:
        res = selection_sort(nums)
        print(f"Input:  {nums}")
        print(f"Sorted: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {nums}"

    print("\n[PASS] All Selection Sort tests passed successfully!")
