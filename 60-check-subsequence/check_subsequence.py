"""
Problem 60: Check if String is a Subsequence
Difficulty: Beginner / Easy

Problem Statement:
Given two strings `s` and `t`, return True if `s` is a subsequence of `t`, or False otherwise.
A subsequence is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
Example: s = "abc", t = "ahbgdc" -> True
Example: s = "axc", t = "ahbgdc" -> False

Concepts:
- Two pointers technique O(len(t))
- Early exit when all characters in `s` are matched
"""

def is_subsequence(s: str, t: str) -> bool:
    """Check if s is a subsequence of t using two pointers."""
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 60: Check Subsequence Tests")
    print("=" * 50)

    test_cases = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "ahbgdc", True),
        ("b", "c", False),
        ("ace", "abcde", True),
    ]

    for s, t, expected in test_cases:
        res = is_subsequence(s, t)
        print(f"s='{s}', t='{t}' -> Is Subsequence? {res} | Expected: {expected}")
        assert res == expected, f"Failed for s='{s}', t='{t}'"

    print("\n[PASS] All Check Subsequence tests passed successfully!")
