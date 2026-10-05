"""
Problem 88: Check Mersenne Prime
Difficulty: Beginner / Easy

Problem Statement:
A Mersenne number is a number that is one less than a power of two: M_p = 2^p - 1.
If M_p is also prime, it is called a Mersenne Prime (this requires p to be prime).
Examples:
  3  = 2^2 - 1 (p=2 is prime, 3 is prime) -> True
  7  = 2^3 - 1 (p=3 is prime, 7 is prime) -> True
  31 = 2^5 - 1 (p=5 is prime, 31 is prime) -> True
  15 = 2^4 - 1 (not prime) -> False

Concepts:
- Power of two relationship (n + 1 is power of 2)
- Primality testing function
- Logarithm base 2 check
"""

import math

def is_prime(n: int) -> bool:
    """Helper to check if n is prime."""
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(n: int) -> bool:
    """Check if n is prime and of the form 2^p - 1 where p is also prime."""
    if not is_prime(n):
        return False
    # Check if n + 1 is a power of 2
    target = n + 1
    if target <= 0 or (target & (target - 1)) != 0:
        return False
    p = target.bit_length() - 1
    return is_prime(p)

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 88: Mersenne Prime Tests")
    print("=" * 50)

    test_cases = [
        (3, True),    # 2^2 - 1
        (7, True),    # 2^3 - 1
        (31, True),   # 2^5 - 1
        (127, True),  # 2^7 - 1
        (15, False),  # 2^4 - 1 (composite)
        (5, False),   # not of form 2^p - 1
        (11, False),
    ]

    for num, expected in test_cases:
        res = is_mersenne_prime(num)
        print(f"Num: {num:3d} -> Mersenne Prime? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Mersenne Prime tests passed successfully!")
