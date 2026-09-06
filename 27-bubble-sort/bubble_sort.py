"""
Problem 27: Bubble Sort Implementation
Difficulty: Beginner / Easy

Problem Statement:
Implement the Bubble Sort algorithm to sort a list of numbers in ascending order.
Bubble Sort repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order.
Example: [64, 34, 25, 12, 22, 11, 90] -> [11, 12, 22, 25, 34, 64, 90]

Complexity:
- Time: O(N^2) worst/average, O(N) best (already sorted with optimized version)
- Space: O(1) in-place

Concepts:
- Nested loop pattern
- Adjacent element comparison and swap
- Early termination optimization with `swapped` flag
"""

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """Bubble Sort with early termination optimization (in-place)."""
    arr = nums[:]  # Work on a copy to preserve the original
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Already sorted — no swaps in this pass

    return arr


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 27: Bubble Sort Tests")
    print("=" * 50)

    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),   # Already sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),   # Reverse sorted
        ([], []),
        ([42], [42]),
        ([-3, 0, -1, 5, 2], [-3, -1, 0, 2, 5]),
    ]

    for nums, expected in test_cases:
        res = bubble_sort(nums)
        print(f"Input: {nums}")
        print(f"  -> Sorted: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {nums}"

    print("\n[PASS] All Bubble Sort tests passed successfully!")
