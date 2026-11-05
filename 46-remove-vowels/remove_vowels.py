"""
Problem 46: Remove Vowels from a String
Difficulty: Beginner / Easy

Problem Statement:
Given a string, return a new string with all vowels (a, e, i, o, u, both lowercase
and uppercase) removed.
Example: "Hello World" -> "Hll Wrld"

Concepts:
- Membership checking using sets for O(1) lookup
- List comprehension and str.join()
- String filtering
"""

def remove_vowels(text: str) -> str:
    """Remove all vowels from a string."""
    vowels = set("aeiouAEIOU")
    return "".join(ch for ch in text if ch not in vowels)


import re

def remove_vowels_regex(s: str) -> str:
    """Remove vowels from string using regular expressions."""
    return re.sub(r'[aeiouAEIOU]', '', s)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 46: Remove Vowels Tests")
    print("=" * 50)

    test_cases = [
        ("Hello World", "Hll Wrld"),
        ("Python Programming", "Pythn Prgrmmng"),
        ("AEIOUaeiou", ""),
        ("xyz", "xyz"),
        ("", ""),
        ("Artificial Intelligence", "rtfcl ntllgnc"),
    ]

    for s, expected in test_cases:
        res = remove_vowels(s)
        print(f"Input: '{s}' -> Result: '{res}' | Expected: '{expected}'")
        assert res == expected, f"Failed for '{s}'"
        assert remove_vowels_regex(s) == expected

    print("\n[PASS] All Remove Vowels tests passed successfully!")
