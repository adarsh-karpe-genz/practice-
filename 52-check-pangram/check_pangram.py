"""
Problem 52: Check if String is a Pangram
Difficulty: Beginner / Easy

Problem Statement:
A pangram is a sentence containing every single letter of the English alphabet (a-z)
at least once. Case is ignored.
Example: "The quick brown fox jumps over the lazy dog" -> True
Example: "Hello World" -> False

Concepts:
- Set of unique alphabetic characters
- string.ascii_lowercase comparison
- .lower() and .isalpha() filtering
"""

import string


def is_pangram(sentence: str) -> bool:
    """Check if string contains every English letter from a to z."""
    alphabet_set = set(string.ascii_lowercase)
    clean_chars = {ch.lower() for ch in sentence if ch.isalpha()}
    return alphabet_set.issubset(clean_chars)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 52: Check Pangram Tests")
    print("=" * 50)

    test_cases = [
        ("The quick brown fox jumps over the lazy dog", True),
        ("Pack my box with five dozen liquor jugs", True),
        ("Hello World", False),
        ("", False),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxy", False),  # missing 'z'
    ]

    for s, expected in test_cases:
        res = is_pangram(s)
        print(f"Sentence: '{s[:30]}...' -> Pangram? {res} | Expected: {expected}")
        assert res == expected, f"Failed for '{s}'"

    print("\n[PASS] All Pangram tests passed successfully!")
