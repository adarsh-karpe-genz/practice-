"""
Problem 39: Insertion Sort Implementation
Difficulty: Beginner / Easy

Problem Statement:
Implement the Insertion Sort algorithm to sort a list in ascending order.
Insertion Sort builds the sorted list one element at a time by inserting
each new element into its correct position among the already-sorted elements.
Example: [5, 3, 1, 4, 2] -> [1, 2, 3, 4, 5]

Complexity: O(N^2) worst/average, O(N) best (already sorted), O(1) space

Concepts:
- Key element extraction and backward shifting
- Inner while loop for shifting larger elements right
- Excellent for small or nearly-sorted data
"""

from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    """Insertion Sort - O(N^2) worst, O(N) best, O(1) space (in-place on copy)."""
    arr = nums[:]
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 39: Insertion Sort Tests")
    print("=" * 50)

    test_cases = [
        ([5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
        ([12, 11, 13, 5, 6], [5, 6, 11, 12, 13]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([], []),
        ([99], [99]),
        ([-5, 2, -1, 0, 3], [-5, -1, 0, 2, 3]),
    ]

    for nums, expected in test_cases:
        res = insertion_sort(nums)
        print(f"Input:  {nums}")
        print(f"Sorted: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {nums}"

    print("\n[PASS] All Insertion Sort tests passed successfully!")
