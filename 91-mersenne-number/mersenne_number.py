"""
Problem 91: Check Mersenne Number
Difficulty: Beginner / Easy

Problem Statement:
A Mersenne number is any positive integer of the form 2^k - 1, where k >= 1.
Examples:
  1  = 2^1 - 1 -> True
  3  = 2^2 - 1 -> True
  7  = 2^3 - 1 -> True
  15 = 2^4 - 1 -> True
  31 = 2^5 - 1 -> True
  6  (not of form 2^k - 1) -> False

Concepts:
- Adding 1 to test for power of 2
- Bitwise test (x & (x - 1) == 0)
- Logarithmic checks
"""

def is_mersenne_number(n: int) -> bool:
    """Check if n is of the form 2^k - 1."""
    if n <= 0:
        return False
    target = n + 1
    return (target & (target - 1)) == 0

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 91: Mersenne Number Tests")
    print("=" * 50)

    test_cases = [
        (1, True),
        (3, True),
        (7, True),
        (15, True),
        (31, True),
        (63, True),
        (6, False),
        (10, False),
        (0, False),
    ]

    for num, expected in test_cases:
        res = is_mersenne_number(num)
        print(f"Num: {num:2d} -> Mersenne? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Mersenne Number tests passed successfully!")
