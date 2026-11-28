"""
Problem 22: Count Frequency of Elements in a List
Difficulty: Beginner / Easy

Problem Statement:
Given a list of items, count the occurrences of each unique element
and return the result as a dictionary mapping elements to their frequencies.
Example: [1, 2, 2, 3, 3, 3] -> {1: 1, 2: 2, 3: 3}

Concepts:
- Manual dictionary tracking with `.get(key, 0) + 1`
- `collections.Counter`
- Mode analysis
"""

from typing import List, Dict, Any
from collections import Counter


def count_frequency_manual(items: List[Any]) -> Dict[Any, int]:
    """Counts element frequency using manual dictionary accumulation."""
    freq: Dict[Any, int] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def count_frequency_counter(items: List[Any]) -> Dict[Any, int]:
    """Counts element frequency using Counter."""
    return dict(Counter(items))


def find_mode(items: List[Any]) -> List[Any]:
    """Finds all modes (most frequently occurring elements)."""
    if not items:
        return []
    freq = count_frequency_manual(items)
    max_count = max(freq.values())
    return [elem for elem, count in freq.items() if count == max_count]


def filter_by_min_frequency(items: List[Any], min_freq: int) -> List[Any]:
    """
    Returns unique elements that appear at least min_freq times.
    """
    freq = count_frequency_manual(items)
    return [k for k, count in freq.items() if count >= min_freq]


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 3, 3, 4], {1: 1, 2: 2, 3: 3, 4: 1}),
        ([], {}),
        (["x"], {"x": 1}),
    ]

    for sample, expected in test_cases:
        res1 = count_frequency_manual(sample)
        res2 = count_frequency_counter(sample)
        assert res1 == expected
        assert res2 == expected
    assert find_mode([1, 2, 2, 3, 3]) == [2, 3]

    # Test min frequency filter
    assert filter_by_min_frequency([1, 2, 2, 3, 3, 3, 4], 2) == [2, 3]
    assert filter_by_min_frequency([1, 2, 3], 2) == []

    print("[PASS] Problem 22: List Frequency tests passed successfully!")
