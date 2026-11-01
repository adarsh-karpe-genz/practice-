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


def is_anagram_prime_hash(s1: str, s2: str) -> bool:
    """Method 3: Prime number product hashing (order-independent multiplication)."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    c1 = [ch.lower() for ch in s1 if ch.isalnum()]
    c2 = [ch.lower() for ch in s2 if ch.isalnum()]
    if len(c1) != len(c2):
        return False
    h1 = 1
    h2 = 1
    for ch in c1:
        h1 *= primes[ord(ch) % 26]
    for ch in c2:
        h2 *= primes[ord(ch) % 26]
    return h1 == h2


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
        res3 = is_anagram_prime_hash(str1, str2)
        assert res3 == expected

    print("\n[PASS] All Valid Anagram tests passed successfully!")
