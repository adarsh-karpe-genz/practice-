"""
Problem 22: Count Frequency of Elements in a List
Difficulty: Beginner / Easy

Problem Statement:
Given a list of items (integers or strings), return a dictionary containing
the frequency of each unique element.
Example: ["apple", "banana", "apple", "cherry", "banana", "apple"]
         -> {"apple": 3, "banana": 2, "cherry": 1}

Concepts:
- Dictionary accumulation using .get(key, default)
- collections.Counter
"""

from collections import Counter
from typing import List, Dict, Any


def count_frequency_manual(items: List[Any]) -> Dict[Any, int]:
    """Method 1: Manual dictionary loop (O(N) time, O(U) space)"""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def count_frequency_counter(items: List[Any]) -> Dict[Any, int]:
    """Method 2: Using collections.Counter"""
    return dict(Counter(items))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 22: List Frequency Tests")
    print("=" * 50)

    test_cases = [
        (["apple", "banana", "apple", "cherry", "banana", "apple"], {"apple": 3, "banana": 2, "cherry": 1}),
        ([1, 2, 2, 3, 3, 3, 4], {1: 1, 2: 2, 3: 3, 4: 1}),
        ([], {}),
        (["x"], {"x": 1}),
    ]

    for sample, expected in test_cases:
        res1 = count_frequency_manual(sample)
        res2 = count_frequency_counter(sample)
        print(f"Items: {sample}")
        print(f"  -> Frequency: {res1} | Expected: {expected}")
        assert res1 == expected
        assert res2 == expected

    print("\n[PASS] All List Frequency tests passed successfully!")
