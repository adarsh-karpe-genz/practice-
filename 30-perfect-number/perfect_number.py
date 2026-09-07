"""
Problem 30: Check Perfect Number
Difficulty: Beginner / Easy

Problem Statement:
A perfect number is a positive integer that is equal to the sum of its
proper divisors (all divisors excluding the number itself).
Examples:
  6  is perfect  -> divisors: 1, 2, 3  -> 1+2+3 = 6  ✓
  28 is perfect  -> divisors: 1,2,4,7,14 -> sum = 28  ✓
  12 is NOT      -> divisors: 1,2,3,4,6  -> sum = 16  ✗

Concepts:
- Loop to find divisors up to sqrt(N) for efficiency O(sqrt(N))
- Pair divisors trick: if i divides n, then n//i also divides n
- Edge case: 1 is not a perfect number
"""

import math


def is_perfect_number(n: int) -> bool:
    """Check if n is a perfect number using O(sqrt(N)) divisor search."""
    if n < 2:
        return False

    divisor_sum = 1  # 1 is always a proper divisor for n >= 2

    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid double-counting perfect square divisors
                divisor_sum += n // i

    return divisor_sum == n


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 30: Perfect Number Tests")
    print("=" * 50)

    test_cases = [
        (6, True),
        (28, True),
        (496, True),
        (8128, True),
        (12, False),
        (1, False),
        (0, False),
        (100, False),
    ]

    for num, expected in test_cases:
        res = is_perfect_number(num)
        status = "✓" if res == expected else "✗"
        print(f"{status} {num:5d} -> Perfect? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Perfect Number tests passed successfully!")
