"""
Problem 20: Leap Year Checker
Difficulty: Beginner / Easy

Problem Statement:
Given a year integer, determine whether it is a Leap Year.
Rules for Gregorian Calendar:
1. A year is a leap year if it is evenly divisible by 4,
2. UNLESS it is divisible by 100, then it is NOT a leap year,
3. EXCEPT if it is also divisible by 400, then it IS a leap year.

Examples:
- 2000: Divisible by 4, 100, and 400 -> Leap Year (True)
- 1900: Divisible by 4 and 100, but NOT 400 -> Not a Leap Year (False)
- 2024: Divisible by 4, NOT 100 -> Leap Year (True)
"""

import calendar


def is_leap_year(year: int) -> bool:
    """Checks if year is leap year in Gregorian calendar."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def next_leap_year(start_year: int) -> int:
    """Finds the next leap year strictly following start_year."""
    y = start_year + 1
    while not is_leap_year(y):
        y += 1
    return y


def count_leap_years_in_range(start_year: int, end_year: int) -> int:
    """
    Counts total leap years in range [start_year, end_year] inclusive.
    """
    return sum(1 for y in range(start_year, end_year + 1) if is_leap_year(y))


if __name__ == "__main__":
    test_cases = [
        (2000, True),
        (1900, False),
        (2024, True),
        (2023, False),
        (2020, True),
        (2004, True),
    ]

    for y, expected in test_cases:
        res = is_leap_year(y)
        assert res == expected, f"Failed for year {y}"
        assert res == calendar.isleap(y)
    assert next_leap_year(2020) == 2024
    assert next_leap_year(2024) == 2028

    # Test count in range
    assert count_leap_years_in_range(2000, 2024) == 7  # 2000, 04, 08, 12, 16, 20, 24

    print("[PASS] Problem 20: Leap Year tests passed successfully!")
