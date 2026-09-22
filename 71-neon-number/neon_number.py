"""
Problem 71: Check Neon Number
Difficulty: Beginner / Easy

Problem Statement:
A positive integer is called a Neon Number if the sum of the digits of its
square equals the number itself.
Examples:
  9 -> 9^2 = 81 -> 8 + 1 = 9  -> True (Neon Number)
  1 -> 1^2 = 1  -> 1          -> True (Neon Number)
  0 -> 0^2 = 0  -> 0          -> True (Neon Number)
  12 -> 12^2 = 144 -> 1 + 4 + 4 = 9 != 12 -> False

Concepts:
- Number squaring
- Digit summation on square
- Number theory properties
"""

def is_neon_number(n: int) -> bool:
    """Check if the sum of digits of n^2 equals n."""
    if n < 0:
        return False
    sq = n * n
    digit_sum = sum(int(digit) for digit in str(sq))
    return digit_sum == n


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 71: Neon Number Tests")
    print("=" * 50)

    test_cases = [
        (9, True),
        (1, True),
        (0, True),
        (12, False),
        (45, False),
        (8, False),
    ]

    for num, expected in test_cases:
        res = is_neon_number(num)
        print(f"Number: {num:2d} -> Neon? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Neon Number tests passed successfully!")
