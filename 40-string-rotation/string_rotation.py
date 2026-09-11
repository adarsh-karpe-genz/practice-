"""
Problem 40: Check if Two Strings are Rotations of Each Other
Difficulty: Beginner / Easy

Problem Statement:
Given two strings s1 and s2, determine if s2 is a rotation of s1.
A rotation means you can shift some characters from the front of s1
and append them to the back, to get s2.
Examples:
  s1 = "abcde",  s2 = "cdeab"  -> True   (rotate 2 left)
  s1 = "hello",  s2 = "llohe"  -> True   (rotate 3 left)
  s1 = "hello",  s2 = "world"  -> False

Key Insight: s2 is a rotation of s1 if and only if s2 is a substring of s1+s1.

Concepts:
- String concatenation trick: s1 + s1
- Substring check with `in` operator
- Length check as a prerequisite
"""

def is_rotation(s1: str, s2: str) -> bool:
    """Check if s2 is a rotation of s1 using the concatenation trick."""
    if len(s1) != len(s2):
        return False
    if s1 == s2 == "":
        return True
    return s2 in (s1 + s1)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 40: String Rotation Tests")
    print("=" * 50)

    test_cases = [
        ("abcde", "cdeab", True),
        ("hello", "llohe", True),
        ("hello", "world", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("abc", "bca", True),
        ("abcd", "abdc", False),
    ]

    for s1, s2, expected in test_cases:
        res = is_rotation(s1, s2)
        print(f"s1='{s1}', s2='{s2}' -> Rotation? {res} | Expected: {expected}")
        assert res == expected, f"Failed for s1='{s1}', s2='{s2}'"

    print("\n[PASS] All String Rotation tests passed successfully!")
