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
    """Method 1: Manual dictionary accumulation with regex tokenization."""
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
    frequency: Dict[str, int] = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def top_k_words(text: str, k: int = 3) -> list[tuple[str, int]]:
    """Return the top-k most frequent words ordered by descending frequency."""
    freq = word_frequency_manual(text)
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k]


def filter_stopwords(text: str, stopwords: set[str] | None = None) -> Dict[str, int]:
    """
    Computes word frequency while ignoring common stopwords.
    """
    if stopwords is None:
        stopwords = {"is", "and", "to", "the", "a", "of", "in"}
    freq = word_frequency_manual(text)
    return {w: count for w, count in freq.items() if w not in stopwords}


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 12: Word Frequency Counter Tests")
    print("=" * 50)

    sample = "Python is great and Python is easy to learn."
    res = word_frequency_manual(sample)

    assert res["python"] == 2
    assert res["is"] == 2
    assert res["great"] == 1
    assert res["learn"] == 1
    top2 = top_k_words(sample, 2)
    assert top2 == [("python", 2), ("is", 2)]

    # Test stopwords filter
    filtered = filter_stopwords(sample)
    assert "is" not in filtered
    assert "and" not in filtered
    assert filtered["python"] == 2
    assert filtered["great"] == 1

    print("[PASS] All Word Frequency tests passed successfully!")
