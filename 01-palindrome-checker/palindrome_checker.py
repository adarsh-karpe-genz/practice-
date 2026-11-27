"""
Problem 01: Palindrome Checker
Difficulty: Beginner / Easy

What is a Palindrome?
A palindrome is a word, phrase, or number that reads the same backward as forward.
Examples: 'radar', 'madam', 'racecar', '121'

Concepts:
- String slicing [::-1]
- Two Pointers
- String methods (.lower(), .isalnum())
"""

def is_palindrome_simple(text: str) -> bool:
    """Method 1: String Slicing (Pythonic & Beginner-friendly)"""
    cleaned = "".join(ch.lower() for ch in str(text) if ch.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointer(text: str) -> bool:
    """Method 2: Two-Pointer Approach (In-place & Space Optimized O(1))"""
    s = str(text).lower()
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_recursive(text: str) -> bool:
    """Method 3: Recursive Approach (Divide and Conquer)"""
    cleaned = "".join(ch.lower() for ch in str(text) if ch.isalnum())

    def _helper(s: str) -> bool:
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return _helper(s[1:-1])

    return _helper(cleaned)


def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring using center expansion.
    Runs in O(N^2) time and O(1) auxiliary space.
    """
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        p1 = expand_around_center(i, i)
        # Even length palindrome
        p2 = expand_around_center(i, i + 1)
        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2
    return longest


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 01: Palindrome Checker Tests")
    print("=" * 50)

    test_cases = [
        ("radar", True),
        ("hello", False),
        ("A man, a plan, a canal: Panama", True),
        ("12321", True),
        ("12345", False),
    ]

    for sample, expected in test_cases:
        res1 = is_palindrome_simple(sample)
        res2 = is_palindrome_two_pointer(sample)
        assert res1 == expected
        assert res2 == expected
        res3 = is_palindrome_recursive(sample)
        assert res3 == expected

    # Test longest palindromic substring
    assert longest_palindromic_substring("babad") in ("bab", "aba")
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("racecar") == "racecar"

    print("[PASS] All Palindrome tests passed successfully!")
