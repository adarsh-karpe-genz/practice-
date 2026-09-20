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

    print("\n[PASS] All Count Words tests passed successfully!")
