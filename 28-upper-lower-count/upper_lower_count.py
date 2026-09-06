"""
Problem 28: Count Uppercase and Lowercase Letters in a String
Difficulty: Beginner / Easy

Problem Statement:
Given a string, count the number of uppercase letters (A-Z) and
lowercase letters (a-z) separately. Ignore digits, spaces, and symbols.
Example: "Hello World! 123" -> {'uppercase': 2, 'lowercase': 8}

Concepts:
- String methods: .isupper(), .islower(), .isalpha()
- Dictionary to aggregate counts
- Iteration over characters
"""

from typing import Dict


def count_case(text: str) -> Dict[str, int]:
    """Count uppercase and lowercase alphabetic characters in a string."""
    counts = {"uppercase": 0, "lowercase": 0}
    for char in text:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
    return counts


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 28: Upper/Lower Count Tests")
    print("=" * 50)

    test_cases = [
        ("Hello World! 123", {"uppercase": 2, "lowercase": 8}),
        ("PYTHON", {"uppercase": 6, "lowercase": 0}),
        ("python", {"uppercase": 0, "lowercase": 6}),
        ("12345!@#", {"uppercase": 0, "lowercase": 0}),
        ("", {"uppercase": 0, "lowercase": 0}),
        ("AbCdEf", {"uppercase": 3, "lowercase": 3}),
    ]

    for s, expected in test_cases:
        res = count_case(s)
        print(f"Input: '{s}'")
        print(f"  -> Counts: {res} | Expected: {expected}")
        assert res == expected, f"Failed for '{s}'"

    print("\n[PASS] All Upper/Lower Count tests passed successfully!")
