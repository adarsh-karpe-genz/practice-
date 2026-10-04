"""
Problem 82: Check Tech Number
Difficulty: Beginner / Easy

Problem Statement:
A Tech Number is a number with an even number of digits that, when split into two
equal halves, the square of the sum of these halves is equal to the number itself.
Examples:
  2025 -> Split into 20 and 25 -> Sum: 20 + 25 = 45 -> 45^2 = 2025 -> True!
  3025 -> Split into 30 and 25 -> Sum: 30 + 25 = 55 -> 55^2 = 3025 -> True!
  81   -> Split into 8 and 1   -> Sum: 8 + 1 = 9    -> 9^2 = 81    -> True!
  1234 -> Split into 12 and 34 -> Sum: 46           -> 46^2 = 2116 != 1234 -> False

Concepts:
- Even digit length verification
- Halving string and integer conversion
- Squaring sum of halves
"""

def is_tech_number(n: int) -> bool:
    """Check if number satisfies Tech Number property."""
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    first_half = int(s[:half])
    second_half = int(s[half:])
    return (first_half + second_half) ** 2 == n

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 82: Tech Number Tests")
    print("=" * 50)

    test_cases = [
        (2025, True),
        (3025, True),
        (9801, True),  # 98 + 01 = 99 -> 99^2 = 9801
        (81, True),
        (1234, False),
        (100, False),  # odd digits
    ]

    for num, expected in test_cases:
        res = is_tech_number(num)
        print(f"Num: {num:4d} -> Tech Number? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Tech Number tests passed successfully!")
