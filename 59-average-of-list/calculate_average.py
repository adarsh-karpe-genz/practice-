"""
Problem 59: Calculate Average of Numbers
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, calculate and return their arithmetic mean (average).
Raise ValueError if the list is empty.
Example: [10, 20, 30, 40, 50] -> 30.0

Concepts:
- sum() / len() pattern
- Floating point division
- Empty list edge case handling
"""

from typing import List


def calculate_average(nums: List[int | float]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not nums:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum(nums) / len(nums)


def calculate_median(numbers: list[int | float]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        return 0.0
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    return float(s[mid]) if n % 2 != 0 else (s[mid - 1] + s[mid]) / 2.0


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 59: Average of List Tests")
    print("=" * 50)

    test_cases = [
        ([10, 20, 30, 40, 50], 30.0),
        ([1, 2, 3, 4], 2.5),
        ([5], 5.0),
        ([0, 0, 0], 0.0),
        ([-10, 10], 0.0),
    ]

    for nums, expected in test_cases:
        res = calculate_average(nums)
        print(f"Nums: {nums} -> Average: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {nums}"
    assert calculate_median([1, 3, 2]) == 2.0
    assert calculate_median([1, 2, 3, 4]) == 2.5

    print("\n[PASS] All Average of List tests passed successfully!")
