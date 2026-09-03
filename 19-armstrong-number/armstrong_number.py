"""
Problem 19: Check Armstrong Number (Narcissistic Number)
Difficulty: Beginner / Easy

Problem Statement:
An Armstrong number (or narcissistic number) of `k` digits is an integer such that
the sum of its digits each raised to the power of `k` is equal to the number itself.
Examples:
- 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 (k=3)
- 9474 is an Armstrong number because 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474 (k=4)
- 10 is NOT an Armstrong number because 1^2 + 0^2 = 1 != 10 (k=2)

Concepts:
- Mathematical digit extraction & powers
- String representation vs pure arithmetic loop
- Handling 0 and single digit numbers
"""

def is_armstrong_math(n: int) -> bool:
    """Method 1: Mathematical digit extraction (O(log10(N)) time, O(1) space)"""
    if n < 0:
        return False
    if n == 0:
        return True

    # Count number of digits k
    temp = n
    k = 0
    while temp > 0:
        k += 1
        temp //= 10

    # Calculate sum of digits raised to power k
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** k
        temp //= 10

    return total == n


def is_armstrong_string(n: int) -> bool:
    """Method 2: String conversion (Pythonic one-liner)"""
    if n < 0:
        return False
    s = str(n)
    k = len(s)
    return sum(int(digit) ** k for digit in s) == n


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 19: Armstrong Number Tests")
    print("=" * 50)

    test_cases = [
        (153, True),
        (370, True),
        (371, True),
        (407, True),
        (9474, True),
        (9, True),
        (0, True),
        (10, False),
        (123, False),
        (-153, False),
    ]

    for num, expected in test_cases:
        res1 = is_armstrong_math(num)
        res2 = is_armstrong_string(num)
        print(f"Number: {num:5d} -> Armstrong? {res1:<5} | Expected: {expected}")
        assert res1 == expected, f"Math method failed for {num}"
        assert res2 == expected, f"String method failed for {num}"

    print("\n[PASS] All Armstrong Number tests passed successfully!")
