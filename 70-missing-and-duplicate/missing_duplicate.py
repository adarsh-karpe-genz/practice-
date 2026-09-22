"""
Problem 70: Find Missing and Duplicate Number (Set Mismatch)
Difficulty: Beginner / Easy

Problem Statement:
Given an array containing N numbers from 1 to N, one number was accidentally
duplicated and one number went missing. Find and return both as (duplicate, missing).
Example: [1, 2, 2, 4] -> Duplicate is 2, Missing is 3 -> (2, 3)

Concepts:
- Frequency counting using collections.Counter or hash set
- Sum formula comparisons: expected sum vs actual sum
- Range 1 to N iteration
"""

from collections import Counter
from typing import List, Tuple


def find_error_nums(nums: List[int]) -> Tuple[int, int]:
    """Find the duplicated and missing numbers from 1 to N."""
    n = len(nums)
    counts = Counter(nums)
    duplicate = -1
    missing = -1

    for i in range(1, n + 1):
        c = counts.get(i, 0)
        if c == 2:
            duplicate = i
        elif c == 0:
            missing = i

    return duplicate, missing


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 70: Missing and Duplicate Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 2, 4], (2, 3)),
        ([1, 1], (1, 2)),
        ([2, 2], (2, 1)),
        ([3, 2, 3, 4, 5], (3, 1)),
    ]

    for nums, expected in test_cases:
        res = find_error_nums(nums)
        print(f"Nums: {nums} -> (Duplicate, Missing): {res} | Expected: {expected}")
        assert res == expected, f"Failed for {nums}"

    print("\n[PASS] All Missing and Duplicate tests passed successfully!")
