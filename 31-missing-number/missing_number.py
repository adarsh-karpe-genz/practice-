"""
Problem 31: Find the Missing Number in an Array
Difficulty: Beginner / Easy

Problem Statement:
Given an array containing N distinct numbers taken from 0 to N (so one
number is missing), find and return the missing number.
Example: [3, 0, 1] -> Missing is 2  (N=3, range 0..3)

Concepts:
- Gauss formula: sum of 0..N = N*(N+1)//2
- XOR trick (O(N) time, O(1) space, no overflow)
- set difference approach
"""

from typing import List


def missing_number_gauss(nums: List[int]) -> int:
    """Method 1: Gauss sum formula (O(N) time, O(1) space)"""
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)


def missing_number_xor(nums: List[int]) -> int:
    """Method 2: XOR trick — x ^ x == 0, so cancel out pairs"""
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result


def missing_in_arithmetic_progression(arr: list[int]) -> int | None:
    """Find the single missing number in an AP series with constant difference d."""
    n = len(arr)
    if n < 2:
        return None
    d = (arr[-1] - arr[0]) // n
    for i in range(n - 1):
        if arr[i + 1] - arr[i] != d:
            return arr[i] + d
    return None


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 31: Missing Number Tests")
    print("=" * 50)

    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
    ]

    for nums, expected in test_cases:
        r1 = missing_number_gauss(nums)
        r2 = missing_number_xor(nums)
        print(f"Array: {nums} -> Missing: {r1} | Expected: {expected}")
        assert r1 == expected, f"Gauss failed for {nums}"
        assert r2 == expected, f"XOR failed for {nums}"
    assert missing_in_arithmetic_progression([2, 4, 8, 10]) == 6
    assert missing_in_arithmetic_progression([1, 4, 7, 13]) == 10

    print("\n[PASS] All Missing Number tests passed successfully!")
