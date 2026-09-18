"""
Problem 61: Count Inversions in an Array
Difficulty: Beginner / Easy

Problem Statement:
An inversion in an array A occurs when i < j and A[i] > A[j].
Given a list of integers, count the total number of inversions.
Example: [2, 4, 1, 3, 5] -> Inversions: (2, 1), (4, 1), (4, 3) -> Total 3

Concepts:
- Nested loop comparison (brute force beginner approach O(N^2))
- Measuring how close an array is to being sorted
"""

from typing import List


def count_inversions_simple(nums: List[int]) -> int:
    """Count inversions using standard nested loops O(N^2)."""
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                count += 1
    return count


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 61: Count Inversions Tests")
    print("=" * 50)

    test_cases = [
        ([2, 4, 1, 3, 5], 3),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 10),
        ([1], 0),
        ([], 0),
    ]

    for nums, expected in test_cases:
        res = count_inversions_simple(nums)
        print(f"Nums: {nums} -> Inversions: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {nums}"

    print("\n[PASS] All Count Inversions tests passed successfully!")
