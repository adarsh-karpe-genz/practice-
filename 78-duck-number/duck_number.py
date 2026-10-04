"""
Problem 78: Check Duck Number
Difficulty: Beginner / Easy

Problem Statement:
A Duck number is a positive number which has zeroes present in it,
but there should be NO zero at the beginning of the number.
Examples:
  1023 -> Contains 0, no leading 0 -> True (Duck Number)
  50   -> Contains 0, no leading 0 -> True (Duck Number)
  321  -> No 0 -> False
  0123 -> Leading 0 (if treated as string) -> False

Concepts:
- String checking and membership testing
- Ignoring leading zeros / verifying positive integer string
"""

def is_duck_number(s: str) -> bool:
    """Check if string s represents a Duck number."""
    if not s or s[0] == '0':
        return False
    return '0' in s


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 78: Duck Number Tests")
    print("=" * 50)

    test_cases = [
        ("1023", True),
        ("50", True),
        ("2004", True),
        ("321", False),
        ("0123", False),
        ("0", False),
        ("7", False),
    ]

    for s_val, expected in test_cases:
        res = is_duck_number(s_val)
        print(f"String: '{s_val}' -> Duck? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {s_val}"

    print("\n[PASS] All Duck Number tests passed successfully!")
