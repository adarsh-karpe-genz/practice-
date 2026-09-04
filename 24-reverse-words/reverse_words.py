"""
Problem 24: Reverse Words in a Sentence
Difficulty: Beginner / Easy

Problem Statement:
Given a string sentence of words separated by spaces, reverse the order
of the words while preserving the letters of each word.
Trim leading/trailing spaces and reduce multiple consecutive spaces between words.
Example: "the sky is blue" -> "blue is sky the"
Example: "  hello world  " -> "world hello"

Concepts:
- String tokenization with .split() (handles multiple spaces)
- List reversal [::-1] or reversed()
- String joining with ' '.join()
"""

def reverse_words_simple(sentence: str) -> str:
    """Method 1: Slicing with split() and join() (Pythonic one-liner)"""
    words = sentence.split()
    return " ".join(words[::-1])


def reverse_words_manual(sentence: str) -> str:
    """Method 2: Using reversed() iterator"""
    words = sentence.split()
    return " ".join(reversed(words))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 24: Reverse Words Tests")
    print("=" * 50)

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
        print(f"Original: '{s}' -> Reversed Words: '{res1}' | Expected: '{expected}'")
        assert res1 == expected, f"Failed for '{s}'"
        assert res2 == expected, f"Failed for '{s}'"

    print("\n[PASS] All Reverse Words tests passed successfully!")
