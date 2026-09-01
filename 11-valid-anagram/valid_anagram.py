"""
Problem 11: Valid Anagram Checker
Difficulty: Beginner / Easy

Problem Statement:
Given two strings `s1` and `s2`, determine if `s2` is an anagram of `s1`.
An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
Examples: "listen" & "silent" -> True, "rat" & "car" -> False

Concepts:
- Sorting approach (O(N log N))
- Hash map / Dictionary character count (O(N) time)
"""

from collections import Counter


def is_anagram_sorting(s1: str, s2: str) -> bool:
    """Method 1: Sorting strings (O(N log N))"""
    clean1 = "".join(ch.lower() for ch in s1 if ch.isalnum())
    clean2 = "".join(ch.lower() for ch in s2 if ch.isalnum())
    return sorted(clean1) == sorted(clean2)


def is_anagram_counting(s1: str, s2: str) -> bool:
    """Method 2: Hash Map frequency counting (O(N) time)"""
    clean1 = [ch.lower() for ch in s1 if ch.isalnum()]
    clean2 = [ch.lower() for ch in s2 if ch.isalnum()]
    return Counter(clean1) == Counter(clean2)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 11: Valid Anagram Tests")
    print("=" * 50)

    test_cases = [
        ("listen", "silent", True),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("Debit Card", "Bad Credit", True),
        ("hello", "world", False),
    ]

    for str1, str2, expected in test_cases:
        res1 = is_anagram_sorting(str1, str2)
        res2 = is_anagram_counting(str1, str2)
        print(f"'{str1}' & '{str2}' -> Anagram? {res1} | Expected: {expected}")
        assert res1 == expected
        assert res2 == expected

    print("\n[PASS] All Valid Anagram tests passed successfully!")
