"""
Problem 87: Check Kaprekar Number
Difficulty: Beginner / Easy

Problem Statement:
A Kaprekar number is a positive integer whose square in that base can be split
into two parts that add up to the original number itself.
Examples:
  9  -> 9^2 = 81  -> 8 + 1 = 9  -> True
  45 -> 45^2 = 2025 -> 20 + 25 = 45 -> True
  55 -> 55^2 = 3025 -> 30 + 25 = 55 -> True
  1  -> 1^2 = 1   -> 0 + 1 = 1  -> True
  10 -> 10^2 = 100 -> split halves don't sum to 10 -> False

Concepts:
- Number squaring
- Splitting digits using string slicing or powers of 10
- Sum of two halves
"""

def is_kaprekar_number(n: int) -> bool:
    """Check if n is a Kaprekar number."""
    if n <= 0:
        return False
    if n == 1:
        return True

    sq = n * n
    s = str(sq)
    d = len(str(n))

    # The right part has d digits, the left has the rest
    right_str = s[-d:]
    left_str = s[:-d]

    right_val = int(right_str) if right_str else 0
    left_val = int(left_str) if left_str else 0

    return (left_val + right_val == n) and (right_val > 0)

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 87: Kaprekar Number Tests")
    print("=" * 50)

    test_cases = [
        (1, True),
        (9, True),
        (45, True),
        (55, True),
        (297, True),  # 297^2 = 88209 -> 88 + 209 = 297
        (10, False),
        (12, False),
        (100, False),
    ]

    for num, expected in test_cases:
        res = is_kaprekar_number(num)
        print(f"Num: {num:3d} -> Kaprekar? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Kaprekar Number tests passed successfully!")
