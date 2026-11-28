"""
Problem 19: Armstrong Number Checker (Narcissistic Number)
Difficulty: Beginner / Easy

Problem Statement:
An Armstrong number is an n-digit number that is equal to the sum
of its digits each raised to the power of n.
Example 1: 153 is a 3-digit number -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 (True)
Example 2: 9474 is a 4-digit number -> 9^4 + 4^4 + 7^4 + 4^4 = 9474 (True)

Concepts:
- Digit extraction via modulo / string
- Power computation `digit ** num_digits`
"""

from typing import List


def is_armstrong_math(n: int) -> bool:
    """Mathematical modulo-based extraction."""
    if n < 0:
        return False
    if n == 0:
        return True
    temp = n
    num_digits = 0
    while temp > 0:
        num_digits += 1
        temp //= 10
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    return total == n


def is_armstrong_string(n: int) -> bool:
    """String-based digit power summation."""
    if n < 0:
        return False
    s = str(n)
    power = len(s)
    return sum(int(d) ** power for d in s) == n


def find_armstrong_numbers(start: int, end: int) -> List[int]:
    """Finds all Armstrong numbers in range [start, end]."""
    return [x for x in range(start, end + 1) if is_armstrong_string(x)]


def armstrong_sum_discrepancy(n: int) -> int:
    """
    Computes the discrepancy: sum(d^k) - n.
    Returns 0 if and only if n is an Armstrong number.
    """
    s = str(abs(n))
    power = len(s)
    digit_sum = sum(int(d) ** power for d in s)
    return digit_sum - abs(n)


if __name__ == "__main__":
    test_cases = [
        (153, True),
        (9474, True),
        (370, True),
        (371, True),
        (407, True),
        (1, True),
        (0, True),
        (10, False),
        (123, False),
        (-153, False),
    ]

    for num, expected in test_cases:
        res1 = is_armstrong_math(num)
        res2 = is_armstrong_string(num)
        assert res1 == expected, f"Math method failed for {num}"
        assert res2 == expected, f"String method failed for {num}"

    assert find_armstrong_numbers(0, 153) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]

    # Test discrepancy
    assert armstrong_sum_discrepancy(153) == 0
    assert armstrong_sum_discrepancy(10) == (1**2 + 0**2) - 10  # 1 - 10 = -9

    print("[PASS] Problem 19: Armstrong Number tests passed successfully!")
