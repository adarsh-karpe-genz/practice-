"""
Problem 93: Check Cullen Number
Difficulty: Beginner / Easy

Problem Statement:
A Cullen number is any natural number of the form:
  C_n = n * 2^n + 1, where n >= 1.
First few Cullen numbers:
  n = 1 -> 1 * 2^1 + 1 = 3
  n = 2 -> 2 * 2^2 + 1 = 9
  n = 3 -> 3 * 2^3 + 1 = 25
  n = 4 -> 4 * 2^4 + 1 = 65
  n = 5 -> 5 * 2^5 + 1 = 161

Concepts:
- Sequence generation formula
- Search loop until generated term >= target
- Mathematical number theory
"""

def is_cullen_number(val: int) -> bool:
    """Check if val is of the form n * 2^n + 1 for n >= 1."""
    if val < 3:
        return False
    n = 1
    while True:
        c = n * (2 ** n) + 1
        if c == val:
            return True
        if c > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 93: Cullen Number Tests")
    print("=" * 50)

    test_cases = [
        (3, True),
        (9, True),
        (25, True),
        (65, True),
        (161, True),
        (4, False),
        (10, False),
        (30, False),
    ]

    for num, expected in test_cases:
        res = is_cullen_number(num)
        print(f"Num: {num:3d} -> Cullen? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Cullen Number tests passed successfully!")
