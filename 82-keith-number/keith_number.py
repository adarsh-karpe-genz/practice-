"""
Problem 82: Check Keith Number
Difficulty: Beginner / Easy

Problem Statement:
A Keith number (or repfigit number) is an n-digit number that appears in a
Fibonacci-like sequence starting with its own digits, where each subsequent
term is the sum of the previous n terms.
Examples:
  19 (2 digits) -> Sequence: 1, 9, 10 (1+9), 19 (9+10) -> Contains 19 -> True
  14 (2 digits) -> Sequence: 1, 4, 5, 9, 14 -> True
  75 (2 digits) -> 7, 5, 12, 17, 29, 46, 75 -> True
  12 -> 1, 2, 3, 5, 8, 13 (> 12) -> False

Concepts:
- Sequence generation with rolling window of size k
- sum(terms[-k:]) accumulation
- Loop termination: term >= n
"""

def is_keith_number(n: int) -> bool:
    """Determine if n is a Keith number."""
    digits = [int(ch) for ch in str(n)]
    k = len(digits)
    if k < 2:
        return False

    terms = list(digits)
    while terms[-1] < n:
        next_val = sum(terms[-k:])
        terms.append(next_val)

    return terms[-1] == n


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 82: Keith Number Tests")
    print("=" * 50)

    test_cases = [
        (14, True),
        (19, True),
        (75, True),
        (197, True),   # 1, 9, 7, 17, 33, 57, 107, 197
        (12, False),
        (25, False),
        (9, False),    # single digit not considered Keith
    ]

    for num, expected in test_cases:
        res = is_keith_number(num)
        print(f"Number: {num:3d} -> Keith? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Keith Number tests passed successfully!")
