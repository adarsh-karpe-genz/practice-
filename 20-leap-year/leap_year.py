"""
Problem 20: Leap Year Checker
Difficulty: Beginner / Easy

Problem Statement:
Given a year as an integer, determine whether it is a Leap Year.
Rules:
1. A year is a leap year if it is divisible by 4,
2. UNLESS it is divisible by 100, in which case it must also be divisible by 400.
Examples:
- 2000 is a leap year (divisible by 400).
- 1900 is NOT a leap year (divisible by 100, but not 400).
- 2024 is a leap year (divisible by 4, not 100).
- 2023 is NOT a leap year.

Concepts:
- Compound Boolean logic (and, or, not)
- Modulo operator (%)
- calendar.isleap standard library comparison
"""

import calendar


def is_leap_year(year: int) -> bool:
    """Determine if a year is a leap year using standard Gregorian rules."""
    if year <= 0:
        raise ValueError("Year must be a positive integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def next_leap_year(start_year: int) -> int:
    """Return the very next leap year strictly greater than start_year."""
    year = start_year + 1
    while not is_leap_year(year):
        year += 1
    return year


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 20: Leap Year Tests")
    print("=" * 50)

    test_cases = [
        (2000, True),
        (2400, True),
        (1900, False),
        (2100, False),
        (2024, True),
        (2023, False),
        (2020, True),
        (2004, True),
    ]

    for y, expected in test_cases:
        res = is_leap_year(y)
        print(f"Year: {y} -> Leap Year? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for year {y}"
        # Validate against calendar module
        assert res == calendar.isleap(y)
    assert next_leap_year(2020) == 2024
    assert next_leap_year(2024) == 2028

    print("\n[PASS] All Leap Year tests passed successfully!")
