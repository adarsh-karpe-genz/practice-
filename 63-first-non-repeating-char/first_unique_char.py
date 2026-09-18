"""
Problem 63: Find First Non-Repeating Character
Difficulty: Beginner / Easy

Problem Statement:
Given a string, find and return the first non-repeating character.
If every character repeats or the string is empty, return None.
Example: "swiss" -> 'w'
Example: "aabbcc" -> None

Concepts:
- Frequency map with dict or collections.Counter
- Two-pass traversal: first to count, second to find first with count 1
- Linear time complexity O(N)
"""

from collections import Counter
from typing import Optional


def first_non_repeating_char(s: str) -> Optional[str]:
    """Find the first character that appears exactly once."""
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 63: First Non-Repeating Char Tests")
    print("=" * 50)

    test_cases = [
        ("swiss", "w"),
        ("aabbcc", None),
        ("leetcode", "l"),
        ("loveleetcode", "v"),
        ("", None),
        ("z", "z"),
    ]

    for s, expected in test_cases:
        res = first_non_repeating_char(s)
        print(f"String: '{s}' -> First Unique: '{res}' | Expected: '{expected}'")
        assert res == expected, f"Failed for '{s}'"

    print("\n[PASS] All First Non-Repeating Char tests passed successfully!")
