"""
Problem 34: Convert Number to Words (1 to 999)
Difficulty: Beginner / Easy

Problem Statement:
Given a positive integer from 1 to 999, convert it to its English word representation.
Examples:
  15  -> "fifteen"
  42  -> "forty two"
  100 -> "one hundred"
  356 -> "three hundred fifty six"

Concepts:
- Lookup tables (lists and dictionaries)
- Integer division // and modulo % to extract hundreds/tens/ones digits
- String joining and formatting
"""

ONES = [
    "", "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

TENS = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]


def number_to_words(n: int) -> str:
    """Convert integer 1-999 to English words."""
    if n <= 0 or n > 999:
        raise ValueError("Input must be between 1 and 999.")

    parts = []

    if n >= 100:
        parts.append(ONES[n // 100] + " hundred")
        n %= 100

    if n >= 20:
        tens_word = TENS[n // 10]
        ones_word = ONES[n % 10]
        parts.append((tens_word + " " + ones_word).strip())
    elif n > 0:
        parts.append(ONES[n])

    return " ".join(parts)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 34: Number to Words Tests")
    print("=" * 50)

    test_cases = [
        (1, "one"),
        (15, "fifteen"),
        (20, "twenty"),
        (42, "forty two"),
        (100, "one hundred"),
        (115, "one hundred fifteen"),
        (356, "three hundred fifty six"),
        (999, "nine hundred ninety nine"),
    ]

    for num, expected in test_cases:
        res = number_to_words(num)
        print(f"{num:4d} -> '{res}' | Expected: '{expected}'")
        assert res == expected, f"Failed for {num}: got '{res}'"

    print("\n[PASS] All Number to Words tests passed successfully!")
