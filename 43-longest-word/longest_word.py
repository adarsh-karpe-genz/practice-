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

    print("\n[PASS] All Longest Word tests passed successfully!")
