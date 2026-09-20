"""
Problem 65: Check Harshad Number (Niven Number)
Difficulty: Beginner / Easy

Problem Statement:
A Harshad number (or Niven number) is an integer that is completely divisible
by the sum of its digits.
Example: 18 -> 1 + 8 = 9, and 18 is divisible by 9 (18 % 9 == 0) -> True
Example: 19 -> 1 + 9 = 10, and 19 is not divisible by 10 (19 % 10 != 0) -> False

Concepts:
- Digit summation via modulo and integer division
- Modulo divisibility check
- Mathematical properties of numbers
"""

def is_harshad_number(n: int) -> bool:
    """Determine if a positive integer is a Harshad number."""
    if n <= 0:
        return False

    temp = n
    digit_sum = 0
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    return n % digit_sum == 0


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 65: Harshad Number Tests")
    print("=" * 50)

    test_cases = [
        (18, True),
        (19, False),
        (21, True),
        (153, True),   # 1+5+3 = 9, 153 % 9 == 0
        (42, True),    # 4+2 = 6, 42 % 6 == 0
        (11, False),   # 1+1 = 2, 11 % 2 != 0
        (1, True),
        (0, False),
    ]

    for num, expected in test_cases:
        res = is_harshad_number(num)
        print(f"Number: {num:4d} -> Harshad? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Harshad Number tests passed successfully!")
