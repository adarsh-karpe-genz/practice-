"""
Problem 23: Linear Search Algorithm
Difficulty: Beginner / Easy

Problem Statement:
Given a list of items and a `target` element, search for the target using
the Linear Search algorithm. Return the 0-based index of the first occurrence,
or -1 if the target is not present in the list.
Example: nums = [10, 50, 30, 70, 80, 20], target = 30 -> Returns 2

Concepts:
- Linear traversal O(N) time complexity
- Return index on match
- Find all indices variant
"""

from typing import List, Any


def linear_search(arr: List[Any], target: Any) -> int:
    """Finds index of first occurrence of target, or -1."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def linear_search_all_indices(arr: List[Any], target: Any) -> List[int]:
    """Returns all indices where target appears."""
    return [i for i, val in enumerate(arr) if val == target]


def linear_search_count_comparisons(arr: List[Any], target: Any) -> tuple[int, int]:
    """
    Performs linear search and returns (found_index, comparisons_count).
    If not found, returns (-1, len(arr)).
    """
    comparisons = 0
    for idx, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return (idx, comparisons)
    return (-1, comparisons)


if __name__ == "__main__":
    test_cases = [
        ([10, 50, 30, 70, 80, 20], 30, 2),
        ([10, 50, 30, 70, 80, 20], 99, -1),
        (["cat", "dog", "bird"], "dog", 1),
        (["cat", "dog", "bird"], "fish", -1),
        ([], 5, -1),
        ([7], 7, 0),
    ]

    for nums, tgt, expected in test_cases:
        res = linear_search(nums, tgt)
        assert res == expected, f"Failed for target {tgt}"
    assert linear_search_all_indices([10, 20, 30, 20, 40], 20) == [1, 3]

    # Test comparison count
    assert linear_search_count_comparisons([10, 20, 30, 40], 30) == (2, 3)
    assert linear_search_count_comparisons([10, 20, 30], 99) == (-1, 3)

    print("[PASS] Problem 23: Linear Search tests passed successfully!")
