"""
Problem 13: Remove Duplicates from a List (Preserving Order)
Difficulty: Beginner / Easy

Problem Statement:
Given a list of elements containing duplicate items, return a new list with
all duplicates removed while preserving the original order of first appearance.
Example: [1, 2, 2, 3, 4, 3, 5] -> [1, 2, 3, 4, 5]

Concepts:
- Set lookup for O(1) membership check
- Maintaining insertion order
- Using `dict.fromkeys()` (Python 3.7+ guarantee)
"""

from typing import List, Any


def remove_duplicates_seen_set(items: List[Any]) -> List[Any]:
    """Method 1: Using a set to track seen items in O(N) time"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def remove_duplicates_dict(items: List[Any]) -> List[Any]:
    """Method 2: Using dict.fromkeys() in Python 3.7+ (One-liner)"""
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 13: Remove Duplicates Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 2, 3, 4, 3, 5], [1, 2, 3, 4, 5]),
        (["apple", "banana", "apple", "orange", "banana"], ["apple", "banana", "orange"]),
        ([10, 10, 10], [10]),
        ([], []),
    ]

    for sample, expected in test_cases:
        r1 = remove_duplicates_seen_set(sample)
        r2 = remove_duplicates_dict(sample)
        print(f"Original: {sample}")
        print(f"  -> Result: {r1} | Expected: {expected}")
        assert r1 == expected
        assert r2 == expected

    print("\n[PASS] All Remove Duplicates tests passed successfully!")
