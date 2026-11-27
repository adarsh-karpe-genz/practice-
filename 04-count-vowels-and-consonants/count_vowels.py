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
    """Counts total vowels and consonants in text."""
    vowels = set("aeiou")
    v_count = 0
    c_count = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    return {"vowels": v_count, "consonants": c_count}


def count_vowel_frequencies(text: str) -> Dict[str, int]:
    """Returns frequency distribution for each vowel a, e, i, o, u."""
    vowels = "aeiou"
    counts = {v: 0 for v in vowels}
    for ch in text.lower():
        if ch in counts:
            counts[ch] += 1
    return counts


def vowel_to_consonant_ratio(text: str) -> float | None:
    """
    Calculates the ratio of vowels to consonants.
    Returns None if consonants count is zero.
    """
    counts = count_vowels_and_consonants(text)
    if counts["consonants"] == 0:
        return None
    return counts["vowels"] / counts["consonants"]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 04: Count Vowels Tests")
    print("=" * 50)

    sample = "Hello World! 123"
    result = count_vowels_and_consonants(sample)

    assert result["vowels"] == 3
    assert result["consonants"] == 7
    v_freq = count_vowel_frequencies(sample)
    assert sum(v_freq.values()) == result["vowels"]

    # Test ratio
    ratio = vowel_to_consonant_ratio(sample)
    assert ratio is not None and abs(ratio - 3 / 7) < 1e-6
    assert vowel_to_consonant_ratio("aeiou") is None

    print("[PASS] All Count Vowels tests passed successfully!")
