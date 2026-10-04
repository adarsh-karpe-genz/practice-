"""
Problem 80: Check Magic Number
Difficulty: Beginner / Easy

Problem Statement:
A number is said to be a Magic Number if the recursive sum of its digits
(repeatedly adding the digits until a single-digit number is obtained) is equal to 1.
Examples:
  19  -> 1 + 9 = 10 -> 1 + 0 = 1 -> True (Magic Number)
  1234 -> 1 + 2 + 3 + 4 = 10 -> 1 + 0 = 1 -> True (Magic Number)
  55  -> 5 + 5 = 10 -> 1 + 0 = 1 -> True (Magic Number)
  28  -> 2 + 8 = 10 -> 1 + 0 = 1 -> True (Magic Number)
  12  -> 1 + 2 = 3 != 1 -> False

Concepts:
- Digital root / recursive digit sum
- While loop condition (n > 9)
- Modulo property (digital root == 1 <=> n % 9 == 1 for n > 0)
"""

def is_magic_number(n: int) -> bool:
    """Check if recursive digit sum of n equals 1."""
    if n <= 0:
        return False

    while n > 9:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total

    return n == 1


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 80: Magic Number Tests")
    print("=" * 50)

    test_cases = [
        (19, True),
        (1234, True),
        (55, True),
        (28, True),
        (1, True),
        (10, True),
        (12, False),
        (100, True),
        (0, False),
    ]

    for num, expected in test_cases:
        res = is_magic_number(num)
        print(f"Number: {num:4d} -> Magic? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Magic Number tests passed successfully!")
