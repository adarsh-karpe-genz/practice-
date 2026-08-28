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
    """Method 2: Two Pointers (Interview standard)"""
    cleaned = "".join(ch.lower() for ch in str(text) if ch.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


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
        print(f"Testing '{sample}' -> Result: {res1} | Expected: {expected}")
        assert res1 == expected
        assert res2 == expected

    print("\n[PASS] All Palindrome tests passed successfully!")
