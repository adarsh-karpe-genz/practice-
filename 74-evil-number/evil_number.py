"""
Problem 74: Check Evil Number
Difficulty: Beginner / Easy

Problem Statement:
A non-negative integer is called an Evil Number if its binary expansion
contains an EVEN number of 1s. Otherwise (odd number of 1s), it is an Odious Number.
Examples:
  3  -> Binary "11"   (two 1s, which is even)  -> True (Evil Number)
  5  -> Binary "101"  (two 1s, which is even)  -> True (Evil Number)
  9  -> Binary "1001" (two 1s, which is even)  -> True (Evil Number)
  7  -> Binary "111"  (three 1s, which is odd) -> False (Odious Number)

Concepts:
- Decimal to binary representation bin()
- Counting bits with .count("1")
- Bitwise parity check
"""

def is_evil_number(n: int) -> bool:
    """Check if n has an even count of set bits (1s) in binary."""
    if n < 0:
        return False
    set_bits_count = bin(n).count("1")
    return set_bits_count % 2 == 0


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 74: Evil Number Tests")
    print("=" * 50)

    test_cases = [
        (3, True),    # 11 -> 2
        (5, True),    # 101 -> 2
        (6, True),    # 110 -> 2
        (9, True),    # 1001 -> 2
        (0, True),    # 0 -> 0 (0 is even)
        (1, False),   # 1 -> 1
        (2, False),   # 10 -> 1
        (7, False),   # 111 -> 3
        (15, True),   # 1111 -> 4
    ]

    for num, expected in test_cases:
        res = is_evil_number(num)
        print(f"Number: {num:2d} ({bin(num):>6}) -> Evil? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Evil Number tests passed successfully!")
