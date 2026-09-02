"""
Problem 16: Count Character Occurrences
Difficulty: Beginner / Easy

Problem Statement:
Given a string, count the frequency of each non-space character
(case-insensitive) and return a dictionary with the counts.
Example: "banana" -> {'b': 1, 'a': 3, 'n': 2}

Concepts:
- Character iteration and normalization (.lower())
- Dictionary accumulation with dict.get()
- collections.Counter
"""

from typing import Dict


def count_characters(text: str) -> Dict[str, int]:
    """Count non-space character occurrences in a string."""
    freq = {}
    for char in text.lower():
        if not char.isspace():
            freq[char] = freq.get(char, 0) + 1
    return freq


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 16: Character Count Tests")
    print("=" * 50)

    sample = "banana"
    res = count_characters(sample)
    print(f"Text: '{sample}' -> Counts: {res}")
    assert res == {"b": 1, "a": 3, "n": 2}

    sample2 = "Hello World"
    res2 = count_characters(sample2)
    print(f"Text: '{sample2}' -> Counts: {res2}")
    assert res2["l"] == 3
    assert res2["o"] == 2
    assert " " not in res2

    print("\n[PASS] All Character Count tests passed successfully!")
