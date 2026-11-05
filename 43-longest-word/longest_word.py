"""
Problem 43: Find the Longest Word in a Sentence
Difficulty: Beginner / Easy

Problem Statement:
Given a sentence as a string, find and return the longest word in it.
If multiple words tie for the longest length, return the first one.
Ignore punctuation attached to words.
Example: "The quick brown fox jumped over the lazy dog" -> "jumped"

Concepts:
- String cleaning / splitting with str.split()
- Built-in max() with key=len
- Iterative comparison pattern
"""

import string


def find_longest_word(sentence: str) -> str:
    """Find the longest word in a sentence, ignoring punctuation."""
    if not sentence.strip():
        return ""

    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    clean_sentence = sentence.translate(translator)

    words = clean_sentence.split()
    if not words:
        return ""

    return max(words, key=len)


import re

def find_all_longest_words(sentence: str) -> list[str]:
    """Return all words tied for maximum length after removing punctuation."""
    words = re.findall(r'[a-zA-Z0-9]+', sentence)
    if not words:
        return []
    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 43: Longest Word Tests")
    print("=" * 50)

    test_cases = [
        ("The quick brown fox jumped over the lazy dog", "jumped"),
        ("Python programming is fantastic", "programming"),
        ("Hello, world!", "Hello"),
        ("A BB CCC DDDD", "DDDD"),
        ("", ""),
        ("one", "one"),
    ]

    for s, expected in test_cases:
        res = find_longest_word(s)
        print(f"Input: '{s}' -> Longest: '{res}' | Expected: '{expected}'")
        assert res == expected, f"Failed for '{s}'"
    assert find_all_longest_words("The quick brown fox jumps") == ["quick", "brown", "jumps"]

    print("\n[PASS] All Longest Word tests passed successfully!")
