"""
Problem 14: Capitalize Words (Title Case)
Difficulty: Beginner / Easy

Problem Statement:
Given a string of words separated by spaces, capitalize the first letter
of each word while keeping all other letters in lowercase.
Example: "hello python world" -> "Hello Python World"

Concepts:
- String methods (`.capitalize()`, `.title()`, `.split()`, `.join()`)
- Preserving formatting and special minor-word capitalization rules
"""

def capitalize_words_manual(text: str) -> str:
    """Capitalizes the first character of each word."""
    words = text.split(" ")
    capitalized = [word.capitalize() for word in words]
    return " ".join(capitalized)


def capitalize_title_style(text: str, minor_words: set[str] | None = None) -> str:
    """Formats sentence in true title style leaving minor connector words lowercase."""
    if minor_words is None:
        minor_words = {"in", "on", "at", "the", "a", "an", "and", "or", "for", "of"}
    words = text.split()
    if not words:
        return ""
    result = []
    for i, w in enumerate(words):
        lw = w.lower()
        if i == 0 or lw not in minor_words:
            result.append(lw.capitalize())
        else:
            result.append(lw)
    return " ".join(result)


def to_camel_case(text: str) -> str:
    """
    Converts space-separated text to lowerCamelCase.
    Example: 'hello world string' -> 'helloWorldString'
    """
    words = text.strip().split()
    if not words:
        return ""
    first = words[0].lower()
    rest = "".join(w.capitalize() for w in words[1:])
    return first + rest


if __name__ == "__main__":
    test_cases = [
        ("hello world", "Hello World"),
        ("python PROGRAMMING is fun", "Python Programming Is Fun"),
        ("a quick brown fox", "A Quick Brown Fox"),
        ("single", "Single"),
    ]

    for sample, expected in test_cases:
        res1 = capitalize_words_manual(sample)
        assert res1 == expected, f"Failed for '{sample}'"
    assert capitalize_title_style("a quick brown fox in the hole") == "A Quick Brown Fox in the Hole"

    # Test camelCase converter
    assert to_camel_case("hello world") == "helloWorld"
    assert to_camel_case("convert to camel case") == "convertToCamelCase"
    assert to_camel_case("") == ""

    print("[PASS] Problem 14: Capitalize Words tests passed successfully!")
