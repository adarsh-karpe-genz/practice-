"""
Problem 29: Reverse a Number
Difficulty: Beginner / Easy

Problem Statement:
Given an integer, reverse its digits.
- Negative numbers stay negative after reversing.
- Leading zeros in the reversed number are dropped.
Examples:
  12345  -> 54321
  -6789  -> -9876
  1000   -> 1

Concepts:
- Modulo (%) and integer division (//) for digit extraction
- Sign handling for negative numbers
- String slicing as alternative Pythonic method
"""

def reverse_number_math(n: int) -> int:
    """Method 1: Math-based digit extraction (no string conversion)"""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0

    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return sign * reversed_num


def reverse_number_string(n: int) -> int:
    """Method 2: String slicing (Pythonic approach)"""
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 29: Reverse Number Tests")
    print("=" * 50)

    test_cases = [
        (12345, 54321),
        (-6789, -9876),
        (1000, 1),
        (0, 0),
        (9, 9),
        (100, 1),
        (-100, -1),
    ]

    for num, expected in test_cases:
        r1 = reverse_number_math(num)
        r2 = reverse_number_string(num)
        print(f"Input: {num:6d} -> Reversed: {r1:6d} | Expected: {expected:6d}")
        assert r1 == expected, f"Math method failed for {num}"
        assert r2 == expected, f"String method failed for {num}"

    print("\n[PASS] All Reverse Number tests passed successfully!")
