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
    """Method 1: Single pass linear scan O(N) comparisons"""
    if not numbers:
        raise ValueError("List cannot be empty.")
    max_val = numbers[0]
    min_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return (max_val, min_val)


def find_max_min_builtin(numbers: List[int]) -> Tuple[int, int]:
    """Method 2: Using built-in max() and min()"""
    if not numbers:
        raise ValueError("List cannot be empty.")
    return (max(numbers), min(numbers))


def find_min_max_divide_and_conquer(numbers: List[int]) -> Tuple[int, int]:
    """Method 3: Tournament divide and conquer algorithm"""
    if not numbers:
        raise ValueError("List cannot be empty.")

    def _helper(low: int, high: int) -> Tuple[int, int]:
        if low == high:
            return (numbers[low], numbers[low])
        if high == low + 1:
            if numbers[low] > numbers[high]:
                return (numbers[low], numbers[high])
            return (numbers[high], numbers[low])
        mid = (low + high) // 2
        max1, min1 = _helper(low, mid)
        max2, min2 = _helper(mid + 1, high)
        return (max(max1, max2), min(min1, min2))

    return _helper(0, len(numbers) - 1)


def min_max_range_spread(numbers: List[int]) -> int:
    """Calculates spread / range: max(numbers) - min(numbers)."""
    mx, mn = find_max_min_manual(numbers)
    return mx - mn


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
        assert res1 == expected
        assert res2 == expected
        res3 = find_min_max_divide_and_conquer(nums)
        assert res3 == expected

    # Test spread range
    assert min_max_range_spread([3, 1, 9, 7, 5, 2]) == 8
    assert min_max_range_spread([42]) == 0

    print("[PASS] All Max/Min tests passed successfully!")
