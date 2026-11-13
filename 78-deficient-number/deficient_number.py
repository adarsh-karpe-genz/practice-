"""
Problem 78: Check Deficient Number
Difficulty: Beginner / Easy

Problem Statement:
A deficient number is a positive integer for which the sum of its proper divisors
is strictly less than the number itself.
Examples:
  15 -> Divisors: 1, 3, 5 -> Sum = 9 < 15 -> True
  21 -> Divisors: 1, 3, 7 -> Sum = 11 < 21 -> True
  12 -> Divisors: 1, 2, 3, 4, 6 -> Sum = 16 > 12 -> False

Concepts:
- Proper divisors summation
- Comparison with original number
- Number theory classifications: abundant, perfect, deficient
"""

import math

def is_deficient(n: int) -> bool:
    """Check if sum of proper divisors of n is less than n."""
    if n <= 0:
        return False
    if n == 1:
        return True  # Proper divisors of 1 is empty sum = 0 < 1
    divisor_sum = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum < n

def deficiency_value(n: int) -> int:
    """Return 2n - sigma(n) (the deficiency of n), where sigma(n) is sum of all divisors."""
    if n <= 0:
        return 0
    sigma = sum(d for d in range(1, n + 1) if n % d == 0)
    return 2 * n - sigma


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 78: Deficient Number Tests")
    print("=" * 50)

    test_cases = [
        (15, True),
        (21, True),
        (1, True),
        (14, True),
        (12, False),
        (18, False),
        (6, False),  # 6 is perfect (sum = 6)
    ]

    for num, expected in test_cases:
        res = is_deficient(num)
        print(f"Num: {num:3d} -> Deficient? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"
    assert deficiency_value(15) == 6  # 2*15 - (1+3+5+15) = 30 - 24 = 6
    assert deficiency_value(8) == 1   # 2*8 - (1+2+4+8) = 16 - 15 = 1

    print("\n[PASS] All Deficient Number tests passed successfully!")
