"""
Problem 14: Capitalize Words (Title Case)
Difficulty: Beginner / Easy

Problem Statement:
Given a string of words separated by spaces, capitalize the first letter
of each word while keeping all other letters in lowercase.
Example: "hello python world" -> "Hello Python World"

Concepts:
- String methods (`.title()`, `.capitalize()`)
- List comprehension and `' '.join()`
"""

def capitalize_words_manual(text: str) -> str:
    """Method 1: Manual split and capitalize (Beginner standard)"""
    words = text.split()
    return " ".join(word.capitalize() for word in words)


def capitalize_words_builtin(text: str) -> str:
    """Method 2: Built-in title method"""
    return text.title()


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 14: Capitalize Words Tests")
    print("=" * 50)

    test_cases = [
        ("hello world", "Hello World"),
        ("python PROGRAMMING is fun", "Python Programming Is Fun"),
        ("a quick brown fox", "A Quick Brown Fox"),
        ("single", "Single"),
    ]

    for sample, expected in test_cases:
        res1 = capitalize_words_manual(sample)
        print(f"Input: '{sample}' -> Result: '{res1}'")
        assert res1 == expected, f"Failed for '{sample}'"

    print("\n[PASS] All Capitalize Words tests passed successfully!")
