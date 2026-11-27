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
        total += n % 10
        n //= 10
    return total


def sum_of_digits_string(n: int) -> int:
    """Method 2: String conversion with generator sum()"""
    return sum(int(digit) for digit in str(abs(n)))


def digital_root(n: int) -> int:
    """Computes digital root via repeated summation (modulo 9 formula)."""
    n = abs(n)
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


def product_of_digits(n: int) -> int:
    """Computes product of all digits of non-negative integer n."""
    n = abs(n)
    if n == 0:
        return 0
    prod = 1
    while n > 0:
        prod *= (n % 10)
        n //= 10
    return prod


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
        assert sum_of_digits_math(num) == expected
        assert sum_of_digits_string(num) == expected

    assert digital_root(38) == 2
    assert digital_root(0) == 0
    assert digital_root(493193) == 2

    # Test product of digits
    assert product_of_digits(1234) == 24
    assert product_of_digits(905) == 0
    assert product_of_digits(7) == 7

    print("[PASS] All Sum of Digits tests passed successfully!")
