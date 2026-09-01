"""
Problem 12: Word Frequency Counter
Difficulty: Beginner / Easy

Problem Statement:
Given a string sentence/text, count the occurrences of each word (case-insensitive)
and return the result as a dictionary mapping words to their frequencies.

Concepts:
- String splitting (`.split()`) & cleaning
- Dictionary frequency accumulation
- Python `dict.get(key, default)` method
"""

import re
from typing import Dict


def word_frequency_manual(text: str) -> Dict[str, int]:
    """Method 1: Manual dictionary loop with string cleaning"""
    words = re.findall(r"\b\w+\b", text.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 12: Word Frequency Counter Tests")
    print("=" * 50)

    sample = "Python is great and Python is easy to learn."
    res = word_frequency_manual(sample)
    print(f"Input: '{sample}'")
    print("Frequencies:", res)

    assert res["python"] == 2
    assert res["is"] == 2
    assert res["great"] == 1
    assert res["learn"] == 1

    print("\n[PASS] All Word Frequency tests passed successfully!")
