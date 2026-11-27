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
    """Method 1: Sorting approach"""
    cleaned1 = [ch.lower() for ch in s1 if ch.isalnum()]
    cleaned2 = [ch.lower() for ch in s2 if ch.isalnum()]
    return sorted(cleaned1) == sorted(cleaned2)


def is_anagram_counting(s1: str, s2: str) -> bool:
    """Method 2: Character frequency count using Counter"""
    cleaned1 = [ch.lower() for ch in s1 if ch.isalnum()]
    cleaned2 = [ch.lower() for ch in s2 if ch.isalnum()]
    return Counter(cleaned1) == Counter(cleaned2)


def is_anagram_prime_hash(s1: str, s2: str) -> bool:
    """Method 3: Prime product hash verification"""
    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
    ]
    def hash_str(s: str) -> int:
        prod = 1
        for ch in s.lower():
            if 'a' <= ch <= 'z':
                prod *= primes[ord(ch) - ord('a')]
        return prod
    return hash_str(s1) == hash_str(s2)


def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Groups a list of words into lists of anagrams.
    O(N * K log K) time complexity where K is maximum word length.
    """
    groups: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


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
        assert is_anagram_sorting(str1, str2) == expected
        assert is_anagram_counting(str1, str2) == expected
        assert is_anagram_prime_hash(str1, str2) == expected

    # Test group anagrams
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(words)
    # Check that eat, tea, ate are grouped together
    for g in grouped:
        if "eat" in g:
            assert set(g) == {"eat", "tea", "ate"}

    print("[PASS] All Valid Anagram tests passed successfully!")
