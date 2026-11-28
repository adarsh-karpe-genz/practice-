"""
Problem 13: Remove Duplicates from a List (Preserving Order)
Difficulty: Beginner / Easy

Problem Statement:
Given a list of elements containing duplicate items, return a new list with
all duplicates removed while preserving the original order of first appearance.
Example: [1, 2, 2, 3, 4, 3, 5] -> [1, 2, 3, 4, 5]

Concepts:
- Seen set tracking for O(1) membership check
- Dictionary `fromkeys()` preserves insertion order (Python 3.7+)
- Generator yielding unique items lazily
"""

from typing import List, Any, Generator


def remove_duplicates_seen_set(lst: List[Any]) -> List[Any]:
    """Method 1: Using a Set to track seen elements."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def remove_duplicates_dict(lst: List[Any]) -> List[Any]:
    """Method 2: Using dict.fromkeys() (Preserves order in Python 3.7+)."""
    return list(dict.fromkeys(lst))


def remove_duplicates_generator(lst: List[Any]) -> Generator[Any, None, None]:
    """Method 3: Generator function yielding unique elements lazily."""
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            yield item


def find_duplicate_elements(lst: List[Any]) -> List[Any]:
    """
    Returns a list of all elements that appear more than once,
    preserving the order of their second appearance.
    """
    seen = set()
    duplicates = set()
    ordered_dups = []
    for item in lst:
        if item in seen:
            if item not in duplicates:
                duplicates.add(item)
                ordered_dups.append(item)
        else:
            seen.add(item)
    return ordered_dups


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 4, 3, 5], [1, 2, 3, 4, 5]),
        (["apple", "banana", "apple", "cherry", "banana"], ["apple", "banana", "cherry"]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([10, 10, 10], [10]),
        ([], []),
    ]

    for sample, expected in test_cases:
        r1 = remove_duplicates_seen_set(sample)
        r2 = remove_duplicates_dict(sample)
        assert r1 == expected
        assert r2 == expected
        r3 = list(remove_duplicates_generator(sample))
        assert r3 == expected

    # Test duplicate elements finder
    assert find_duplicate_elements([1, 2, 2, 3, 4, 3, 5]) == [2, 3]
    assert find_duplicate_elements([1, 2, 3]) == []
    assert find_duplicate_elements(["a", "b", "a", "a"]) == ["a"]

    print("[PASS] Problem 13: Remove Duplicates tests passed successfully!")
