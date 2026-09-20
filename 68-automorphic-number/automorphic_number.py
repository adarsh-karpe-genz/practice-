"""
Problem 68: Check Automorphic Number
Difficulty: Beginner / Easy

Problem Statement:
An automorphic number (or circular number) is a number whose square ends
with the same digits as the number itself.
Examples:
  5  -> 5^2  = 25  (ends in 5)   -> True
  6  -> 6^2  = 36  (ends in 6)   -> True
  25 -> 25^2 = 625 (ends in 25)  -> True
  7  -> 7^2  = 49  (ends in 9)   -> False

Concepts:
- Square computation
- String endswith() method vs modulo arithmetic
- Mathematical number theory
"""

def is_automorphic(n: int) -> bool:
    """Determine if a non-negative integer is an automorphic number."""
    if n < 0:
        return False
    square = n * n
    return str(square).endswith(str(n))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 68: Automorphic Number Tests")
    print("=" * 50)

    test_cases = [
        (5, True),
        (6, True),
        (25, True),
        (76, True),   # 76^2 = 5776
        (7, False),
        (10, False),
        (0, True),    # 0^2 = 0
        (1, True),    # 1^2 = 1
    ]

    for num, expected in test_cases:
        res = is_automorphic(num)
        print(f"Number: {num:3d} (Square: {num*num:5d}) -> Automorphic? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Automorphic Number tests passed successfully!")
