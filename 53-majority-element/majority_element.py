"""
Problem 53: Find Majority Element (Boyer-Moore Voting Algorithm)
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers of size N, find the majority element that appears
more than N // 2 times. Assume a majority element always exists.
Example: [3, 2, 3] -> 3
Example: [2, 2, 1, 1, 1, 2, 2] -> 2

Concepts:
- Boyer-Moore Voting Algorithm: O(N) time, O(1) space
- Dictionary frequency counter: O(N) time, O(N) space
"""

from typing import List


def majority_element_boyer_moore(nums: List[int]) -> int:
    """Find majority element using Boyer-Moore Voting Algorithm (O(1) space)."""
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


def majority_element_dict(nums: List[int]) -> int:
    """Find majority element using dictionary counter."""
    counts = {}
    threshold = len(nums) // 2
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > threshold:
            return num
    return nums[0]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 53: Majority Element Tests")
    print("=" * 50)

    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([6, 6, 6, 7, 7], 6),
    ]

    for nums, expected in test_cases:
        r1 = majority_element_boyer_moore(nums)
        r2 = majority_element_dict(nums)
        print(f"Nums: {nums} -> Majority: {r1} | Expected: {expected}")
        assert r1 == expected
        assert r2 == expected

    print("\n[PASS] All Majority Element tests passed successfully!")
