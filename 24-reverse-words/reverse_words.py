"""
Problem 24: Reverse Words in a Sentence
Difficulty: Beginner / Easy

Problem Statement:
Given a string sentence of words separated by spaces, reverse the order
of the words while preserving the letters of each word.
Trim leading/trailing spaces and reduce multiple consecutive spaces between words.
Example: "the sky is blue" -> "blue is sky the"

Concepts:
- `.split()` and `.join()`
- Word sequence reversal
"""

def reverse_words_simple(sentence: str) -> str:
    """Reverses order of words using split and reversed."""
    words = sentence.split()
    return " ".join(reversed(words))


def reverse_words_manual(sentence: str) -> str:
    """Manual word splitting and reversal."""
    words = sentence.split()
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return " ".join(words)


def reverse_individual_words_only(sentence: str) -> str:
    """Reverses characters in each word while preserving word order."""
    return " ".join(w[::-1] for w in sentence.split())


def count_words(sentence: str) -> int:
    """Returns total number of words in sentence ignoring whitespace."""
    return len(sentence.split())


if __name__ == "__main__":
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("single", "single"),
        ("", ""),
    ]

    for s, expected in test_cases:
        res1 = reverse_words_simple(s)
        res2 = reverse_words_manual(s)
        assert res1 == expected, f"Failed for '{s}'"
        assert res2 == expected, f"Failed for '{s}'"
    assert reverse_individual_words_only("hello world") == "olleh dlrow"

    # Test count words
    assert count_words("the sky is blue") == 4
    assert count_words("   ") == 0

    print("[PASS] Problem 24: Reverse Words tests passed successfully!")
