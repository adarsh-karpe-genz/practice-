"""
Problem 79: Check Strong Number (Peterson / Krishnamurthy Number)
Difficulty: Beginner / Easy

Problem Statement:
A number is called a Strong Number if the sum of the factorials of each of its
digits is equal to the number itself.
Examples:
  145 -> 1! + 4! + 5! = 1 + 24 + 120 = 145 -> True
  2   -> 2! = 2 -> True
  123 -> 1! + 2! + 3! = 1 + 2 + 6 = 9 != 123 -> False

Concepts:
- math.factorial lookup
- Digit extraction via modulo % and division //
- Factorial digit sum comparison
"""

import math

def is_strong_number(n: int) -> bool:
    """Check if sum of factorials of digits of n equals n."""
    if n <= 0:
        return False
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)
        temp //= 10
    return total == n

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 79: Strong Number Tests")
    print("=" * 50)

    test_cases = [
        (145, True),
        (1, True),
        (2, True),
        (40585, True),
        (123, False),
        (10, False),
    ]

    for num, expected in test_cases:
        res = is_strong_number(num)
        print(f"Num: {num:5d} -> Strong? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Strong Number tests passed successfully!")
