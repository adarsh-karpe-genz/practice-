"""
Problem 66: Count Words in a String
Difficulty: Beginner / Easy

Problem Statement:
Given a string, count the total number of words in it.
Words are separated by one or more whitespace characters.
Leading and trailing spaces should be ignored.
Example: "   Hello   world!  Welcome to Python. " -> 5

Concepts:
- str.split() handling of variable-length whitespaces
- Edge case handling (empty strings, all whitespace)
"""

def count_words(text: str) -> int:
    """Return the count of words in the given text."""
    if not text:
        return 0
    words = text.split()
    return len(words)


import re

def word_statistics(text: str) -> dict[str, float | int]:
    """Calculate total words, unique words, and average word length."""
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return {"total": 0, "unique": 0, "avg_len": 0.0}
    return {
        "total": len(words),
        "unique": len(set(words)),
        "avg_len": round(sum(len(w) for w in words) / len(words), 2)
    }


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 66: Count Words Tests")
    print("=" * 50)

    test_cases = [
        ("   Hello   world!  Welcome to Python. ", 5),
        ("SingleWord", 1),
        ("", 0),
        ("    ", 0),
        ("Python is fun and easy to learn!", 7),
    ]

    for s, expected in test_cases:
        res = count_words(s)
        print(f"String: '{s.strip()[:25]}' -> Word Count: {res} | Expected: {expected}")
        assert res == expected, f"Failed for '{s}'"
    stats = word_statistics("Python is fun and Python is easy")
    assert stats["total"] == 7 and stats["unique"] == 5

    print("\n[PASS] All Count Words tests passed successfully!")
