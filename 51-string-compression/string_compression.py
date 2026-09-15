"""
Problem 51: String Compression (Run-Length Encoding)
Difficulty: Beginner / Easy

Problem Statement:
Implement basic string compression using the counts of repeated characters.
Example: "aabcccccaaa" -> "a2b1c5a3"
If the compressed string is not shorter than the original, return original or compressed based on mode.

Concepts:
- Consecutive character frequency counting
- Loop tracking of previous char and count
- StringBuilder pattern using list appending
"""

def compress_string(text: str) -> str:
    """Perform run-length compression on string."""
    if not text:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(f"{text[i - 1]}{count}")
            count = 1

    compressed.append(f"{text[-1]}{count}")
    return "".join(compressed)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 51: String Compression Tests")
    print("=" * 50)

    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcd", "a1b1c1d1"),
        ("aaaa", "a4"),
        ("", ""),
        ("a", "a1"),
    ]

    for s, expected in test_cases:
        res = compress_string(s)
        print(f"Input: '{s}' -> Compressed: '{res}' | Expected: '{expected}'")
        assert res == expected, f"Failed for '{s}'"

    print("\n[PASS] All String Compression tests passed successfully!")
