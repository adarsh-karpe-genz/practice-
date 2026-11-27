"""
Problem 02: Reverse a String (Multiple Approaches)
Difficulty: Beginner / Easy

Problem Statement:
Given an input string `s`, return the string reversed.
Example: 'python' -> 'nohtyp'

Concepts:
- Slicing [::-1]
- Loop / Accumulator
- Built-in reversed() + join()
- In-place list two-pointer reversal
"""

def reverse_slicing(s: str) -> str:
    """Method 1: Slicing (Fastest & most common in Python)"""
    return s[::-1]


def reverse_loop(s: str) -> str:
    """Method 2: Using a Loop (Classic accumulator)"""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def reverse_recursive(s: str) -> str:
    """Method 3: Recursive string reversal"""
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]


def reverse_two_pointers(s: str) -> str:
    """Method 4: Two-pointer in-place style reversal using a mutable list"""
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


def reverse_words_preserving_spaces(s: str) -> str:
    """
    Reverses each word individually while preserving original word order and whitespace.
    Example: 'hello world' -> 'olleh dlrow'
    """
    words = s.split(" ")
    return " ".join(reverse_slicing(w) for w in words)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 02: Reverse String Tests")
    print("=" * 50)

    test_words = ["python", "hello", "developer", "a", ""]
    for word in test_words:
        r1 = reverse_slicing(word)
        r2 = reverse_loop(word)
        r3 = reverse_two_pointers(word)
        expected = word[::-1]
        r4 = reverse_recursive(word)
        assert r1 == expected and r2 == expected and r3 == expected and r4 == expected

    # Test word-by-word reversal
    assert reverse_words_preserving_spaces("hello world") == "olleh dlrow"
    assert reverse_words_preserving_spaces("python code") == "nohtyp edoc"

    print("[PASS] All Reverse String tests passed successfully!")
