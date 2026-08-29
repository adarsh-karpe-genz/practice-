"""
Problem 07: Find Maximum and Minimum in a List
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, find both the largest (maximum) and smallest (minimum) elements.
Example: [3, 1, 9, 7, 5, 2] -> Max: 9, Min: 1

Concepts:
- Iterating through lists
- Tracking max / min variables
- Python built-in max() and min() functions
- Handling empty list edge cases
"""

from typing import List, Tuple


def find_max_min_manual(numbers: List[int]) -> Tuple[int, int]:
    """Method 1: Single-pass manual loop (O(N) time, O(1) space)"""
    if not numbers:
        raise ValueError("List cannot be empty.")

    current_max = numbers[0]
    current_min = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        if num < current_min:
            current_min = num

    return current_max, current_min


def find_max_min_builtin(numbers: List[int]) -> Tuple[int, int]:
    """Method 2: Using Python built-in functions"""
    if not numbers:
        raise ValueError("List cannot be empty.")
    return max(numbers), min(numbers)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 07: Find Max and Min Tests")
    print("=" * 50)

    test_lists = [
        ([3, 1, 9, 7, 5, 2], (9, 1)),
        ([42], (42, 42)),
        ([-5, -1, -10, -2], (-1, -10)),
        ([100, 200, 50, 300], (300, 50)),
    ]

    for nums, expected in test_lists:
        res1 = find_max_min_manual(nums)
        res2 = find_max_min_builtin(nums)
        print(f"List: {nums} -> (Max, Min): {res1} | Expected: {expected}")
        assert res1 == expected
        assert res2 == expected

    print("\n[PASS] All Max/Min tests passed successfully!")
