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


def capitalize_title_style(sentence: str, minor_words: set[str] | None = None) -> str:
    """Capitalize words in sentence while keeping minor articles/prepositions lowercase."""
    if minor_words is None:
        minor_words = {"a", "an", "the", "in", "on", "of", "and", "is"}
    words = sentence.split()
    if not words:
        return ""
    result = [words[0].capitalize()]
    for w in words[1:]:
        low = w.lower()
        if low in minor_words:
            result.append(low)
        else:
            result.append(w.capitalize())
    return " ".join(result)


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
    assert capitalize_title_style("a quick brown fox in the hole") == "A Quick Brown Fox in the Hole"

    print("\n[PASS] All Capitalize Words tests passed successfully!")
