"""
Problem 80: Check Duck Number
Difficulty: Beginner / Easy

Problem Statement:
A Duck Number is a positive number which has at least one zero ('0') in it,
but the zero should not be in the beginning (leading zeros do not count).
Examples:
  1023 -> Has zero, not at start -> True
  2004 -> Has zero, not at start -> True
  70   -> Has zero, not at start -> True
  321  -> No zero -> False
  0123 -> Leading zero (not a Duck number)

Concepts:
- String representation and slicing
- Checking '0' in string[1:]
- Non-negative integer validation
"""

def is_duck_number(s: str) -> bool:
    """Check if string representation of number has '0' after leading digit."""
    s = s.strip()
    if not s or s.startswith("0") or not s.isdigit():
        return False
    return "0" in s[1:]

def is_duck_number_math(num: int) -> bool:
    """Check if positive integer num is a Duck number purely via arithmetic division."""
    if num <= 0:
        return False
    has_zero = False
    temp = num
    while temp > 0:
        if temp % 10 == 0:
            has_zero = True
            break
        temp //= 10
    return has_zero


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 80: Duck Number Tests")
    print("=" * 50)

    test_cases = [
        ("1023", True),
        ("2004", True),
        ("70", True),
        ("321", False),
        ("0123", False),
        ("0", False),
    ]

    for s, expected in test_cases:
        res = is_duck_number(s)
        print(f"Str: '{s}' -> Duck? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {s}"
        if s.isdigit() and not s.startswith("0"):
            assert is_duck_number_math(int(s)) == expected

    print("\n[PASS] All Duck Number tests passed successfully!")
