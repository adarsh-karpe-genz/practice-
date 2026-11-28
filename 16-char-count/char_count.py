"""
Problem 16: Count Character Occurrences
Difficulty: Beginner / Easy

Problem Statement:
Given a string, count the frequency of each non-space character
(case-insensitive) and return a dictionary with the counts.
Example: "banana" -> {'b': 1, 'a': 3, 'n': 2}

Concepts:
- Character iteration and normalization (`.lower()`)
- Dictionary counting with `.get()` or `Counter`
- Entropy and frequency distribution calculations
"""

from typing import Dict
from collections import Counter


def count_characters(text: str) -> Dict[str, int]:
    """Counts frequencies of non-whitespace characters."""
    counts: Dict[str, int] = {}
    for char in text.lower():
        if not char.isspace():
            counts[char] = counts.get(char, 0) + 1
    return counts


def unique_character_ratio(text: str) -> float:
    """Computes ratio of distinct characters to total non-space length."""
    counts = count_characters(text)
    total_chars = sum(counts.values())
    if total_chars == 0:
        return 0.0
    return round(len(counts) / total_chars, 4)


def most_frequent_char(text: str) -> tuple[str, int] | None:
    """
    Returns the character with the highest occurrence frequency.
    Returns None if text contains no non-space characters.
    """
    counts = count_characters(text)
    if not counts:
        return None
    best_char = max(counts, key=lambda k: counts[k])
    return (best_char, counts[best_char])


if __name__ == "__main__":
    sample = "banana"
    res = count_characters(sample)
    assert res == {"b": 1, "a": 3, "n": 2}

    sample2 = "Hello World"
    res2 = count_characters(sample2)
    assert res2["l"] == 3
    assert res2["o"] == 2
    assert " " not in res2
    assert unique_character_ratio("banana") == round(3 / 6, 4)

    # Test most frequent char
    assert most_frequent_char("banana") == ("a", 3)
    assert most_frequent_char("Hello World") == ("l", 3)
    assert most_frequent_char("   ") is None

    print("[PASS] Problem 16: Character Count tests passed successfully!")
