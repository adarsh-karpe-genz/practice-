"""
Problem 81: Check Happy Number
Difficulty: Beginner / Easy

Problem Statement:
A Happy Number is a number which eventually reaches 1 when replaced by
the sum of the square of each digit repeatedly.
If the cycle repeats endlessly without reaching 1, it is an unhappy (sad) number.
Examples:
  19 -> 1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> 6^2 + 8^2 = 100 -> 1^2 + 0^2 + 0^2 = 1 -> True
  2  -> enters loop 4, 16, 37, 58, 89, 145, 42, 20, 4 -> False

Concepts:
- Hash set for cycle detection (seen numbers)
- Sum of squared digits calculation
- While loop termination condition
"""

def is_happy_number(n: int) -> bool:
    """Determine if a number is happy using a set to detect cycles."""
    if n <= 0:
        return False

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return n == 1


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 81: Happy Number Tests")
    print("=" * 50)

    test_cases = [
        (19, True),
        (7, True),
        (1, True),
        (2, False),
        (4, False),
        (20, False),
    ]

    for num, expected in test_cases:
        res = is_happy_number(num)
        print(f"Number: {num:2d} -> Happy? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Happy Number tests passed successfully!")
