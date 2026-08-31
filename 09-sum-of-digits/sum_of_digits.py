"""
Problem 09: Sum of Digits of a Number
Difficulty: Beginner / Easy

Problem Statement:
Given a non-negative integer `n`, compute the sum of all its individual digits.
Example: 1234 -> 1 + 2 + 3 + 4 = 10
Example: 905  -> 9 + 0 + 5 = 14

Concepts:
- Mathematical extraction using modulo (%) and integer division (//)
- String conversion and generator expression sum()
- Handling single digits and zero
"""

def sum_of_digits_math(n: int) -> int:
    """Method 1: Mathematical modulo approach (O(log10(N)) time, O(1) space)"""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10  # extract last digit
        n //= 10         # remove last digit
    return total


def sum_of_digits_string(n: int) -> int:
    """Method 2: String conversion (Pythonic one-liner)"""
    return sum(int(digit) for digit in str(abs(n)))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 09: Sum of Digits Tests")
    print("=" * 50)

    test_cases = [
        (1234, 10),
        (905, 14),
        (0, 0),
        (7, 7),
        (99999, 45),
        (-582, 15),
    ]

    for num, expected in test_cases:
        res1 = sum_of_digits_math(num)
        res2 = sum_of_digits_string(num)
        print(f"Number: {num:6d} -> Sum: {res1:2d} | Expected: {expected:2d}")
        assert res1 == expected, f"Math method failed for {num}"
        assert res2 == expected, f"String method failed for {num}"

    print("\n[PASS] All Sum of Digits tests passed successfully!")
