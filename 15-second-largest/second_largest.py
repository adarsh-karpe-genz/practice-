"""
Problem 15: Find Second Largest Number in a List
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, return the second largest distinct number.
If no second largest number exists (e.g., list length < 2 or all items equal), return None.
Example: [10, 20, 4, 45, 99, 99] -> 45

Concepts:
- Single-pass linear scan with two tracking pointers O(N)
- Set deduplication and sorting O(N log N)
- Min-heap / heapq for top-K largest numbers
"""

from typing import List, Optional
import heapq


def find_second_largest_single_pass(numbers: List[int]) -> Optional[int]:
    """Single pass tracking largest and second largest."""
    if len(numbers) < 2:
        return None
    largest = float("-inf")
    second_largest = float("-inf")
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return int(second_largest) if second_largest != float("-inf") else None


def find_second_largest_set(numbers: List[int]) -> Optional[int]:
    """Set deduplication method."""
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]


def find_second_largest_heap(numbers: List[int]) -> Optional[int]:
    """Heap-based top-2 unique elements search."""
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    top2 = heapq.nlargest(2, unique)
    return top2[1]


def find_kth_largest(numbers: List[int], k: int) -> Optional[int]:
    """
    Finds the k-th distinct largest number using a heap.
    Returns None if fewer than k distinct numbers exist.
    """
    unique = list(set(numbers))
    if len(unique) < k or k <= 0:
        return None
    return heapq.nlargest(k, unique)[-1]


if __name__ == "__main__":
    test_cases = [
        ([10, 20, 4, 45, 99, 99], 45),
        ([5, 5, 5, 5], None),
        ([3], None),
        ([], None),
        ([12, 35, 1, 10, 34, 1], 34),
        ([100], None),
        ([-10, -5, -2, -20], -5),
    ]

    for nums, expected in test_cases:
        res1 = find_second_largest_single_pass(nums)
        res2 = find_second_largest_set(nums)
        assert res1 == expected, f"Single-pass failed for {nums}"
        assert res2 == expected, f"Set method failed for {nums}"
        res3 = find_second_largest_heap(nums)
        assert res3 == expected, f"Heap method failed for {nums}"

    # Test kth largest
    assert find_kth_largest([10, 20, 4, 45, 99, 99], 3) == 20
    assert find_kth_largest([10, 20], 3) is None
    assert find_kth_largest([5, 5, 5], 1) == 5

    print("[PASS] Problem 15: Second Largest tests passed successfully!")
