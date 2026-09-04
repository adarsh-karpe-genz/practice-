"""
Problem 23: Linear Search Algorithm
Difficulty: Beginner / Easy

Problem Statement:
Given a list of items and a `target` element, search for the target using
the Linear Search algorithm. Return the 0-based index of the first occurrence,
or -1 if the target is not present in the list.
Example: nums = [10, 50, 30, 70, 80, 20], target = 30 -> Returns 2

Concepts:
- Sequential iteration with enumerate()
- Early exit upon match (O(1) best, O(N) worst)
- Handling element not found (-1 return)
"""

from typing import List, Any


def linear_search(items: List[Any], target: Any) -> int:
    """Perform linear search for target in items list."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 23: Linear Search Tests")
    print("=" * 50)

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
        print(f"List: {nums}, Target: {tgt} -> Found Index: {res:<2} | Expected: {expected:<2}")
        assert res == expected, f"Failed for target {tgt}"

    print("\n[PASS] All Linear Search tests passed successfully!")
