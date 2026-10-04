"""
Problem 83: Check Keith Number (Repfigit Number)
Difficulty: Beginner / Easy

Problem Statement:
A Keith Number is an n-digit number that appears in a sequence generated
using its own digits as the starting terms, where each subsequent term is
the sum of the previous n terms.
Example:
  197 (3 digits):
  Start terms: 1, 9, 7
  Next term: 1 + 9 + 7 = 17
  Next term: 9 + 7 + 17 = 33
  Next term: 7 + 17 + 33 = 57
  Next term: 17 + 33 + 57 = 107
  Next term: 33 + 57 + 107 = 197 (Matches 197!) -> True

Concepts:
- Fibonacci-like sequence generation
- Sliding window / list queue of size n
- Loop until term >= target
"""

def is_keith_number(n: int) -> bool:
    """Check if n is a Keith Number."""
    if n < 10:
        return False
    digits = [int(d) for d in str(n)]
    k = len(digits)
    seq = digits[:]

    while True:
        next_val = sum(seq[-k:])
        if next_val == n:
            return True
        if next_val > n:
            return False
        seq.append(next_val)

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 83: Keith Number Tests")
    print("=" * 50)

    test_cases = [
        (14, True),    # 1, 4 -> 5 -> 9 -> 14
        (19, True),    # 1, 9 -> 10 -> 19
        (197, True),
        (742, True),
        (15, False),
        (100, False),
    ]

    for num, expected in test_cases:
        res = is_keith_number(num)
        print(f"Num: {num:3d} -> Keith Number? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Keith Number tests passed successfully!")
