"""
Problem 54: Roman Numeral to Integer Converter
Difficulty: Beginner / Easy

Problem Statement:
Given a Roman numeral string, convert it to an integer.
Roman numerals are represented by seven different symbols:
  I (1), V (5), X (10), L (50), C (100), D (500), M (1000).
If a smaller numeral appears before a larger numeral, the value is subtracted (e.g. IV = 4, IX = 9).
Examples:
  "III"     -> 3
  "LVIII"   -> 58
  "MCMXCIV" -> 1994

Concepts:
- Dictionary mapping
- Subtractive notation condition: val[i] < val[i+1]
- Linear traversal O(N)
"""

ROMAN_MAP = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to an integer."""
    total = 0
    n = len(s)

    for i in range(n):
        current_val = ROMAN_MAP[s[i]]
        if i + 1 < n and current_val < ROMAN_MAP[s[i + 1]]:
            total -= current_val
        else:
            total += current_val

    return total


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 54: Roman to Integer Tests")
    print("=" * 50)

    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("CDXLIV", 444),
        ("XL", 40),
        ("XC", 90),
    ]

    for roman, expected in test_cases:
        res = roman_to_int(roman)
        print(f"Roman: {roman:10} -> Int: {res:5} | Expected: {expected}")
        assert res == expected, f"Failed for {roman}"

    print("\n[PASS] All Roman to Integer tests passed successfully!")
