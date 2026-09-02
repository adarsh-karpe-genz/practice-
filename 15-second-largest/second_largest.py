"""
Problem 15: Find Second Largest Number in a List
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, return the second largest distinct number.
If no second largest number exists (e.g., list length < 2 or all items equal), return None.
Example: [10, 20, 4, 45, 99, 99] -> 45

Concepts:
- Single-pass tracking of first and second maximum (O(N) time, O(1) space)
- Set deduplication and sorting approach
"""

from typing import List, Optional


def find_second_largest_single_pass(numbers: List[int]) -> Optional[int]:
    """Method 1: Single-pass tracking (O(N) time, O(1) space)"""
    if len(numbers) < 2:
        return None

    first = second = float("-inf")

    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return int(second) if second != float("-inf") else None


def find_second_largest_set(numbers: List[int]) -> Optional[int]:
    """Method 2: Using set and sorting (Pythonic & simple)"""
    unique_nums = sorted(set(numbers))
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 15: Second Largest Tests")
    print("=" * 50)

    test_cases = [
        ([10, 20, 4, 45, 99, 99], 45),
        ([5, 5, 5, 5], None),
        ([12, 35, 1, 10, 34, 1], 34),
        ([100], None),
        ([-10, -5, -2, -20], -5),
    ]

    for nums, expected in test_cases:
        res1 = find_second_largest_single_pass(nums)
        res2 = find_second_largest_set(nums)
        print(f"List: {nums} -> Second Largest: {res1} | Expected: {expected}")
        assert res1 == expected, f"Single-pass failed for {nums}"
        assert res2 == expected, f"Set method failed for {nums}"

    print("\n[PASS] All Second Largest tests passed successfully!")
