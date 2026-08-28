"""
Problem 04: Count Vowels and Consonants
Difficulty: Beginner / Easy

Problem Statement:
Given a string, count the total number of vowels (a, e, i, o, u) and consonants (letters that are not vowels).
Ignore numbers, spaces, and punctuation.

Concepts:
- Sets / Strings for O(1) membership testing (`char in vowels`)
- Character classification (`.isalpha()`, `.lower()`)
- Python Dictionaries for counts
"""

from typing import Dict


def count_vowels_and_consonants(text: str) -> Dict[str, int]:
    """Counts vowels and consonants in given string."""
    vowels = set("aeiou")
    counts = {"vowels": 0, "consonants": 0}

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                counts["vowels"] += 1
            else:
                counts["consonants"] += 1

    return counts


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 04: Count Vowels Tests")
    print("=" * 50)

    sample = "Hello World! 123"
    result = count_vowels_and_consonants(sample)
    print(f"Input: '{sample}'")
    print(f"Counts: {result}")

    # 'Hello World' -> vowels: e, o, o (3) | consonants: H, l, l, W, r, l, d (7)
    assert result["vowels"] == 3
    assert result["consonants"] == 7

    print("\n[PASS] All Count Vowels tests passed successfully!")
