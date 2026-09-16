"""
Problem 55: Cumulative Sum (Prefix Sum / Running Total)
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, return a new list where each element at index i
is the sum of all elements from index 0 to i (running sum / prefix sum).
Example: [1, 2, 3, 4] -> [1, 3, 6, 10]
Example: [1, 1, 1, 1, 1] -> [1, 2, 3, 4, 5]

Concepts:
- Accumulator variable pattern
- itertools.accumulate standard library comparison
- Prefix sum array applications in algorithms
"""

import itertools
from typing import List


def cumulative_sum_loop(nums: List[int | float]) -> List[int | float]:
    """Method 1: Iterative accumulator loop (O(N) time, O(N) space)."""
    running_total = 0
    result = []
    for num in nums:
        running_total += num
        result.append(running_total)
    return result


def cumulative_sum_itertools(nums: List[int | float]) -> List[int | float]:
    """Method 2: Using itertools.accumulate."""
    return list(itertools.accumulate(nums))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 55: Cumulative Sum Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ([], []),
        ([5], [5]),
        ([-1, -2, -3], [-1, -3, -6]),
    ]

    for nums, expected in test_cases:
        r1 = cumulative_sum_loop(nums)
        r2 = cumulative_sum_itertools(nums)
        print(f"Input: {nums} -> Cumulative: {r1} | Expected: {expected}")
        assert r1 == expected
        assert r2 == expected

    print("\n[PASS] All Cumulative Sum tests passed successfully!")
