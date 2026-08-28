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
    """Method 2: Using a Loop (Classic algorithmic foundation)"""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def reverse_two_pointers(s: str) -> str:
    """Method 3: In-place list two pointers"""
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


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
        print(f"Original: '{word}' -> Reversed: '{r1}'")
        assert r1 == expected and r2 == expected and r3 == expected

    print("\n[PASS] All Reverse String tests passed successfully!")
